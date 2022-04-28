from imports import *
from query import *
from functions import *
print("before connecting to database")

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DVLN2DDBS01\EC;' #changed to live database instead of dev.
                      'Database=IAFF;'
                      'Trusted_Connection=yes;')
dfAll = pd.read_sql(Query, conn)
dfAll = correctingDfFromDatabase(dfAll, False)
listofCategories = list(dfAll["EntryTypeNameFinal"].unique())
listofCategories.sort()
conn.close()
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DVLN2DDBS01\EC;' #changed to live database instead of dev.
                      'Database=IAFF;'
                      'Trusted_Connection=yes;')


dfpandg = pd.read_sql(pgquery, conn)
print("connected to database")
dfpandg = correctingDfFromDatabase(dfpandg, False)


print(dfpandg.groupby("FestivalYear")["FestivalYear"].count())
print(dfpandg[dfpandg.Shortlist==1].groupby("FestivalYear")["FestivalYear"].count())
print(dfpandg[dfpandg.Winner.notnull()].groupby("FestivalYear")["FestivalYear"].count())

print(dfpandg[dfpandg.Winner.notnull()].groupby(["FestivalYear","Winner"])["Winner"].count())

dfpandg.groupby(["FestivalYear","EntryTypeNameFinal"])["FestivalCode"].count().reset_index()\
    .pivot_table("FestivalCode","EntryTypeNameFinal","FestivalYear").to_clipboard()
dfOutput = pd.DataFrame(columns=["EntryTypeNameFinal","2020", "2021"])

for category in listofCategories:
    dfTemp = dfpandg[(dfpandg["EntryTypeNameFinal"] == category)]
    row = [category,len(dfTemp[dfTemp["FestivalYear"] == 2020]), len(dfTemp[dfTemp["FestivalYear"] == 2021])]
    dfOutput.loc[len(dfOutput)] = row

dfOutput.to_clipboard()