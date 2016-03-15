
# Educational Attainment
sql = "SELECT * FROM tabular.b15002_educational_attainment_acs_m WHERE acs_year = '2010-14'"
cols = ['municipal', 'lths_p','hs_p','sc_p','assoc_p','bapl_p']
df = read_sql(sql, conn, coerce_float=True, params=None)
df = df[(df["muni_id"] == MUNI_ID) | (df["municipal"] == "Massachusetts") | (df["municipal"] == COUNTY)]
df[cols].to_excel(writer, "EduAttainment", header=["Geography", "% Less than High School", "% High School Diploma", "% Some College", "% Associates Degree", "% Bachelor's or More"])
