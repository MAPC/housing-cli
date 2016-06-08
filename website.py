from flask import Flask
from flask import render_template, request, send_file
from charts import DataGrid, Workbook, Batch, Chart
import psycopg2
import pandas as pd
from pandas.io.sql import read_sql

app = Flask(__name__)

@app.route("/")
def index():
  conn2 = psycopg2.connect("host=db.dev.mapc.org user=editor password=M999PCedit.451 dbname=datasets")
  munis = read_sql("SELECT * FROM public._datakeys_muni351", conn2, coerce_float=True, params=None)
  munis_list = munis[munis["mapc"] == 1][["muni_id", "municipal"]].to_dict(orient="records")
  
  return render_template('munis.html', municipalities=munis_list)

@app.route('/municipalities/<muni_id>')
def generate():
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

  output = StringIO.StringIO()
  output.seek(0)

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
