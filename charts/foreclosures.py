
# Foreclosures
sql = "SELECT * FROM tabular.hous_foreclosures_m WHERE muni_id=%s" % MUNI_ID
df = read_sql(sql, conn, coerce_float=True, params=None)

# status_quo = df[['hh_10', 'hh_20_sq', 'hh_30_sq']].values.tolist()[0]
# stronger_region = df[['hh_10', 'hh_20_sr', 'hh_30_sr']].values.tolist()[0]

# Add the worksheet data that the charts will refer to.
headings = ['Year', 'Foreclosures']
line(workbook, df['cal_year'], df['deeds'], headings=headings, sheetname="Foreclosures")
