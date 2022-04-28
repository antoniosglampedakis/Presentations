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

listofcompanynames = [
    'FOLK WUNDERMAN THOMPSON', 'J. WALTER THOMPSON', 'J. WALTER THOMPSON AMSTERDAM', 'J. WALTER THOMPSON ARGENTINA',
    'J. WALTER THOMPSON ATLANTA', 'J. WALTER THOMPSON BANGKOK', 'J. WALTER THOMPSON BEIRUT', 'J. WALTER THOMPSON BRAZIL',
    'J. WALTER THOMPSON CAIRO', 'J. WALTER THOMPSON CANADA', 'J. WALTER THOMPSON COLOMBIA',
    'J. WALTER THOMPSON COSTA RICA', 'J. WALTER THOMPSON FOLK', 'J. WALTER THOMPSON HONG KONG',
    'J. WALTER THOMPSON INDIA', 'J. WALTER THOMPSON ITALY', 'J. WALTER THOMPSON JAKARTA',
    'J. WALTER THOMPSON JAPAN', 'J. WALTER THOMPSON MEXICO', 'J. WALTER THOMPSON NEW ZEALAND',
    'J. WALTER THOMPSON PARIS', 'J. WALTER THOMPSON PERTH', 'J. WALTER THOMPSON PERU', 'J. WALTER THOMPSON PHILIPPINES',
    'J. WALTER THOMPSON PUERTO RICO', 'J. WALTER THOMPSON RUSSIA', 'J. WALTER THOMPSON SINGAPORE',
    'J. WALTER THOMPSON TAIWAN', 'MANAJANS/J. WALTER THOMPSON', 'MIRUM', 'MIRUM AGENCY',
    'POSSIBLE', 'POSSIBLE MOSCOW', 'SANTO', 'SANTO LONDON', 'SANTO USA', 'SWIFT', 'WUNDERMAN', 'WUNDERMAN BRAZIL',
    'WUNDERMAN CATO JOHNSON', 'WUNDERMAN DUBAI', 'WUNDERMAN HEALTH', 'WUNDERMAN MEXICO', 'WUNDERMAN MEXICO',
    'WUNDERMAN PHANTASIA', 'WUNDERMAN THOMPSON', 'WUNDERMAN THOMPSON ARGENTINA', 'WUNDERMAN THOMPSON BANGKOK',
    'WUNDERMAN THOMPSON HEALTH', 'WUNDERMAN THOMPSON MOSCOW', 'WUNDERMAN THOMPSON NEW ZEALAND',
    'WUNDERMAN THOMPSON SPAIN', 'WUNDERMAN-BIENALTO'
]
print("correcting dataframe")



dateTime = datetime.datetime.now().strftime("%d%m%Y_%H%M")

writer = pd.ExcelWriter("benchmarkWundermanThompson{}.xlsx".format(dateTime) )

dfWT = dfAll[dfAll["CompanyNameFinal"].isin(listofcompanynames)]
dfWT = correctingWT(dfWT)



creatingSlide(dfAll, writer, "Cannes Lions Overview")
creatingSlide(dfWT, writer, "WundermanThompson Overview")

gettingAgencyNumbers(dfWT, "CompanyNameFinal", "FCB Deep-dive", writer)
gettingAgencyNumbersFromList(dfAll, listofNetworkNames, "NetworkNameFinal", "FCB vs. Top 20 Networks", writer)

marks = checkSpecificEntry(entry ="DESTINATION MENU", columnToAggregate="EntryTypeNameFinal", fileFromPc ="AllEntrieswithMarks2021_2020_WithYear.xlsx", year=2021,
                   columnToSearchForEntries = "Title", secondEntryToFilter= None, secondCriterionToFilter= None, writingFile=writer)
marks.to_excel(writer, sheet_name="Piece of Work", startrow=6, startcol=1)

writer.close()
print("finished")
