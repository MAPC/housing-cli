import xlsxwriter
import requests
from xlsxwriter.utility import xl_rowcol_to_cell
import psycopg2
import pandas as pd
from pandas.io import sql
from pandas.io.sql import read_sql
import requests
import sys
import time
import os 
import numpy
import traceback
from census import Census
from us import states
import sqlparse
from sqlparse.sql import Identifier
from itertools import cycle

class Workbook(object):
  def __init__(self):
    self.title = "Charts"
    self.writer = pd.ExcelWriter("output/%s.xlsx"% self.title, engine='xlsxwriter')
    self.workbook = self.writer.book


  def close(self):
    self.workbook.close()

class Batch(object):
  def __init__(self, workbook, muni_id):
    self.Workbook = workbook
    self.muni_id = muni_id

class DataGrid(object):
  """Pulls data from SQL db and projects it onto an Excel worksheet"""

  def __init__(self, batch, sql, headings):
    conn2 = psycopg2.connect("host=db.dev.mapc.org user=editor password=M999PCedit.451 dbname=datasets")
    self.Batch = batch
    self.sql = sql
    self.headings = headings
    self.full_crosswalk = read_sql("SELECT * FROM public._datakeys_muni351", conn2, coerce_float=True, params=None)
    self.keys = self.full_crosswalk[self.full_crosswalk["muni_id"] == self.Batch.muni_id]
    self.cousub_fips = self.keys["COUSUB"].tolist()[0]
    self.county_fips = self.keys["county_id"].tolist()[0]
    self.munged = self.data() # This stores the final form after a munge occurs
    self.subregions = read_sql("SELECT * FROM public.mapc_subregions", conn2, coerce_float=True, params=None)
    self.subregion = self.subregions[self.subregions['MUNI_ID']==self.Batch.muni_id]["Subregion"].tolist()[0]
    self.subregional_munis = self.subregions[self.subregions["Subregion"].isin(["SWAP", "TRIC", "METROWEST"])]
    self.census_api = Census("a036e6c9b1f578e84bafe0a0514bb4faf59359dc")

    #Cross walk
    # crosswalk_sql = "SELECT * FROM tabular._datakeys_muni351 WHERE muni_id = %s" % self.Batch.muni_id
    self.crosswalk = self.keys
    self.county = self.crosswalk[self.crosswalk['muni_id']==self.Batch.muni_id]["county"].tolist()[0]
    self.muni_name = self.crosswalk[self.crosswalk["muni_id"] == self.Batch.muni_id]["municipal"].tolist()[0]
    self.table_name = self.get_table_name()

    self.metadata = read_sql("SELECT * FROM metadata.%s" % self.table_name, self.conn(), coerce_float=True, params=None)
    self.creator = self.metadata[self.metadata['name']=="creator"]["details"].tolist()[0]
    # self.tablename = self.metadata[self.metadata['name']=="tbl_table"]["details"].tolist()[0]
    # self.year_column = dataset.data().columns[dataset.data().columns.str.contains("y**r")][0]
    # self.year = dataset.metadata[dataset.metadata['name']=="creator"]

  def data(self):
    return read_sql(self.sql, self.conn(), coerce_float=True, params=None)

  def get_table_name(self):
    for token in sqlparse.parse(self.sql)[0].tokens:
      if isinstance(token, Identifier):
        split = str(token).split(".")
        last = len(split) - 1
        return split[last]

  def conn(self, string="host=10.10.10.240 user=dsviewer password=dsview933 dbname=ds"):
    return psycopg2.connect(string)

  def munge(self, fun):
    """ Arrange the dataframe exactly as needed """
    fun(self)

  def bbox(self):
    """ Returns tuple of width, height """
    # expects zero-based counting when calculating
    return tuple([xl_rowcol_to_cell(0, self.shape()[1]), xl_rowcol_to_cell(self.shape()[0], 0)])

  def shape(self):
    """ Returns the zero-based coordinates of munged DataFrame """
    # return tuple(numpy.subtract(self.munged.shape, (1,1)))
    return self.munged.shape

  def columns(self):
    return self.munged.columns.values

  def project(self, title):
    """ Projects pandas DataFrame object onto Excel worksheet
        and stores information about that grid """

    self.munged.to_excel(self.Batch.Workbook.writer, sheet_name=title, index=False)
    self.worksheet = self.Batch.Workbook.writer.sheets[title]
    self.worksheet.write(self.shape()[0] + 1, 0, "Source: %s" % self.creator)
    # self.worksheet.write(self.shape()[0] + 2, 0, "Table Name: %s" % self.tablename)

class Chart(object):
  """Chart has a DataGrid and belongs to Batch"""

  def __init__(self, batch, dataset, title):
    self.Batch = batch
    self.DataGrid = dataset
    self.title = title
    self.colors = cycle(["#2b4c80", "#B6CF8A", "#808080", "#83C3D5", "#FDB509", "#000000"])

  def generate(self, type = "column", subtype = ""):
    self.DataGrid.project(self.title)
    self.worksheet = self.Batch.Workbook.writer.sheets[self.title]
    self.__chart(type=type, subtype=subtype)

  ### Private

  def __categories(self):
    return [self.title, 1, 0, self.DataGrid.shape()[0], 0]

  def __chart(self, type="column", subtype=""):
    self.chart = self.Batch.Workbook.workbook.add_chart({'type': type, 'subtype': subtype})
    self.chart.set_size({'width': 720, 'height': 576})
    # iterate over all columns - they are the series
    for idx, val in enumerate(self.DataGrid.columns()):

      # skip the first - it's for categories only.
      if(idx != 0):

        self.chart.add_series({
          'name':       [self.title, 0, idx], 
          'categories': self.__categories(), 
          'values':     [self.title, 1, idx, self.DataGrid.shape()[0], idx],
          'data_labels': {'value': True},
          'fill':   {'color': next(self.colors)},
        })

    self.worksheet.insert_chart(xl_rowcol_to_cell(0, self.DataGrid.shape()[1] + 1), self.chart)
