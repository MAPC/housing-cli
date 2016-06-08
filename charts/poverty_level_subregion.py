

# Percentage of Families with Incomes below the Poverty Level, Subregion
# sql = "SELECT * FROM tabular.b17017_poverty_by_hh_type_acs_m WHERE acs_year = '2010-14'"
# df = read_sql(sql, conn, coerce_float=True, params=None)
# # df["non_white"] = df["totpop"] - df["nhwhi"]
# # df["p_nw"] = (df["non_white"] / df["totpop"]) * 100
# subregion_munis = df[df["muni_id"].isin(SUBREGIONAL_MUNIS["MUNI_ID"])].sort_values(by=['pov_f_p'], ascending=False)

# column(workbook, subregion_munis["municipal"], subregion_munis["pov_f_p"], headings=["Municipalities","% Families in Poverty"],  sheetname="PovertySubregion")

# Percentage of Families with Incomes below the Poverty Level, Subregion
sql = "SELECT * FROM tabular.b17017_poverty_by_hh_type_acs_m WHERE acs_year = '2010-14'"
dataset = DataGrid(batch, sql, [])
chart = Chart(batch,dataset,"PovertySubregion")

def munging(self):
  df = self.data()
  self.munged = df[df["muni_id"].isin(self.subregional_munis["MUNI_ID"])].sort_values(by=['pov_f_p'], ascending=False)[['municipal', 'pov_f_p']]
  self.munged.columns =["Municipalities","% Families in Poverty"]

dataset.munge(munging)
chart.generate(type="column")

chart.chart.set_title({
  'name': 'Percentage of Families in Poverty, %s' % dataset.subregion
})
