# Average Household Size by Tenure
sql = "SELECT * FROM mapc.hous_section8_income_limits_by_year_m WHERE muni_id = %s AND fy_year = 2014" % batch.muni_id
dataset = DataGrid(batch, sql, [])

def munging(self):
  cols = ['il_50_1', 'il_50_2', 'il_50_3', 'il_50_4', 'il_50_5', 'il_50_6', 'il_50_7', 'il_50_8', 'il_30_1', 'il_30_2', 'il_30_3', 'il_30_4', 'il_30_5', 'il_30_6', 'il_30_7', 'il_30_8', 'il_80_1', 'il_80_2', 'il_80_3', 'il_80_4', 'il_80_5', 'il_80_6', 'il_80_7', 'il_80_8']
  df = self.data()[cols]
  transp = df.transpose()
  transp["cols"] = transp.index
  split = transp["cols"].str.split("_", expand=True)
  split.columns = ["col1", "AMI", "HHSize"]
  final = transp.join(split)
  final.columns = ["limit", "cols", "col1", "AMI", "HHSize"]
  self.munged = pd.pivot_table(final, values="limit", index=["HHSize"], columns=["AMI"])
  self.munged.insert(0, "HHSize", self.munged.index)

dataset.munge(munging)
dataset.project("IncomeLimits")

