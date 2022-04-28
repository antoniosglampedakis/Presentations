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
'VMLY&R', 'VML', 'VMLY&R BRAZIL', 'PROLAM Y&R', 'Y&R BRAZIL', 'Y&R DUBAI', 'VMLY&R MADRID', 'Y&R MADRID', 'Y&R PRAGUE',
    'Y&R', 'Y&R ANZ', 'VMLY&R COMMERCE', 'Y&R NEW YORK', 'Y&R ISTANBUL', 'DHÉLET Y&R',
     'THE CLASSIC PARTNERSHIP ADVERTISING', 'VMLY&R MEXICO', 'BURSON COHN & WOLFE',
    'VMLY&R PRAGUE', 'VMLY&R SOUTH AFRICA', 'Y&R LONDON', 'THE CLASSIC PARTNERSHIP',
    'VMLY&R LIMA', 'DHELET VMLY&R', 'VMLY&R POLAND', 'Y&R PARIS', 'VMLY&R MELBOURNE', 'Y&R SOUTH AFRICA', 'DHÉLET VMLY&R',
    'BERLIN CAMERON', 'VMLY&R PARIS','SCHOLZ & FRIENDS', "SCHOLZ & FRIENDS HAMBURG","VMLY&R ISTANBUL", 'TAXI TORONTO', 'TAXI', 'TAXI CANADA'
]

print("corrected dataframe")


writer = pd.ExcelWriter("benchmarkVLMYR.xlsx")
dateTime = datetime.datetime.now().strftime("%d%m%Y_%H%M")

dfVLMYR = dfAll[dfAll["CompanyNameFinal"].isin(listofcompanynames)]
dfVLMYR = correctingVLMYR(dfVLMYR)
print("created vlmyr dataframe")


creatingSlide(dfAll, writer, "Cannes Lions Overview")
creatingSlide(dfVLMYR, writer, "dfVLMYR Overview")
print("created first slides)")


gettingAgencyNumbers(dfVLMYR,  "CompanyNameFinal", "VLMR&Y Deep-dive", writer)
gettingAgencyNumbersFromList(dfAll, listofNetworkNames, "NetworkNameFinal", "VLMR&Y vs. Top 20 Networks", writer)

writer.save()
writer.close()
print("finished")