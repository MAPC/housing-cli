# Median Gross Rent
# sql = "SELECT * FROM tabular.b25063_b25064_b25065_rent_acs_m WHERE acs_year = '2010-14'"
# cols = ['med_c_r']
# headings = ['Municipality', 'Median Gross Renter']
# df = read_sql(sql, conn, coerce_float=True, params=None).sort_values(by="med_c_r", ascending=False)
# df = df[df['muni_id'].isin(SUBREGIONAL_MUNIS["MUNI_ID"])]
# muncipalities = df['municipal']
# column(workbook, df['municipal'], df["med_c_r"], headings=headings, sheetname="MedianGrossRent")

# Median Gross Rent
sql = "SELECT * FROM tabular.b25063_b25064_b25065_rent_acs_m WHERE acs_year = '2010-14'"
dataset = DataGrid(batch, sql, [])
chart = Chart(batch,dataset,"MedianGrossRent")

def munging(self):
  df = self.data()
  cols = ['municipal', 'med_c_r']
  headings = ['Municipality', 'Median Gross Renter']
  df = df[df['muni_id'].isin(self.subregional_munis["MUNI_ID"])].sort_values(by="med_c_r", ascending=False)
  self.munged = df[cols]
  self.munged.columns = headings

dataset.munge(munging)
chart.generate(type="column")
