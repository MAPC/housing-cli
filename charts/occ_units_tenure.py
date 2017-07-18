# Occupied Units by Tenure, Subregion
sql = "SELECT * FROM tabular.b25032_hu_tenure_by_units_acs_m WHERE acs_year = '2011-15'"
dataset = DataGrid(batch, sql, [])
chart = Chart(batch,dataset,"TenureSubregion")

def munging(self):
  df = self.data()
  cols = ['municipal', 'o_hu','r_hu']
  headings = ['Municipality', 'Ownered-Occupied Housing Units', 'Renter-Occupied Housing Units']
  df = df[df['muni_id'].isin(self.subregional_munis["MUNI_ID"])].sort_values(by="o_hu_p", ascending=False)
  self.munged = df[cols]
  self.munged.columns = headings

dataset.munge(munging)
chart.generate(type="column", subtype="percent_stacked")

chart.chart.set_title({
  'name': 'Occupied Units by Tenure, %s' % dataset.subregion
})
