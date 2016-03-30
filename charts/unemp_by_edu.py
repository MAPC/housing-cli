# Percentage of Families with Incomes below the Poverty Level, Subregion
sql = "SELECT * FROM tabular.b23006_educational_attainment_by_laborforce_acs_m WHERE acs_year = '2010-14' AND muni_id = %s" % batch.muni_id
dataset = DataGrid(batch, sql, [])
chart = Chart(batch,dataset,"EducationAttainByLabor")

def munging(self):
  df = self.data()
  cols = ["lhs_ue_p", "hs_ue_p", "sc_ue_p", "bap_ue_p"]
  self.munged = df[cols].transpose()
  self.munged.columns = ["% Unemployed"]
  categories = ["Less than High School", "High School Graduate",  "with Some College Education",  "with Bachelors degree or higher"]
  self.munged.insert(0,"Educational Attainment", categories)

dataset.munge(munging)
chart.generate(type="column")
