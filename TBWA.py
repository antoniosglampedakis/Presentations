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
conn.close()

print("connected to database")
dfAll = correctingDfFromDatabase(dfAll, True)
dfAll = correctingTBWA(dfAll)

print("correcting dataframe")


dateTime = datetime.datetime.now().strftime("%d%m%Y_%H%M")
dfTBWA = dfAll[dfAll["NetworkNameFinal"].str.contains("TBWA WORLDWIDE", case = False)]

writer = pd.ExcelWriter("benchmarkTBWA{}.xlsx".format(dateTime) )



creatingSlide(dfAll, writer, "Cannes Lions Overview")
creatingSlide(dfTBWA, writer, "TBWA WORLDWIDE Overview")

gettingAgencyNumbers(dfTBWA, "CompanyNameFinal", "TBWA Deep-dive", writer)
gettingAgencyNumbersFromList(dfAll, listofNetworkNames, "NetworkNameFinal", "TBWA WORLDWIDE vs. Top 20 Networks", writer)
#need a different entry name!
entry = "Shwii"
marks = checkSpecificEntry(entry =entry, columnToAggregate="EntryTypeNameFinal", fileFromPc ="AllEntrieswithMarks2021_2020_WithYear.xlsx", year=2021,
                   columnToSearchForEntries = "Title", secondEntryToFilter= None, secondCriterionToFilter= None, writingFile=writer)
marks.to_excel(writer, sheet_name="Piece of Work " + entry, startrow=6, startcol=1)

writer.save()
print("finished")
