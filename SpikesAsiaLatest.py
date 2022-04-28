#this file should not be here, since it is not a benchmarking issue.
#However, since i have most of my cleaning functions here I am adding that file as well.

from functions import correctingDfFromDatabase
from imports import *
from functions import gettingEarliestOccurance
from CorrectingFunctions import addingAllCorrectingFunctions
from query import QuerySaLatest
print("before connecting to database")
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=iafsql;' #changed to live database instead of dev.
                      'Database=IAFF;'
                      'Trusted_Connection=yes;')
dfAll = pd.read_sql(QuerySaLatest, conn)


print("connected to database")
dfAll = correctingDfFromDatabase(dfAll, False)
dfAll = addingAllCorrectingFunctions(dfAll)
dfAll = dfAll.rename({'UltimateHoldingCompanyName':"Holdings"}, axis = 1)


listOfColumns = ["NetworkNameFinal","RegionNameFinal", "Holdings","RegionNameFinal","CountryFinal"]


for column in listOfColumns:
    dfAll[column] = dfAll[column].replace("\+","&", regex = True)
    dfAll[column] = dfAll[column].replace(r"\\"," ", regex = True)


gettingEarliestOccurance(df=dfAll, columns= listOfColumns, year= 2022 )