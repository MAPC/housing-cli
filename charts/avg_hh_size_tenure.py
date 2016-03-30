# Average Household Size by Tenure
sql = "SELECT * FROM tabular.b25010_avg_hhsize_by_tenure_acs_m WHERE muni_id = %s" % batch.muni_id
dataset = DataGrid(batch, sql, [])

def munging(self):
  y2000 = self.census_api.sf1.state_county_subdivision(("NAME", "H012001", "H012002", "H012003"), 25, self.county_fips, self.cousub_fips, year="2000")[0]
  y2010 = self.census_api.sf1.state_county_subdivision(("NAME", "H0120001", "H0120002", "H0120003"), 25, self.county_fips, self.cousub_fips, year="2010")[0]
  
  y2010["YEAR"] = 2010
  y2000["YEAR"] = 2000

  y2010["H012001"] = y2010.pop("H0120001")
  y2010["H012002"] = y2010.pop("H0120002")
  y2010["H012003"] = y2010.pop("H0120003")

  collapse = [] 
  collapse.append(y2000)
  collapse.append(y2010)

  self.munged = pd.DataFrame.from_dict(collapse)[["H012001", "H012002", "H012003", "YEAR"]]
  self.munged.columns = ["Overall Household Size", "Owner-Occupied Household Size", "Renter-Occupied Household Size", "Year"]

dataset.munge(munging)
dataset.project("AvgHHSize")
