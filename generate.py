import sys
import traceback
import glob
import pandas as pd
from pandas.io import sql
from pandas.io.sql import read_sql
from charts import Workbook, Batch, DataGrid, Chart


def camelize(file):
   first, *rest = file.split('_')
   return first + ''.join(word.capitalize() for word in rest)

def main():
  print("Running")
  muni_id = int(sys.argv[1])
  workbook = Workbook()
  batch = Batch(workbook, muni_id)
  charts = glob.glob("./charts/*.py")
  chart_pairings = dict()
  for chart in charts: 
      chart_pairings[camelize(chart.replace("./charts/", "").replace(".py",""))] = open(chart).read()

  failures = []
  for chart in chart_pairings:
      log = "Generating " + chart + "... "
      try: 
          exec(chart_pairings[chart])
          log += "Success ✓"
      except: 
          failures.append(chart)
          log += "Failure"
          traceback.print_exc()
      print(log)

  if (len(failures) > 0):
      print("The following charts failed to generate:")

      for failure in failures:
          print(failure)

  workbook.close()

main()
