

# # Households by Age of Householder
# sql = "SELECT * FROM tabular.hous_projections_hh_by_age_m WHERE muni_id = %s" % MUNI_ID

# df = read_sql(sql, conn, coerce_float=True, params=None)

# # # Add the worksheet data that the charts will refer to.
# headings = ['Age of Householder', '2010', '2020', '2030', 'Change 2010-2030', '% Change 2010-2030']
# cols = ['age_group','hhest_10','hh_20_sr','hh_30_sr','change','change_p']
# df["change"] = df['hh_30_sr'] - df['hhest_10']
# df["change_p"] = ((df['hh_30_sr'] - df['hhest_10']) / df['hhest_10']) * 100
# df[cols].to_excel(writer, "HouseholdsByAge", header=headings)

# Households by Age of Householder
sql = "SELECT * FROM tabular.hous_projections_hh_by_age_m WHERE muni_id = %s" % batch.muni_id
dataset = DataGrid(batch, sql, [])

def munging(self):
  df = self.data()
  headings = ['Age of Householder', '2010', '2020', '2030', 'Change 2010-2030', '% Change 2010-2030']
  cols = ['age_group','hhest_10','hh_20_sr','hh_30_sr','change','change_p']
  df["change"] = df['hh_30_sr'] - df['hhest_10']
  df["change_p"] = ((df['hh_30_sr'] - df['hhest_10']) / df['hhest_10']) * 100
  self.munged = df[cols]
  self.munged.columns = headings

dataset.munge(munging)
dataset.project("HouseholdsByAge")
