

# Occupied Units by Tenure, Subregion
sql = "SELECT * FROM tabular.b25032_hu_tenure_by_units_acs_m WHERE acs_year = '2010-14'"
cols = ['o_hu','r_hu']
headings = ['Municipality', 'Ownered-Occupied Housing Units', 'Renter-Occupied Housing Units']
df = read_sql(sql, conn, coerce_float=True, params=None)
df = df[df['muni_id'].isin(SUBREGIONAL_MUNIS["MUNI_ID"])]
muncipalities = df['municipal']
transpose_df = df[cols].transpose()
column(workbook, df['municipal'], 
       transpose_df.loc['o_hu'].tolist(),
       transpose_df.loc['r_hu'].tolist(), subtype='percent_stacked', headings=headings, sheetname="TenureSubregion")


