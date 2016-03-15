# Population by Age
sql = "SELECT * FROM tabular.demo_projections_pop_by_age_m WHERE muni_id=%s" % MUNI_ID
df = read_sql(sql, conn, coerce_float=True, params=None)

# Add the worksheet data that the charts will refer to.
headings = ['Age', '1990', '2000', '2010', '2020', '2030', 'Change 2010-2030', '% Change 2010-2030']
df["change"] = df['pop_30sr'] - df['pop_10']
df["change_p"] = ((df['pop_30sr'] - df['pop_10']) / df['pop_10']) * 100

df[['age_group','pop_90','pop_00','pop_10','pop_20sr','pop_30sr','change','change_p']].to_excel(writer, "Population by Age",  header=headings)
