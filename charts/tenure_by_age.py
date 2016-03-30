# Average Household Size by Tenure
sql = "SELECT * FROM tabular.b25010_avg_hhsize_by_tenure_acs_m WHERE muni_id = %s" % batch.muni_id
dataset = DataGrid(batch, sql, [])
chart = Chart(batch,dataset,"TenureByAge")

def munging(self):
  cols = tuple(["NAME",\
                "B25007_003E",\
                "B25007_004E",\
                "B25007_005E",\
                "B25007_006E",\
                "B25007_007E",\
                "B25007_008E",\
                "B25007_009E",\
                "B25007_010E",\
                "B25007_011E",\
                "B25007_013E",\
                "B25007_014E",\
                "B25007_015E",\
                "B25007_016E",\
                "B25007_017E",\
                "B25007_018E",\
                "B25007_019E",\
                "B25007_020E",\
                "B25007_021E"])

  response = self.census_api.acs.state_county_subdivision(cols, 25, self.county_fips, self.cousub_fips)
  table = pd.DataFrame.from_dict(response)

  owner = ["B25007_003E",\
            "B25007_004E",\
            "B25007_005E",\
            "B25007_006E",\
            "B25007_007E",\
            "B25007_008E",\
            "B25007_009E",\
            "B25007_010E",\
            "B25007_011E",]

  renter = ["B25007_013E",\
            "B25007_014E",\
            "B25007_015E",\
            "B25007_016E",\
            "B25007_017E",\
            "B25007_018E",\
            "B25007_019E",\
            "B25007_020E",\
            "B25007_021E"]

  index_list = ["Householder 15 to 24 years",\
                "Householder 25 to 34 years",\
                "Householder 35 to 44 years",\
                "Householder 45 to 54 years",\
                "Householder 55 to 59 years",\
                "Householder 60 to 64 years",\
                "Householder 65 to 74 years",\
                "Householder 75 to 84 years",\
                "Householder 85 years and over"]

  owner_table = table[owner]
  owner_table = owner_table.transpose()
  owner_table.columns = ["Owner Households"]
  owner_table.index = index_list

  renter_table = table[renter]
  renter_table = renter_table.transpose()
  renter_table.columns = ["Renter Households"]
  renter_table.index = index_list

  self.munged = owner_table.join(renter_table).convert_objects(convert_numeric=True)
  self.munged.insert(0,"Age of Householder", self.munged.index)

dataset.munge(munging)
chart.generate(type="column", subtype="percent_stacked")
