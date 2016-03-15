# Household Projections
sql = "SELECT * FROM tabular.hous_projections_hh_m WHERE muni_id=%s" % MUNI_ID
df = read_sql(sql, conn, coerce_float=True, params=None)

status_quo = df[['hh_10', 'hh_20_sq', 'hh_30_sq']].values.tolist()[0]
stronger_region = df[['hh_10', 'hh_20_sr', 'hh_30_sr']].values.tolist()[0]

# Add the worksheet data that the charts will refer to.
headings = ['Year', 'Status Quo', 'Stronger Region']
years = [2010, 2020, 2030]
line(workbook, years, status_quo, stronger_region, headings=headings, sheetname="HouseholdProjections")
