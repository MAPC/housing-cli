# Foreclosure Deeds Issued, Subregion
sql = "SELECT * FROM tabular.hous_foreclosures_m WHERE cal_year='2012'"
dataset = DataGrid(batch, sql, [])
chart = Chart(batch,dataset,"ForeclosureDeedsSubregion")

def munging(self):
  df = self.data()
  headings = ['Municipality', 'Foreclosure Deeds']
  cols = ['municipal', 'deeds']
  self.munged = df[cols].sort_values(by="deeds", ascending=False)[df['muni_id']\
  .isin(self.subregional_munis["MUNI_ID"])]
  self.munged.columns = headings

dataset.munge(munging)
chart.generate(type="column")

chart.chart.set_title({
  'name': 'Foreclosure Deeds in %s' % dataset.subregion
})
