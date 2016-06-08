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
  # cols = ['pop_00','pop_10', 'pop_20sq', 'pop_30sq', 'pop_20sr', 'pop_30sr']
  # df = df[cols]
  # transposed = df[cols].transpose()
  
  # transposed.insert(1,"Year", [2000,2010,2020,2030,2020,2030])
  # transposed.insert(2, "Type", ["Census", "Census", "Status Quo", "Status Quo", "Stronger Region", "Stronger Region"])
  # transposed.columns = ["Population", "Year", "Type"]
  # transposed.append( transposed[transposed["Year"]==2010]["Type"] = "Status Quo", ignore_index=True )

  # self.munged = pd.pivot_table(transposed, values=["Population"], index=["Year"], columns=["Type"])["Population"]
  # self.munged.insert(0, "Year", self.munged.index)

dataset.munge(munging)
chart.generate(type="line")

chart.chart.set_title({
  'name': 'Population Projections'
})
