#!/usr/bin/python
# coding: utf-8

# # Automated HNDA Excel Charts
# 
# Because we are starting to see the same requests for our housing needs and demand analyses, let's build those workflows into code here.



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

CWD = os.getcwd()

# Set the muni id for the generated charts
MUNI_ID = int(sys.argv[1])


def camelize(file):
   first, *rest = file.split('_')
   return first + ''.join(word.capitalize() for word in rest)


### CODE BLOBS

charts = glob.glob("./charts/*.py")
chart_pairings = dict()
for chart in charts: 
    chart_pairings[camelize(chart.replace("./charts/", "").replace(".py",""))] = open(chart).read()



# Chart Helpers

# Bar Chart:
# Inserts new worksheet to the given workbook. 
# Requires string or numeric label as array, list or Pandas Series.

def column(workbook, labels, series1, *others, type='column', subtype = '', headings = ["Series", "values"], sheetname="Sheet"):
    worksheet = workbook.add_worksheet(sheetname)
    length = len(labels)
    sheet_name = worksheet.get_name()
    
    chart1 = workbook.add_chart({'type': type, 'subtype': subtype})
    worksheet.write_row('A1', headings, bold)
    worksheet.write_column("A2", labels)
    
    worksheet.write_column("B2", series1)
    chart1.add_series({
        'name':       [sheet_name, 0, 1], 
        'categories': [sheet_name, 1, 0,length,0], # '=%s!$A$2:$A$%s' % (sheet_name, length),
        'values':     [sheet_name, 1, 1,length,1], #'=%s!$B$2:$B$%s' % (sheet_name, length),
        'data_labels': {'value': True}
    })
    
    for idx, val in enumerate(others):
        cell = xl_rowcol_to_cell(1,idx+2)
        worksheet.write_column(cell, val)
        chart1.add_series({
            'name':       [sheet_name, 0, idx+2], 
            'categories': [sheet_name, 1, 0,length,0], # '=%s!$A$2:$A$%s' % (sheet_name, length),
            'values':     [sheet_name, 1, idx+2,length,idx+2], #'=%s!$B$2:$B$%s' % (sheet_name, length),
            'data_labels': {'value': True},
        })
    
    worksheet.insert_chart('D2', chart1)
    
    
# Line Chart:

def line(workbook, labels, series1, *others, subtype='', headings=["Series","values"], sheetname="Sheet"):
    worksheet = workbook.add_worksheet(sheetname)
    length = len(labels)
    sheet_name = worksheet.get_name()
    
    chart1 = workbook.add_chart({'type': 'line', 'subtype': subtype})
    worksheet.write_row('A1', headings, bold)
    worksheet.write_column("A2", labels)
    
    worksheet.write_column("B2", series1)
    chart1.add_series({
        'name':       [sheet_name, 0, 1], 
        'categories': [sheet_name, 1, 0,length,0], # '=%s!$A$2:$A$%s' % (sheet_name, length),
        'values':     [sheet_name, 1, 1,length,1], #'=%s!$B$2:$B$%s' % (sheet_name, length),
        'data_labels': {'value': True}
    })
    
    for idx, val in enumerate(others):
        cell = xl_rowcol_to_cell(1,idx+2)
        worksheet.write_column(cell, val)
        chart1.add_series({
            'name':       [sheet_name, 0, idx+2], 
            'categories': [sheet_name, 1, 0,length,0], # '=%s!$A$2:$A$%s' % (sheet_name, length),
            'values':     [sheet_name, 1, idx+2,length,idx+2], #'=%s!$B$2:$B$%s' % (sheet_name, length),
            'data_labels': {'value': True}
        })
        
    worksheet.insert_chart('D2', chart1)



# basic connection
conn = psycopg2.connect("host=10.10.10.240 user=dsviewer password=dsview933 dbname=ds")




# subregional keys
conn2 = psycopg2.connect("host=db.dev.mapc.org user=editor password=M999PCedit.451 dbname=datasets")
sql = "SELECT * FROM public.mapc_subregions"
subregions = read_sql(sql, conn2, coerce_float=True, params=None)
SUBREGION = subregions[subregions['MUNI_ID']==MUNI_ID]["Subregion"].tolist()[0]

# we select munis if they partially match because of many-to-many relations
SUBREGIONAL_MUNIS = subregions[subregions["Subregion"].str.contains(SUBREGION)]

# other data keys
sql = "SELECT * FROM tabular._datakeys_muni351 WHERE muni_id = %s" % MUNI_ID
crosswalk = read_sql(sql, conn, coerce_float=True, params=None)
COUNTY = crosswalk[crosswalk['muni_id']==MUNI_ID]["county"].tolist()[0]
MUNI_NAME = crosswalk[crosswalk["muni_id"] == MUNI_ID]["municipal"].tolist()[0]



# workbook = Workbook.new(name: 'filename.xlsx')
# charts = load chart file
# charts.each { |chart| chart.generate }


# create workbook
workbook_name = 'output/%s-Charts.xlsx' % (MUNI_NAME)
writer = pd.ExcelWriter(workbook_name, engine='xlsxwriter')
workbook = writer.book
bold = workbook.add_format({'bold': 1})

municipalities = ""
# # Line Graphs
failures = []
for chart in chart_pairings:
    log = "Generating " + chart + "... "
    try: 
        exec(chart_pairings[chart])
        log += "Success ✓"
    except: 
        failures.append(chart)
        log += "Failure"
    print(log)

if (len(failures) > 0):
    print("The following charts failed to generate:")

    for failure in failures:
        print(failure)

workbook.close()










## TODO:


# Average Household Size - missing data from database
# data = pd.read_csv('http://www.housing.ma/gloucester/profile.csv', skiprows=2)
# data
# worksheet = workbook.add_worksheet()
# bold = workbook.add_format({'bold': 1})
# # Add the worksheet data that the charts will refer to.
# headings = ['Age', '1990', '2000', '2010', '2020', '2030', 'Change 2010-2030', '% Change 2010-2030']






# Race, % change
# THIS TABLE DOESN"T WORK FOR SOME REASON
# sql = "SELECT * FROM tabular.b03002_race_ethnicity_acs_m WHERE muni_id = %s AND acs_year IN ('2005-09','2010-14')" % MUNI_ID
# meta_sql = "SELECT * FROM metadata.b03002_race_ethnicity_acs_m"

# df = read_sql(sql, conn, coerce_float=True, params=None)
# meta = read_sql(meta_sql,conn,coerce_float=True, params=None)

# # Add the worksheet data that the charts will refer to. Since metadata values don't map to field names
# # they can't be used.
# headings = [ '2009', '2014', 'Change 2009-2014', '% Change 2009-2014']
# categories = ['nhwhi','nhaa','nhnana','nhas','nhpi','nhoth','nhmlt','lat']
# categories_pretty = meta[meta["name"].isin(categories)]["alias"].tolist()

# df = df[categories].transpose()
# df['change'] = df[1] - df[0]
# df['change_p'] = ((df[1] - df[0]) / df[0]) * 100
# df.to_excel(writer, "RacePercentChange", index_label='Race', header=headings)







# Percentage of Families with Incomes below the Poverty Level










# Households by Type, with Children




# Income as Percent of AMI by Household Type/Size




# Cost Burden by Household Type, All Households
# Data not yet in the data browser




# Cost Burden by Household Type, Low-Income Households




# Cost Burden by Household Type, Income




# Housing Problems for Salem Households at 80-120% of AMI




# Foreclosure Petitions, Auctions, and Deeds Issued, Subregion


# # Bar Charts














# Housing Tenure by Age of Householder
# Missing from Data Browser
# sql = "SELECT * FROM tabular.b25072_b25093_costburden_by_age_acs_m WHERE acs_year = '2010-14' AND muni_id = '%s'" % MUNI_ID
# df = read_sql(sql, conn, coerce_float=True, params=None)
# # incomes = df[cols].transpose().sort_values(by=[0])[0].tolist()
# cols = ['o1524','o2534','o3564','o65ovr','r1524','r2534','r3564','r65ovr']
# # column(workbook, cols, incomes, type='bar')
# df[cols]
















#this must be run last



