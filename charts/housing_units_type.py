# Housing Units by Type
sql = "SELECT * FROM tabular.b25024_hu_units_in_structure_acs_m WHERE acs_year = '2010-14'"
dataset = DataGrid(batch, sql, [])
chart = Chart(batch,dataset,"HousingUnitsByTypeSubregion")

def munging(self):
  df = self.data()
  cols = ['municipal', 'u1','u2','u3_4','u5_9','u10_19','u20_49','u50ov','u_oth']
  headings = ['Municipality', 'Single Family', 'Two-Family', '3-4 Units', '5-9 Units', '10-19 Units', '20-49 Units', '50+ Units', 'Other']
  df = df[df['muni_id'].isin(self.subregional_munis["MUNI_ID"])]
  self.munged = df[cols]
  self.munged.columns = headings
  


dataset.munge(munging)
chart.generate(type="column", subtype="percent_stacked")
