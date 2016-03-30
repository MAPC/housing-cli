# Population Projections
# worksheet = workbook.add_worksheet()
# sql = "SELECT * FROM tabular.demo_projections_pop_m WHERE muni_id=%s" % MUNI_ID
# df = read_sql(sql, conn, coerce_float=True, params=None)
# status_quo = df[['pop_00','pop_10', 'pop_20sq', 'pop_30sq']].values.tolist()[0]
# stronger_region = df[['pop_00','pop_10', 'pop_20sr', 'pop_30sr']].values.tolist()[0]
# years = [2000,2010,2020,2030]
# headings = ['Year', 'Status Quo', 'Stronger Region']

# line(workbook, years, status_quo, stronger_region, headings=headings,sheetname="PopulationProjections")


# Population Projections
sql = "SELECT * FROM tabular.demo_projections_pop_m WHERE muni_id=%s" % batch.muni_id
dataset = DataGrid(batch, sql, [])
chart = Chart(batch,dataset,"PopulationProjections")

def munging(self):
  df = self.data()
  years = [2000,2010,2020,2030]

  status_quo = df[['pop_00','pop_10', 'pop_20sq', 'pop_30sq']].transpose()
  status_quo.columns = ["Status Quo"]
  status_quo.index = years

  stronger_region = df[['pop_00','pop_10', 'pop_20sr', 'pop_30sr']].transpose()
  stronger_region.columns = ["Stronger Region"]
  stronger_region.index = years

  headings = ['Year', 'Status Quo', 'Stronger Region']

  status_quo.insert(1, "Stronger Region", stronger_region["Stronger Region"])
  status_quo.insert(0, "Year", status_quo.index)
  self.munged = status_quo

dataset.munge(munging)
chart.generate(type="line")
