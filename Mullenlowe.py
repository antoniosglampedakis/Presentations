from CorrectingFunctions import *
from functions import *
from imports import *
from query import Query
print("before connecting to database")
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DVLN2DDBS01\EC;' #changed to live database instead of dev.
                      'Database=IAFF;'
                      'Trusted_Connection=yes;')
dfAll = pd.read_sql(Query, conn)
print("connected to database")
dfAll = correctingDfFromDatabase(dfAll, True)
dfAll = correctingMullenlowe(dfAll)


print("correcting dataframe")



dateTime = datetime.datetime.now().strftime("%d%m%Y_%H%M")

writer = pd.ExcelWriter("benchmarkMullenlowe{}.xlsx".format(dateTime) )

dfMullenlowe = dfAll[(dfAll["NetworkNameFinal"].str.contains("mullenlowe", case = False)) |
                     ((dfAll["companyName"] == "THE MARTIN AGENCY")&( dfAll["NetworkName"]== "McCann Worldgroup"))]

creatingSlide(dfAll, writer, "Cannes Lions Overview")
creatingSlide(dfMullenlowe, writer, "MULLENLOWE GROUP Overview")

gettingAgencyNumbers(dfMullenlowe, "CompanyNameFinal", "MULLENLOWE Deep-dive", writer)
gettingAgencyNumbersFromList(dfAll, listofNetworkNames, "NetworkNameFinal", "MULLENLOWE vs. Top 20 Networks", writer)

#CHANGE TITLE NAME, WE DO NOT WANT DESTINATION MENU

listOfTitles = ["MAGNUM XXL TOWEL COLLECTION","THE UNSEEN STORY"]
for entry in listOfTitles:
    marks = checkSpecificEntry(entry = entry, columnToAggregate="EntryTypeNameFinal", fileFromPc ="AllEntrieswithMarks2021_2020_WithYear.xlsx", year=2021,
                   columnToSearchForEntries = "Title", secondEntryToFilter= None, secondCriterionToFilter= None, writingFile=writer)
    marks.to_excel(writer, sheet_name=entry, startrow=0, startcol=0)

writer.close()
print("finished")