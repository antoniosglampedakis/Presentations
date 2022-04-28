from CorrectingFunctions import *
from functions import *
from imports import *
from query import QueryForEdelmanOtherFields
from edelmancorrectingfunction import correctingEdelmanCreative
from CorrectingFunctions import correctingEdelman
print("before connecting to database")
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=iafsql;' #changed to live database instead of dev.
                      'Database=IAFF;'
                      'Trusted_Connection=yes;')
dfAll = pd.read_sql(QueryForEdelmanOtherFields, conn)
print("connected to database")
dfAll = correctingDfFromDatabase(dfAll, True)

dfAll = correctingDroga(dfAll)
print("correcteddroga?")
print("droga5: ",dfAll[dfAll["companyName"].str.contains("DROGA5", case = False)|\
      ((dfAll["NetworkName"].str.contains("DROGA5", case = False) ))]\
.groupby("FestivalYear")["FestivalYear"].count())
dfAll = correctingDeloitte(dfAll)
print("corrected dEloitte?")
print("deloitte", dfAll[dfAll["companyName"].str.contains("DELOITTE", case = False)\
|((dfAll["NetworkName"].str.contains("DELOITTE", case = False)))]\
.groupby("FestivalYear")["FestivalYear"].count())

dfAll = correctingWeberShandwick(dfAll)
dfAll = correctingEdelman(dfAll)
dfAll = correctingEdelmanCreative(dfAll, "creativeAgency","correctCreativeAgency","correctCreativeNetwork")
dfAll = correctingEdelmanCreative(dfAll, "creativeAgency2","correctCreativeAgency2","correctCreativeNetwork2")




print("correcting dataframe")



dateTime = datetime.datetime.now().strftime("%d%m%Y_%H%M")

writer = pd.ExcelWriter("benchmarkEdelman{}.xlsx".format(dateTime) )

dfEdelman = dfAll[(dfAll["NetworkNameFinal"].str.contains("EDELMAN", case = False))]
dfEdelmanCreative = dfAll[(dfAll["correctCreativeNetwork"].str.contains("EDELMAN", case = False, na = False))]
dfEdelmanCreative2 = dfAll[(dfAll["correctCreativeNetwork2"].str.contains("EDELMAN", case = False, na = False))]


creatingSlide(dfAll, writer, "Cannes Lions Overview")
creatingSlide(dfEdelmanCreative, writer, "Edelman creative Overview")
creatingSlide(dfEdelmanCreative2, writer, "Edelman creative Overview 2")

creatingSlide(dfEdelman, writer, "Edelman Overview")



listofNetworkNames = ['EDELMAN','DROGA5','DELOITTE','WEBER SHANDWICK']


gettingAgencyNumbers(dfEdelman, "CompanyNameFinal", "Edelman Deep-dive", writer)

gettingAgencyNumbersFromList(dfAll, listofNetworkNames, "NetworkNameFinal", "Edelman vs. Selected Networks", writer)

marks = checkSpecificEntry(entry ="#BUYBACKFRIDAY", columnToAggregate="EntryTypeNameFinal"
                   , fileFromPc ="AllEntrieswithMarks2021_2020_WithYear.xlsx", year=2021,
                   columnToSearchForEntries = "Title", secondEntryToFilter= None, secondCriterionToFilter= None,
                   writingFile=writer)

marks.to_excel(writer, sheet_name="Piece of Work", startrow=0, startcol=0)

writer.close()
print("finished")
