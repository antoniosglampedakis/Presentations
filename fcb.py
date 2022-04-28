from CorrectingFunctions import *
from functions import *
from imports import *
from query import Query

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DVLN2DDBS01\EC;' #changed to live database instead of dev.
                      'Database=IAFF;'
                      'Trusted_Connection=yes;')

dfAll = pd.read_sql(Query, conn)

listofcompanynames = [
'Area 23', 'Brand Station', 'FCB Africa', 'FCB Amsterdam', 'FCB Brasil', 'FCB Canada',
    'FCB Chicago', 'Chicago / New York FCB', 'FCB Global', 'FCB Health Europe', 'FCB Health New York',
    'FCB Health Toronto', 'FCB Inferno', 'FCB Interface', 'FCB Lisbon', 'FCB Manila', 'FCB New York',
    'FCB New Zealand', 'FCB Partners Milan', 'FCB Shimoni Finkelstein Barki', 'FCB West', 'FCB/SIX',
    'FCB&FiRe Buenos Aires', 'FCB&FiRe Madrid', 'FCB Ulka', 'Happiness Brussels', 'Happiness Saigon',
    'HelloFCB+', 'Horizon FCB Dubai', 'Oneighty/FCB'
]
##getting the
dfAll = correctingDfFromDatabase(dfAll, True)
dfAll = correctingFCB((dfAll))

dateTime = datetime.datetime.now().strftime("%d%m%Y_%H%M")
writer = pd.ExcelWriter("benchmarkFCB{}.xlsx".format(dateTime) )

dfFCB = dfAll[dfAll["CompanyNameFinal"].str.contains('|'.join(listofcompanynames), case = False)]

creatingSlide(dfAll, writer, "Cannes Lions Overview")
creatingSlide(dfFCB, writer, "FCB Overview")

gettingAgencyNumbers(dfFCB, "CompanyNameFinal", "FCB Deep-dive", writer)
gettingAgencyNumbersFromList(dfAll, listofNetworkNames, "NetworkNameFinal", "FCB vs. Top 20 Networks", writer)


marks = checkSpecificEntry(entry ="UNBOXING IBAI", columnToAggregate="EntryTypeNameFinal", fileFromPc ="AllEntrieswithMarks2021_2020_WithYear.xlsx", year=2021,
                   columnToSearchForEntries = "Title", secondEntryToFilter= None, secondCriterionToFilter= None, writingFile=writer)
marks.to_excel(writer, sheet_name="Piece of Work", startrow=6, startcol=1)

writer.close()
writer.save()
print("finished")
