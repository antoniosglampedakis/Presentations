from imports import *
from functions import cleaningCountries
from query import OrlaAsiaQuery

print("before connecting to database")
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=iafsql;' #changed to live database instead of dev.
                      'Database=IAFF;'
                      'Trusted_Connection=yes;')
dfAll = pd.read_sql(OrlaAsiaQuery, conn)
print("connected to database")

dfAll = cleaningCountries(dfAll)

dateTime = datetime.datetime.now().strftime("%d%m%Y_%H%M")

writer = pd.ExcelWriter("OrlaAsia{}.xlsx".format(dateTime) )


dfAll.groupby("RegionName")["count"].count().to_excel(writer, sheet_name= "Entries", startrow = 0)
dfAll[dfAll["short"]==1].groupby("RegionName")["count"].count().to_excel(writer, sheet_name= "Shortlisted", startrow = 0)
dfAll[dfAll["Winners"].notnull()].groupby("RegionName")["count"].count().to_excel(writer, sheet_name= "Winners", startrow = 0)

dfAll[dfAll["RegionName"]=="ASIA"].groupby("CountryFinal"  )["count"].count().to_excel(writer, sheet_name= "Entries per CountryFinal", startrow = 0)
dfAll[(dfAll["short"]==1)&(dfAll["RegionName"]=="ASIA")].groupby("CountryFinal")["count"].count().to_excel(writer, sheet_name= "Shortlisted per CountryFinal", startrow = 0)
dfAll[(dfAll["Winners"].notnull()) &(dfAll["RegionName"]=="ASIA")].groupby("CountryFinal")["count"].count().to_excel(writer, sheet_name= "Winners per CountryFinal", startrow = 0)


dfAll[dfAll["RegionName"]=="ASIA"].groupby(["CountryFinal", "FestivalYear"])["count"].count()\
    .to_excel(writer, sheet_name= "Entries per year and Country", startrow = 0)
dfAll[(dfAll["short"]==1)&(dfAll["RegionName"]=="ASIA")].groupby(["CountryFinal", "FestivalYear"])["count"].count()\
    .to_excel(writer, sheet_name= "Shortlisted per year and Country", startrow = 0)
dfAll[(dfAll["Winners"].notnull()) &(dfAll["RegionName"]=="ASIA")].groupby(["CountryFinal", "FestivalYear"])["count"].count()\
    .to_excel(writer, sheet_name= "Winners per year and Country", startrow = 0)
writer.save()
writer.close()