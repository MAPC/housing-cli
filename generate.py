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
import glob 

class Workbook(object):
  def __init__(self):
    self.writer = pd.ExcelWriter("Charts.xlsx", engine='xlsxwriter')
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
    self.Batch = batch
    self.sql = sql
    self.headings = headings
    self.munged = self.data() # This stores the final form after a munge occurs

  def data(self):
    return read_sql(self.sql, self.conn(), coerce_float=True, params=None)

  def conn(self):
    return psycopg2.connect("")

  def munge(self):
    """ arrange the dataframe exactly as needed """
    fun(self)

  def project(self):
    """ projects pandas DataFrame object onto Excel worksheet
        and stores information about that grid """

    self.munged.to_excel(self.Batch.Workbook.writer, sheet_name="Test", index=False)
    self.worksheet = self.Batch.Workbook.writer.sheets["Test"]
  
  def worksheet(self):
    return workbook.add_worksheet("Sheetname")

class Chart(object):
  """Chart has a DataGrid and belongs to Batch"""

  def __init__(self, batch, dataset, title):
    self.Batch = batch
    self.DataGrid = dataset
    self.title = title

  def generate(self, fun, *args):
    self.DataGrid.project()
    fun(self)



