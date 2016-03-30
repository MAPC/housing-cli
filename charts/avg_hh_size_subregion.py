# Average Household Size, Subregion
dataset = DataGrid(batch, "SELECT * FROM tabular.b25010_avg_hhsize_by_tenure_acs_m WHERE acs_year = '2010-14'", [])
chart = Chart(batch,dataset,"avg_hh_size_subregion")

def munging(self):
  df = self.data()
  self.munged = df[df["muni_id"]\
    .isin(self.subregional_munis["MUNI_ID"])]\
    .sort_values(by=['avghh'], ascending=False)[['municipal', 'avghh']]\

  self.munged.columns = ["Municipalities", "Average Household Size"]

dataset.munge(munging)
chart.generate(type="column")
