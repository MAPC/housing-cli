
# Stacked, Percent family, non-family, subregional municipalities
sql = "SELECT * FROM mapc.hous_hh_fam_00_10m WHERE years = '2010'"

df = read_sql(sql, conn, coerce_float=True, params=None)
df = df[df["muni_id"].isin(SUBREGIONAL_MUNIS["MUNI_ID"])].sort_values(by=["hhf_p"], ascending=False)
headings = ['Municipality', 'Family', 'Non-Family']
print(df)
column(workbook,df["municipal"],df["hhf"],df["hhnf"], subtype="percent_stacked", headings=headings, sheetname="HouseholdsByFamType")
