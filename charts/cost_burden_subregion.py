# Cost Burden, Subregion
sql = "SELECT * FROM tabular.b25091_b25070_costburden_acs_m WHERE acs_year = '2010-14'"
dataset = DataGrid(batch, sql, [])
chart = Chart(batch,dataset,"CostBurdenSubregion")

def munging(self):
  cols = ['municipal', 'cb_p']
  headings = ['Municipality', 'Cost Burden Households, Percent']
  df = self.data()
  self.munged = df.sort_values(by="cb_p", ascending=False)[df['muni_id'].isin(self.subregional_munis["MUNI_ID"])][cols]
  self.munged.columns = headings

dataset.munge(munging)
chart.generate(type="column")

chart.chart.set_title({
  'name': 'Cost Burden, %s' % dataset.subregion
})
