Average Household Size by Tenure
sql = "SELECT * FROM tabular.b25002_b25003_hu_occupancy_by_tenure_race_acs_m WHERE muni_id = %s" % batch.muni_id
dataset = DataGrid(batch, sql, [])

def munging(self):
  cols = ["B25004_001E",\
          "B25004_002E",\
          "B25004_003E",\
          "B25004_004E",\
          "B25004_005E",\
          "B25004_008E"]

  muni = self.census_api.acs.state_county_subdivision(cols, 25, self.county_fips, self.cousub_fips)
  region = self.census_api.acs.state_county_subdivision(("B01001_001E"), 25, "*", "*")
  massachusetts = self.census_api.acs.state(cols, 25)

  muni.append(massachusetts[0])

  table = pd.DataFrame.from_dict(muni)
  table["vacancy_rate"] = 
  self.munged = table

dataset.munge(munging)
dataset.project("AvgHHSize")

