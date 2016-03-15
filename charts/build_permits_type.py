


# Building Permits by Type
sql = "SELECT * FROM tabular.hous_building_permits_m WHERE bp_year = '2013'"
cols = ['sf_units', 'mf_units']
headings = ['Municipality', 'Single-Family Permits', 'Multi-Family Permits']
df = read_sql(sql, conn, coerce_float=True, params=None).sort_values(by="tot_units", ascending=False)
df = df[df['muni_id'].isin(SUBREGIONAL_MUNIS["MUNI_ID"])]

muncipalities = df['municipal']
column(workbook, df['municipal'], df["sf_units"], df["mf_units"], subtype="stacked", headings=headings, sheetname="BuildingPermits")

