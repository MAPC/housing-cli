
# Housing Units by Type
sql = "SELECT * FROM tabular.b25024_hu_units_in_structure_acs_m WHERE muni_id = %s AND acs_year IN ('2010-14')" % MUNI_ID
cols = ['u1','u2','u3_4','u5_9','u10_19','u20_49','u50ov','u_oth']
df = read_sql(sql, conn, coerce_float=True, params=None)
transpose_df = df[cols].transpose()
transpose_df['pct'] = (transpose_df[0] / df['hu'][0]) * 100
transpose_df.to_excel(writer, "HousingByType",index_label="Type", header=["Housing Units", "Percent"])
