from CorrectingFunctions import *
from functions import *
from imports import *
from query import QueryIndAgency
print("before connecting to database")
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=iafsql;' #changed to live database instead of dev.
                      'Database=IAFF;'
                      'Trusted_Connection=yes;')

dfAll = pd.read_sql(QueryIndAgency, conn)
conn.close()

dfAll["Short"] = dfAll["Short"].fillna(0)


dfAll["RegionNameFinal"] = dfAll["RegionName"]

dfAll.loc[(dfAll["RegionNameFinal"] == "EASTERN EUROPE"), "RegionNameFinal"] = "EUROPE"

dfAll["EntryTypeNameFinal"] = dfAll["EntryTypeName"]


dfAll.loc[((dfAll["EntryTypeName"] == "Glass: The Lion For Change")
        | (dfAll["EntryTypeName"] == "Glass - The Lion For Change")
        ), "EntryTypeNameFinal"] = "Glass"
dfAll.loc[(dfAll["EntryTypeName"] == "Entertainment for Music"), "EntryTypeNameFinal"] = "Entertainment Lions For Music"
dfAll.loc[(dfAll["EntryTypeName"] == "Entertainment for Sport"), "EntryTypeNameFinal"] = "Entertainment Lions For Sport"

listOfRegions = dfAll.RegionNameFinal.unique()


dateTime = datetime.datetime.now().strftime("%d%m%Y_%H%M")
writer = pd.ExcelWriter("independent{}.xlsx".format(dateTime) )
for region in listOfRegions:
    dfAll[(dfAll["RegionName"] == region)&(dfAll.AwardCountCode.notnull())]\
    .groupby("companyName")["companyName"].count().sort_values(ascending = False).head(30)\
    .to_excel(writer, sheet_name= "{}  winners".format(region))

    dfAll[(dfAll["RegionName"] == region)&(dfAll.Short ==1)]\
    .groupby("companyName")["companyName"].count().sort_values(ascending = False).head(30)\
    .to_excel(writer, sheet_name="{}  Shortlists".format(region))

writer.close()