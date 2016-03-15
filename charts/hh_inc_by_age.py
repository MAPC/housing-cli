

# Household Income by Age of Householder
sql = "SELECT * FROM tabular.b19037_hh_income_by_age_acs_m WHERE acs_year = '2010-14' AND muni_id = '%s'" % MUNI_ID
df = read_sql(sql, conn, coerce_float=True, params=None)
cols = ['iu25u20','iu252039','iu254059','iu256074','iu257599','iu25100o','i25u20','i252039','i254059','i256074','i257599','i25100o','i45u20','i452039','i454059','i456074','i457599','i45100o','i65u20','i652039','i654059','i656074','i657599','i65100o']
labels = ['Incomes', 'Under 25', '25-44 years', '45-64 years', '65+ years']
incomes = ['Income under $20,000','Income $20,000-$39,999','Income $40,000-$59,999','Income $60,000-$74,999','Income $75,000-$99,999','Income $100,000 or more']

years1 = df[['iu25u20','iu252039','iu254059','iu256074','iu257599','iu25100o']].transpose()[0].tolist()
years2 = df[['i25u20','i252039','i254059','i256074','i257599','i25100o']].transpose()[0].tolist()
years3 = df[['i45u20','i452039','i454059','i456074','i457599','i45100o']].transpose()[0].tolist()
years4 = df[['i65u20','i652039','i654059','i656074','i657599','i65100o']].transpose()[0].tolist()

column(workbook, incomes, years1, years2, years3, years4, subtype='percent_stacked', headings=labels,  sheetname="IncomeByAge")

