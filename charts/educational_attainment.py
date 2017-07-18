# Educational Attainment
sql = "SELECT * FROM tabular.b15002_educational_attainment_acs_m WHERE acs_year = '2011-15'"
dataset = DataGrid(batch, sql, [])

def munging(self):
  cols = ['municipal', 'lths_p','hs_p','sc_p','assoc_p','bapl_p']
  df = self.data()
  headings = ["Geography", "% Less than High School", "% High School Diploma", "% Some College", "% Associates Degree", "% Bachelor's or More"]
  self.munged = df[cols][(df["muni_id"] == self.Batch.muni_id) | (df["municipal"] == "Massachusetts") | (df["municipal"] == self.county)]
  self.munged.columns = headings

dataset.munge(munging)
dataset.project("educational_attainment")
