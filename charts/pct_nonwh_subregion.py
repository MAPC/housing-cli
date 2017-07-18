
# Percent Non-White, Subregion
# sql = "SELECT * FROM tabular.b03002_race_ethnicity_acs_m WHERE acs_year = '2005-09'"
# df = read_sql(sql, conn, coerce_float=True, params=None)
# df["non_white"] = df["totpop"] - df["nhwhi"]
# df["p_nw"] = (df["non_white"] / df["totpop"]) * 100
# subregion_munis = df[df["muni_id"].isin(SUBREGIONAL_MUNIS["MUNI_ID"])].sort_values(by=['p_nw'], ascending=False)

# column(workbook, subregion_munis["municipal"], subregion_munis["p_nw"], headings=["Municipalities","% Non-White"],  sheetname="PercentNonWhiteSubregion")


# Percent Non-White, Subregion
sql = "SELECT * FROM tabular.b03002_race_ethnicity_acs_m WHERE acs_year = '2011-15'"
dataset = DataGrid(batch, sql, [])
chart = Chart(batch,dataset,"PercentNonWhiteSubregion")

def munging(self):
  df = self.data()
  df["non_white"] = df["totpop"] - df["nhwhi"]
  df["p_nw"] = (df["non_white"] / df["totpop"]) * 100
  subregion_munis = df[df["muni_id"].isin(self.subregional_munis["MUNI_ID"])].sort_values(by=['p_nw'], ascending=False)
  self.munged = subregion_munis[["municipal", "p_nw"]]
  self.munged.columns = ["Municipalities","% Non-White"]

dataset.munge(munging)
chart.generate(type="column")

chart.chart.set_title({
  'name': 'Percent Non-White, %s' % dataset.subregion
})
