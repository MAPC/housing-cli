# Foreclosure Deeds Issued, Subregion
sql = "SELECT * FROM tabular.hous_foreclosures_m WHERE cal_year='2012'"
dataset = generate.DataGrid(batch, sql, [])
chart = generate.Chart(batch,dataset,"ForeclosureDeedsSubregion")

def munging(self):
  df = self.data()
  headings = ['Municipality', 'Foreclosure Deeds']
  cols = ['municipal', 'deeds']
  self.munged = df[cols].sort_values(by="deeds", ascending=False)[df['muni_id']\
  .isin(self.subregional_munis["MUNI_ID"])]

dataset.munge(munging)
chart.generate(type="column")
