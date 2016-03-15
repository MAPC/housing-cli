
# Housing Demand by Tenure, Stronger Region
sql = "SELECT * FROM mapc.hous_projections_hu_demand_by_age_m WHERE muni_id = '%s'" % MUNI_ID

df = read_sql(sql, conn, coerce_float=True, params=None)

pivoted = df.pivot('age_group','typetenure', 'hu10_20sr').reset_index()

# cols = ['h_00','h8099','h6079','h4059','h_39']
headings = ['Age Group', 'Multifamily-Own', 'Multifamily-Rent', 'Single Family-Own', 'Single Family-Rent']
# df = df[df['muni_id'].isin(SUBREGIONAL_MUNIS["MUNI_ID"])]
labels = pivoted['age_group']
# transpose_df = df[cols].transpose()
column(workbook, labels, 
       pivoted['Multifamily-Own'],
       pivoted['Multifamily-Rent'], 
       pivoted['Single Family-Own'],
       pivoted['Single Family-Rent'], subtype='stacked', headings=headings, sheetname="HousingDemandStrongeRegion")

