


# Average Household Size, Subregion
sql = "SELECT * FROM tabular.b25010_avg_hhsize_by_tenure_acs_m WHERE acs_year = '2010-14'"
df = read_sql(sql, conn, coerce_float=True, params=None)
# df["non_white"] = df["totpop"] - df["nhwhi"]
# df["p_nw"] = (df["non_white"] / df["totpop"]) * 100
subregion_munis = df[df["muni_id"].isin(SUBREGIONAL_MUNIS["MUNI_ID"])].sort_values(by=['avghh'], ascending=False)

column(workbook, subregion_munis["municipal"], subregion_munis["avghh"], headings=["Municipalities","Average Household Size, Subregion"],  sheetname="AverageHHSizeSubregion")

