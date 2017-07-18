

# Median Household Income, Subregion
# TODO: Refactor to pull latest ACS date
# sql = "SELECT * FROM tabular.b25119_mhi_tenure_acs_m WHERE acs_year = '2010-14'"
# df = read_sql(sql, conn, coerce_float=True, params=None)
# mhi = df[df['muni_id'].isin(SUBREGIONAL_MUNIS["MUNI_ID"])].sort_values(by=['mhi'], ascending=False)
# column(workbook, mhi["municipal"], mhi["mhi"], headings=["Municipalities", "Median Household Income"],  sheetname="HHIncomeMedian")

# Housing Units by Year Built
sql = "SELECT * FROM tabular.b25119_mhi_tenure_acs_m WHERE acs_year = '2011-15'"
dataset = DataGrid(batch, sql, [])
chart = Chart(batch,dataset,"HHIncomeMedian")

def munging(self):
  df = self.data()
  mhi = df[df['muni_id'].isin(self.subregional_munis["MUNI_ID"])].sort_values(by=['mhi'], ascending=False)
  self.munged = mhi[["municipal", "mhi"]]
  self.munged.columns = ["Municipalities", "Median Household Income"]

dataset.munge(munging)
chart.generate(type="column")

chart.chart.set_title({
  'name': 'Housing Units by Year Built, %s' % dataset.subregion
})
