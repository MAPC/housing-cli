
# Foreclosures
sql = "SELECT * FROM tabular.hous_foreclosures_m WHERE muni_id=%s" % batch.muni_id
dataset = DataGrid(batch, sql, [])
chart = Chart(batch,dataset,"Foreclosures")

def munging(self):
  df = self.data()
  headings = ['Year', 'Foreclosures']
  self.munged = df[["cal_year", "deeds"]]
  self.munged.columns = headings

dataset.munge(munging)
chart.generate(type="line")
