
# Stacked, Percent family, non-family, subregional municipalities
sql = "SELECT * FROM mapc.hous_hh_fam_00_10m WHERE years = '2010'"
dataset = generate.DataGrid(batch, sql, [])
chart = generate.Chart(batch,dataset,"HouseholdsByFamType")

def munging(self):
  df = self.data()
  cols = ["municipal", "hhf", "hhnf"]
  self.munged = df[df["muni_id"].isin(self.subregional_munis["MUNI_ID"])].sort_values(by=["hhf_p"], ascending=False)[cols]
  self.munged.columns = ['Municipality', 'Family', 'Non-Family']

dataset.munge(munging)
chart.generate(type="column", subtype="percent_stacked")

# df = read_sql(sql, conn, coerce_float=True, params=None)
# df = df[df["muni_id"].isin(SUBREGIONAL_MUNIS["MUNI_ID"])].sort_values(by=["hhf_p"], ascending=False)
# headings = ['Municipality', 'Family', 'Non-Family']
# column(workbook,df["municipal"],df["hhf"],df["hhnf"], subtype="percent_stacked", headings=headings, sheetname="HouseholdsByFamType")
