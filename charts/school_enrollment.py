
# School Enrollment 
# sql = "SELECT * FROM tabular.educ_enrollment_by_year_m WHERE muni_id = %s" % MUNI_ID

# df = read_sql(sql, conn, coerce_float=True, params=None)
# # transpose_df = df[cols].transpose()
# # transpose_df['pct'] = (transpose_df[0] / df['hu'][0]) * 100
# # transpose_df.to_excel(writer, "Sheet%s" % str(workbook.sheetname_count + 1),index_label="Type", header=["Housing Units", "Percent"])
# df["minority_p"] = (df['enrolled'] - df['whi_num']) / df['enrolled']
# df['diff'] = (df['enrolled'].diff()/df['enrolled'].shift(1)) * 100
# cols = ['schoolyear','enrolled','diff','minority_p','ell_pct','lep_pct','li_pct']
# df[cols].to_excel(writer, "Enrollment", header=["School Year", "Enrolled", "% Change from previous", "% Minority", "% English Language Learner", "% Limited English Proficiency", "% Low-Income"])

# School Enrollment 
sql = "SELECT * FROM tabular.educ_enrollment_by_year_m WHERE muni_id = %s" % batch.muni_id
dataset = DataGrid(batch, sql, [])

def munging(self):
  df = self.data()

  df["minority_p"] = (df['enrolled'] - df['whi_num']) / df['enrolled']
  df['diff'] = (df['enrolled'].diff()/df['enrolled'].shift(1)) * 100
  cols = ['schoolyear','enrolled','diff','minority_p','ell_pct','lep_pct','li_pct']
  self.munged = df[cols]
  self.munged.columns = ["School Year", "Enrolled", "% Change from previous", "% Minority", "% English Language Learner", "% Limited English Proficiency", "% Low-Income"]

dataset.munge(munging)
dataset.project("School Enrollment")
