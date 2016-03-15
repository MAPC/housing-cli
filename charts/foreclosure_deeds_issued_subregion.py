
# Foreclosure Deeds Issued, Subregion
sql = "SELECT * FROM tabular.hous_foreclosures_m WHERE cal_year='2012'"
cols = ['deeds']
headings = ['Municipality', 'Foreclosure Deeds']
df = read_sql(sql, conn, coerce_float=True, params=None).sort_values(by="deeds", ascending=False)
df = df[df['muni_id'].isin(SUBREGIONAL_MUNIS["MUNI_ID"])]
column(workbook, df['municipal'], df["deeds"], headings=headings, sheetname="ForeclosureDeedsSubregion")

