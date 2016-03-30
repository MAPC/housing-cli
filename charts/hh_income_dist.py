# Household Income Distribution
# sql = "SELECT * FROM tabular.b19001_hh_income_acs_m WHERE acs_year = '2010-14' AND muni_id = '%s'" % MUNI_ID
# df = read_sql(sql, conn, coerce_float=True, params=None)
# cols = ['incu10','inc1015','inc1520','inc2025','inc2530','inc3035','inc3540','inc4045','inc4550','inc5060','inc6075','i7599','i100125','i125150','i150200','in200o']
# incomes = df[cols].transpose().sort_values(by=[0])[0].tolist()
# column(workbook, cols, incomes, type='bar', headings=["Income Category","Income Distribution"],  sheetname="IncomeDist")

# Household Income Distribution
sql = "SELECT * FROM tabular.b19001_hh_income_acs_m WHERE acs_year = '2010-14' AND muni_id = '%s'" % batch.muni_id
dataset = DataGrid(batch, sql, [])
chart = Chart(batch,dataset,"IncomeDist")

def munging(self):

  df = self.data()
  cols = ['incu10','inc1015','inc1520','inc2025','inc2530','inc3035','inc3540','inc4045','inc4550','inc5060','inc6075','i7599','i100125','i125150','i150200','in200o']
  self.munged = df[cols].transpose().sort_values(by=[0])
  self.munged.columns = ["Income Distribution"]
  self.munged.insert(0, "Income Category", self.munged.index)

dataset.munge(munging)
chart.generate(type="column")
