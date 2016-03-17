
# Foreclosures
sql = "SELECT * FROM tabular.hous_foreclosures_m WHERE muni_id=%s" % batch.muni_id
dataset = generate.DataGrid(batch, sql, [])
chart = generate.Chart(batch,dataset,"Foreclosures")

def munging(self):
  df = self.data()
  headings = ['Year', 'Foreclosures']
  self.munged = df[["cal_year", "deeds"]]

dataset.munge(munging)
chart.generate(type="line")
