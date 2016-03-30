# Population by Age
sql = "SELECT * FROM tabular.demo_projections_pop_by_age_m WHERE muni_id=%s" % batch.muni_id
dataset = DataGrid(batch, sql, [])

def munging(self):
  df = self.data()

  headings = ['Age', '1990', '2000', '2010', '2020', '2030', 'Change 2010-2030', '% Change 2010-2030']
  df["change"] = df['pop_30sr'] - df['pop_10']
  df["change_p"] = ((df['pop_30sr'] - df['pop_10']) / df['pop_10']) * 100
  self.munged = df[['age_group','pop_90','pop_00','pop_10','pop_20sr','pop_30sr','change','change_p']]
  self.munged.columns = headings

dataset.munge(munging)
dataset.project("Population by Age")
