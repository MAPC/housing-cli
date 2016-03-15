

# Housing Units by Type
sql = "SELECT * FROM tabular.b25024_hu_units_in_structure_acs_m WHERE acs_year = '2010-14'"
cols = ['u1','u2','u3_4','u5_9','u10_19','u20_49','u50ov','u_oth']
headings = ['Municipality', 'Single Family', 'Two-Family', '3-4 Units', '5-9 Units', '10-19 Units', '20-49 Units', '50+ Units', 'Other']
df = read_sql(sql, conn, coerce_float=True, params=None)
df = df[df['muni_id'].isin(SUBREGIONAL_MUNIS["MUNI_ID"])]
muncipalities = df['municipal']
transpose_df = df[cols].transpose()
column(workbook, df['municipal'], 
       transpose_df.loc['u1'].tolist(),
       transpose_df.loc['u2'].tolist(), 
       transpose_df.loc['u3_4'].tolist(),
       transpose_df.loc['u5_9'].tolist(),
       transpose_df.loc['u10_19'].tolist(),
       transpose_df.loc['u20_49'].tolist(),
       transpose_df.loc['u50ov'].tolist(),
       transpose_df.loc['u_oth'].tolist(), subtype='percent_stacked', headings=headings,  sheetname="HousingUnitsByTypeSubregion")

