# Population Projections
# worksheet = workbook.add_worksheet()
sql = "SELECT * FROM tabular.demo_projections_pop_m WHERE muni_id=%s" % MUNI_ID
df = read_sql(sql, conn, coerce_float=True, params=None)
status_quo = df[['pop_00','pop_10', 'pop_20sq', 'pop_30sq']].values.tolist()[0]
stronger_region = df[['pop_00','pop_10', 'pop_20sr', 'pop_30sr']].values.tolist()[0]
years = [2000,2010,2020,2030]
headings = ['Year', 'Status Quo', 'Stronger Region']

line(workbook, years, status_quo, stronger_region, headings=headings,sheetname="PopulationProjections")
