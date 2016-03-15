# Cost Burden, Subregion
sql = "SELECT * FROM tabular.b25091_b25070_costburden_acs_m WHERE acs_year = '2010-14'"
cols = ['cb_p']
headings = ['Municipality', 'Cost Burden Households, Percent']
df = read_sql(sql, conn, coerce_float=True, params=None).sort_values(by="cb_p", ascending=False)
df = df[df['muni_id'].isin(SUBREGIONAL_MUNIS["MUNI_ID"])]
column(workbook, df['municipal'], df["cb_p"], headings=headings, sheetname="CostBurden")


# def transpose(data, opts):
#   # 


# Chart.new(
#   table: b25091_b25070_costburden_acs_m,
#   condition: 'acs_year = ...',
#   workbook: workbook
#   munge: transpose()
# ).generate
