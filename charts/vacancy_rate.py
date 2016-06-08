# Average Household Size by Tenure
sql = "SELECT * FROM tabular.b25002_b25003_hu_occupancy_by_tenure_race_acs_m WHERE muni_id = %s" % batch.muni_id
dataset = DataGrid(batch, sql, [])

def munging(self):
  # OVERALL:
  # VacantAvailable = (B25004_002E + B25004_003E + B25004_004E + B25004_005E + B25004_008E)
  # Total = VacantAvailable + B25002_002E   
  # VacancyRate = VacantAvailable/Total
  # include MOE

  # RENTAL:
  # VacantAvailable = For Rent + Rented, Not occupied
  # Total = Rental: Occupied Rental + For Rent + Rented, Not occupied
  # VacancyRate = VacantAvailable/Total

  # OWNER:
  # VacantAvailable = For Sale + Sold, not occupied
  # Total = Occupied Owner + For Sale + Sold, not occupied
  # VacancyRate = VacantAvailable/Total

  cols = ["B25002_002E",\
          "B25004_002E",\
          "B25004_003E",\
          "B25004_004E",\
          "B25004_005E",\
          "B25004_008E",\
          "B25003_002E",\
          "B25003_003E"]

  self.full_crosswalk["COUSUB"] = self.full_crosswalk["COUSUB"].apply('{:0>5}'.format)

  # collapsing totals, returns as a series:
  region = pd.DataFrame.from_dict(self.census_api.acs.state_county_subdivision(cols, 25, "*", "*"))
  region = region[region["county subdivision"].isin(self.full_crosswalk[self.full_crosswalk["mapc"] == 1]["COUSUB"])]\
          .astype(int)\
          .sum()
  region = pd.DataFrame(region)
  region.columns= ["region"]

  # returns as a dataframe
  muni = pd.DataFrame.from_dict(self.census_api.acs.state_county_subdivision(cols, 25, self.county_fips, self.cousub_fips))\
          .astype(int).transpose()
  muni.columns = ["muni"]

  # returns as a dataframe
  massachusetts = pd.DataFrame.from_dict(self.census_api.acs.state(cols, 25))\
                  .astype(int).transpose()
  massachusetts.columns = ["massachusetts"]

  # unifying geographies for analysis
  full = muni.join(region).join(massachusetts).transpose()

  full["Overall Vacancy"] =  (full["B25004_002E"] + full["B25004_003E"] + full["B25004_004E"] + full["B25004_005E"] + full["B25004_008E"]) /\
                             (full["B25004_002E"] + full["B25004_003E"] + full["B25004_004E"] + full["B25004_005E"] + full["B25004_008E"] + full["B25002_002E"])

  full["Rental Vacancy"] =  (full["B25004_002E"] + full["B25004_003E"]) /\
                             (full["B25004_002E"] + full["B25004_003E"] + full["B25003_003E"])

  full["Owner Vacancy"] =  (full["B25004_004E"] + full["B25004_005E"]) /\
                             (full["B25004_004E"] + full["B25004_005E"] + full["B25003_002E"])

  full["Geography"] = full.index

  self.munged = full[["Geography", "Overall Vacancy", "Rental Vacancy", "Owner Vacancy"]]

dataset.munge(munging)
dataset.project("VacancyRate")

