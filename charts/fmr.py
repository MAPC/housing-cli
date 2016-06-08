# Average Household Size by Tenure
sql = "SELECT * FROM tabular.hous_fair_market_rent_by_year_m WHERE muni_id = %s" % batch.muni_id
dataset = DataGrid(batch, sql, [])
chart = Chart(batch,dataset,"FairMarkRents")

def munging(self):
  df = self.data()[self.data()["fy_year"] > 2010 ]

  self.munged=df[['fmrnt_0br', 'fmrnt_1br', 'fmrnt_2br', 'fmrnt_3br', 'fmrnt_4pbr']]
  self.munged.index = df["fy_year"]
  self.munged = self.munged.transpose()
  self.munged.index = ["Efficiency", "1 Bedroom", "2 Bedrooms", "3 Bedrooms", "4 Bedrooms"]
  self.munged.insert(0, "Bedrooms", self.munged.index)
  


dataset.munge(munging)
chart.generate(type="column")

chart.chart.set_title({
  'name': 'Fair Market Rents'
})
