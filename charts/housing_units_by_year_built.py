

# Housing Units by Year Built
sql = "SELECT * FROM tabular.b25127_hu_tenure_year_built_units_acs_m WHERE acs_year = '2010-14'"
cols = ['h_00','h8099','h6079','h4059','h_39']
headings = ['Municipality', '2000 or after', '1980-99', '1960-1979', '1940-59', 'Under 1939']
df = read_sql(sql, conn, coerce_float=True, params=None)
df = df[df['muni_id'].isin(SUBREGIONAL_MUNIS["MUNI_ID"])]
muncipalities = df['municipal']
transpose_df = df[cols].transpose()
column(workbook, df['municipal'], 
       transpose_df.loc['h_00'].tolist(),
       transpose_df.loc['h8099'].tolist(), 
       transpose_df.loc['h6079'].tolist(),
       transpose_df.loc['h4059'].tolist(),
       transpose_df.loc['h_39'].tolist(), subtype='percent_stacked', headings=headings, sheetname="YearBuilt")

