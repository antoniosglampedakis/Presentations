from imports import *

def correctingTopNetworks(df):
    df["NetworkNameFinal"] = df["NetworkName"]
    df["CompanyNameFinal"] = df["companyName"]

    df.loc[((df["NetworkName"] == "J. WALTER THOMPSON")
            | (df["NetworkName"] == "WUNDERMAN")
            ), "NetworkNameFinal"] = "WUNDERMAN THOMPSON"

    df.loc[(df["companyName"].str.contains("WUNDERMAN")) & (df["FestivalYear"] == 2018) & (
            df["NetworkName"] == "WPP non-network")
    , "NetworkNameFinal"] = "WUNDERMAN THOMPSON"

    df.loc[(df["companyName"] == "AKQA") & (df["FestivalYear"] == 2018), "NetworkNameFinal"] = "AKQA"

    df.loc[(df["companyName"].str.contains("GEOMETRY OGILVY JAPAN")), "NetworkNameFinal"] = "OGILVY"


    havas_creative = "havas creative"
    df.loc[((df["NetworkName"] =="havas")|(df["NetworkName"] ==havas_creative)), "NetworkNameFinal"] = havas_creative

    df.loc[((df["companyName"] =="BETC")
            & (df["NetworkName"].str.contains("havas", case = False))
            &(df["FestivalYear"] == 2018)), "NetworkNameFinal"] = havas_creative

    df.loc[((df["companyName"] == "VML")
            | (df["companyName"] == "Y&R")
            | (df["companyName"] == "VMLY&R")
            | ((df["NetworkName"].str.contains("taxi", case=False))))
           | (df["companyName"].str.contains("THE CLASSIC PARTNERSHIP", case=False))
    , "NetworkNameFinal"] = "VMLY&R"

    return df
def correctingYears(df):
    df["FestivalYear"] = df["FestivalYear"].replace(2020, 2021)
    df["FestivalYear"] = df["FestivalYear"].replace(2021, '2020/2021')
    return df

def correctingMarksDf(df):
    df["EntryTypeNameFinal"] = df["EntryTypeName"]

    df.loc[((df["EntryTypeName"] == "Glass: The Lion For Change")
            |(df["EntryTypeName"] == "Glass - The Lion For Change")
            ), "EntryTypeNameFinal"] = "Glass"

    df.loc[(df["EntryTypeName"] == "Entertainment for Music"), "EntryTypeNameFinal"] = "Entertainment Lions For Music"
    df.loc[(df["EntryTypeName"] == "Entertainment for Sport"), "EntryTypeNameFinal"] = "Entertainment Lions For Sport"

    return df

def correctingDfFromDatabase(df, Year):
    #df = df.apply(lambda x: x.astype(str).str.strip() if x.dtype == "object" else x)

    df["NetworkNameFinal"] = df["NetworkName"]
    df["CompanyNameFinal"] = df["companyName"]

    df["Shortlist"] = df["Shortlist"].fillna(0)

    listOfColumnsToCorrect = ["companyName", "coTown", "Country", "NetworkName"]

    for column in listOfColumnsToCorrect:
        df[column] = df[column].str.lstrip()
        df[column] = df[column].str.rstrip()
    if Year:
        df = correctingYears(df)

    df["EntryTypeNameFinal"] = df["EntryTypeName"]

    df.loc[((df["EntryTypeName"] == "Glass: The Lion For Change")
            |(df["EntryTypeName"] == "Glass - The Lion For Change")
            ), "EntryTypeNameFinal"] = "Glass"

    df.loc[(df["EntryTypeName"] == "Entertainment for Music"), "EntryTypeNameFinal"] = "Entertainment Lions For Music"
    df.loc[(df["EntryTypeName"] == "Entertainment for Sport"), "EntryTypeNameFinal"] = "Entertainment Lions For Sport"



    df["RegionNameFinal"] = df["RegionName"]

    df.loc[(df["RegionNameFinal"] == "ASIA"), "RegionNameFinal"] = "APAC"
    df.loc[(df["RegionNameFinal"] == "AUSTRALIA & SOUTH PACIFIC"), "RegionNameFinal"] = "APAC"
    df.loc[(df["RegionNameFinal"] == "EASTERN EUROPE"), "RegionNameFinal"] = "EUROPE"


    df.loc[((df["Winner"] == "CEFP")|(df["Winner"] == "TGP")|(df["Winner"] == "GP4G")), "Winner"] = "GP"

    df["CountryFinal"] = df["Country"]

    df.loc[((df["Country"] == "CHINESE TAIPEI")
            | (df["Country"] == "TAIWAN")),
           "CountryFinal"] = "TAIPEI"
    df.loc[(df["Country"] == "HONG KONG SAR") , "CountryFinal"] = "HONG KONG"

    return df

def cleaningCountries(df):
    df["CountryFinal"] = df["Country"]

    df.loc[((df["Country"] == "CHINESE TAIPEI")
            | (df["Country"] == "TAIWAN")),
           "CountryFinal"] = "TAIPEI"
    df.loc[(df["Country"] == "HONG KONG SAR") , "CountryFinal"] = "HONG KONG"
    return df

def correctingDfTotal(df):
    df = correctingDfFromDatabase(df=df, Year=True)
    df = correctingTopNetworks(df)
    #df = correctingFCB(df)
    return df


def creatingSlides(dfAll, dfFCB):
    return

def creatingSlide(df, writer, sheetName):
    allEntries = df.groupby("FestivalYear")["All Entries"].count()
    shortlists = df[df["Shortlist"] == 1].rename(columns={"All Entries": "Shortlisted"})\
    .groupby("FestivalYear")["Shortlisted"]\
        .count()
    winners = df[df["Winner"].notnull()].rename(columns={"All Entries": "Winners"})\
    .groupby("FestivalYear")["Winners"].count()#transform to table

    listofseries = [allEntries, shortlists, winners]
    cols = [2018, 2019, "2020/2021"]
    skata = pd.DataFrame(listofseries, columns=cols)
    skata.to_excel(writer, sheet_name= sheetName, startrow = 1)


    df.groupby(["EntryTypeNameFinal", "FestivalYear"]).count().reset_index(). \
        pivot_table("FestivalCode", "EntryTypeNameFinal", "FestivalYear")\
        .to_excel(writer, sheet_name=sheetName, startrow = 6)#need the sum

    df[df["Shortlist"]==1].groupby(["EntryTypeNameFinal", "FestivalYear"]).count().reset_index(). \
        pivot_table("FestivalCode", "EntryTypeNameFinal", "FestivalYear")\
        .to_excel(writer, sheet_name=sheetName, startrow = 39)#need the sum

    df[df["Winner"].notnull()].groupby(["EntryTypeNameFinal", "FestivalYear"]).count().reset_index(). \
        pivot_table("FestivalCode", "EntryTypeNameFinal", "FestivalYear")\
        .to_excel(writer, sheet_name=sheetName, startrow = 77)#need the sum

    df.groupby(["Winner", "FestivalYear"]).count().reset_index(). \
        pivot_table("FestivalCode", "Winner", "FestivalYear")\
        .to_excel(writer, sheet_name=sheetName, startrow = 111)#need the sum


    df.groupby(["RegionNameFinal", "FestivalYear"]).count().reset_index(). \
        pivot_table("FestivalCode", "RegionNameFinal", "FestivalYear")\
        .to_excel(writer, sheet_name=sheetName, startrow = 121)#need the sum


    df[df["Shortlist"] == 1].groupby(["RegionNameFinal", "FestivalYear"]).count().reset_index(). \
        pivot_table("FestivalCode", "RegionNameFinal", "FestivalYear")\
        .to_excel(writer, sheet_name=sheetName, startrow = 129)#need the sum

    df[df["Winner"].notnull()].groupby(["RegionNameFinal", "FestivalYear"]).count().reset_index(). \
        pivot_table("FestivalCode", "RegionNameFinal", "FestivalYear")\
        .to_excel(writer, sheet_name=sheetName, startrow = 141)#need the sum



def gettingAgencyNumbers(df, column, sheetName, writer):

    years =[2018, 2019, "2020/2021"]
    dictionaryEntries = {}
    listOfSomething = df[column].unique()
    listOfSomething.sort()
    for company in listOfSomething:
        for year in years:
            dictionaryEntries[company, year] = len(df[(df["FestivalYear"] == year)&(df[column].str.contains(company, case = False))])

    dfEntries = pd.Series(dictionaryEntries).reset_index()
    dfEntries.columns = ["Agencies","Year","Entries"]
    dfEntries.pivot("Agencies", "Year", "Entries").to_excel(writer,sheet_name= sheetName, startcol= 1, startrow= 1)

    dictionaryShortlist = {}
    for company in listOfSomething:
        for year in years:
            dictionaryShortlist[company, year] = len(df[(df["FestivalYear"] == year)\
                             &(df[column].str.contains(company, case = False))&(df["Shortlist"]==1)])
    dfShortlists = pd.Series(dictionaryShortlist).reset_index()
    dfShortlists.columns = ["Agencies","Year","Shortlists"]
    dfShortlists.pivot("Agencies", "Year", "Shortlists").to_excel(writer,sheet_name= sheetName, startcol= 5, startrow= 1, index = False)



    dictionaryWinners = {}
    for company in listOfSomething:
        for year in years:
            dictionaryWinners[company, year] = len(df[(df["FestivalYear"] == year)&(df[column].str.contains(company, case = False))
                                                  &(df["Winner"].notnull())])

    dfWinners = pd.Series(dictionaryWinners).reset_index()
    dfWinners.columns = ["Agencies","Year","Winners"]
    dfWinners.pivot("Agencies", "Year", "Winners").to_excel(writer,sheet_name= sheetName, startcol= 8, startrow= 1, index = False)



def gettingAgencyNumbersFromList(df, listOfSomething, column, sheetName, writer):

    years =[2018, 2019, "2020/2021"]

    festivalAveragePercentage20202021 = len(df[(df.Winner.notnull())&(df.FestivalYear == "2020/2021")])/len(df[df.FestivalYear == "2020/2021"])


    dictionaryEntries = {}
    for company in listOfSomething:
        for year in years:
            dictionaryEntries[company, year] = len(df[(df["FestivalYear"] == year)&(df[column].str.contains(company, case = False))])

    dfEntries = pd.Series(dictionaryEntries).reset_index()
    dfEntries.columns = ["Agencies","Year","Entries"]
    dfEntries.pivot("Agencies", "Year", "Entries").to_excel(writer,sheet_name= sheetName, startcol= 1, startrow= 1)

    dictionaryShortlist = {}
    for company in listOfSomething:
        for year in years:
            dictionaryShortlist[company, year] = len(df[(df["FestivalYear"] == year)\
                             &(df[column].str.contains(company, case = False))&(df["Shortlist"]==1)])
    dfShortlists = pd.Series(dictionaryShortlist).reset_index()
    dfShortlists.columns = ["Agencies","Year","Shortlists"]
    dfShortlists.pivot("Agencies", "Year", "Shortlists").to_excel(writer,sheet_name= sheetName, startcol= 5, startrow= 1, index = False)



    dictionaryWinners = {}
    for company in listOfSomething:
        for year in years:
            dictionaryWinners[company, year] = len(df[(df["FestivalYear"] == year)&(df[column].str.contains(company, case = False))
                                                  &(df["Winner"].notnull())])

    dfWinners = pd.Series(dictionaryWinners).reset_index()
    dfWinners.columns = ["Agencies","Year","Winners"]
    dfWinners.pivot("Agencies", "Year", "Winners").to_excel(writer,sheet_name= sheetName, startcol= 8, startrow= 1, index = False)


    dictionaryPercentages = {}
    for company in listOfSomething:
        for year in years:
            dictionaryPercentages[company, year] = len(df[(df["FestivalYear"] == year)&(df[column].str.contains(company, case = False))
                                                  &(df["Winner"].notnull())])/ len(df[(df["FestivalYear"] == year)&(df[column].str.contains(company, case = False))])


    dfPercentages = pd.Series(dictionaryPercentages).reset_index()
    dfPercentages.columns = ["Agencies","Year","Winners"]
    dfPercentages.pivot("Agencies", "Year", "Winners").to_excel(writer,sheet_name= sheetName, startcol= 11, startrow= 1, index = False)

    (dfPercentages.pivot("Agencies", "Year", "Winners")["2020/2021"] - dfPercentages.pivot("Agencies", "Year", "Winners")[2019])\
        .rename("2020/2021 vs 2019")\
        .to_excel(writer,sheet_name= sheetName, startcol= 14, startrow= 1, index = False)
    (dfPercentages.pivot("Agencies", "Year", "Winners")["2020/2021"] - festivalAveragePercentage20202021) \
        .rename("vs Festival Average 2020/2021")\
        .to_excel(writer, sheet_name=sheetName, startcol=15, startrow=1, index=False)


def checkSplitsForEntry(entries,  year, fileFromPc):
    dateTime = datetime.datetime.now().strftime("%d%m%Y_%H%M")
    writingFile =pd.ExcelWriter( "entryanalysis_per_mark_average{}.xlsx".format(dateTime),engine= "xlsxwriter" )

    if year == 2020:
        sheet_name =0
    elif year == 2021:
        sheet_name = 1
    else:
        print("Not a valid year")


    if isinstance(entries, str):
        entries = [entries]

    df = pd.read_excel(fileFromPc, sheet_name = sheet_name)
    dfOutput = pd.DataFrame(columns = ["EntryTypeName","RoundOfVoting","TitleOfAd", "Split1", "Split2", "Split3", "Split4", "Split5"])
    for entry in entries:
        pass
    filteredDf = df[(df["TitleOfAd"].str.contains(entry.lower(), case=False, na=False))]

    listofCategories = list(df["EntryTypeName"].unique())
    print(listofCategories)

    for category in listofCategories:
        print(category)
        dfTemp = filteredDf[(filteredDf["EntryTypeName"] == category)]
        print(len(dfTemp))
        row =dfTemp.groupby(["EntryTypeName","RoundOfVoting","TitleOfAd"])[["Split1", "Split2", "Split3", "Split4", "Split5"]].mean()
        row = row.reset_index().values.tolist()
        print(row)
        for i in range(len(row)):
            print("asdfafdasd, i", i)
            dfOutput.loc[len(dfOutput)] = row[i]

    dfOutput.to_excel(writingFile, sheet_name=entry)
    writingFile.close()


def checkSpecificEntry(entry, columnToAggregate, fileFromPc, year,
                       columnToSearchForEntries, secondEntryToFilter, secondCriterionToFilter, writingFile):

    df = pd.read_excel(fileFromPc)
    df = df.rename(columns = {"Short": "Shortlist", "Entry Type":"EntryTypeName", "Award": "Winner"})

    df = correctingMarksDf(df)


    SecondMark = "Second Mark"
    FirstMark = "First Mark"

    dfTemp = df[df["FestivalYear"] == year]

    print(type(entry))
    print(entry)
    if secondEntryToFilter is None:
        filteredDf = dfTemp[(dfTemp[columnToSearchForEntries].str.contains(entry.lower(), case = False, na = False))]
        print("mpainei sto none gamwtoxristo?")
    else:
        filteredDf = dfTemp[(dfTemp[columnToSearchForEntries].str.contains(entry.lower(), case = False, na = False))&
                    (dfTemp[secondCriterionToFilter].str.contains(secondEntryToFilter.lower(), case = False, na = False))]
        print("den mpainei sto none gamwtoxristo?")

    listofCategories = list(filteredDf[columnToAggregate].unique())

    EntryDf = filteredDf.groupby(columnToAggregate)[FirstMark, SecondMark].mean()

    dfAll = pd.DataFrame()
    dfAll["All First Mark Average"] = dfTemp[dfTemp[columnToAggregate].isin(listofCategories)].groupby([columnToAggregate])[FirstMark].mean()
    dfAll["All Second Mark Average"] = dfTemp[dfTemp[columnToAggregate].isin(listofCategories)].groupby([columnToAggregate])[SecondMark].mean()


    newShort = pd.DataFrame()

    newShort["Short First Mark Average"] = dfTemp[(dfTemp[columnToAggregate].isin(listofCategories)) &
                                                  (dfTemp["Shortlist"] == "YES")].groupby([columnToAggregate])[FirstMark].mean()

    newShort["Short Second Mark Average"] = dfTemp[(dfTemp[columnToAggregate].isin(listofCategories))
           & (dfTemp["Shortlist"] == "YES")].groupby([columnToAggregate])[SecondMark].mean()



    awardsDf = dfTemp[(dfTemp[columnToAggregate].isin(listofCategories)) & (dfTemp["Winner"].notnull())].groupby([columnToAggregate, "Winner"])[
        SecondMark, FirstMark].mean().reset_index().set_index(columnToAggregate)\
    .pivot_table([SecondMark, FirstMark], columnToAggregate, "Winner")

    goldAndGpAwardsDf = dfTemp[(dfTemp[columnToAggregate].isin(listofCategories)) &
                               ((dfTemp["Winner"]== 'Gold Lion')|(dfTemp["Winner"]== 'Grand Prix'))].groupby([columnToAggregate])[
        SecondMark, FirstMark]\
        .mean().reset_index().set_index(columnToAggregate)\
        .rename(columns={SecondMark: "Second Mark For GP/GL", FirstMark: "First Mark For GP/GL"})\
    .pivot_table(['Second Mark For GP/GL', 'First Mark For GP/GL'], columnToAggregate)

    final = pd.concat([ EntryDf,dfAll,newShort, awardsDf, goldAndGpAwardsDf] , axis =1)
#    final.to_excel(writingFile, sheet_name="Piece of Work", startrow= 6,startcol=1)
    return final



def gettingEarliestOccurance (df,columns, year): #some results seem fake
    dateTime = datetime.datetime.now().strftime("%d%m%Y_%H%M")

    if isinstance(columns, str):
        columns = [columns]

    writingFile =pd.ExcelWriter( "first appearences SA 2022{}.xlsx".format(dateTime) )
    for column in columns:
        print("do we have an issue with?" +column)
        df = df.dropna(subset=[column])
        df[column] = df[column].str.lstrip()
        df[column] = df[column].str.rstrip()
        winners = df[(df["FestivalYear"] == year) & (df["Winner"].notnull())]
        shortlisted = df[(df["FestivalYear"] == year) & (df["Shortlist"] == 1)]
        Appearences = df[(df["FestivalYear"] == year)]
        WinnersDF = pd.DataFrame()
        WinnersDF["Winners" + str(year)] = winners[column].unique()
        WinnersDF = WinnersDF.set_index("Winners" + str(year))
        otinanai = '|'.join(pd.Series(WinnersDF.index))

        WinnersDF[column+" min"] = df[df[column].str.contains('|'.join(otinanai))].groupby(column)["FestivalYear"].min()
        WinnersDF[column+" max"] = df[df[column].str.contains('|'.join(otinanai))].groupby(column)["FestivalYear"] \
            .unique().apply(lambda x: findsecondlargest(x))
        WinnersDF.sort_index().to_excel(writingFile, sheet_name= column+" Winners")

        shortlistedDf = pd.DataFrame()
        shortlistedDf["Shortlisted" + str(year)] = shortlisted[column].unique()
        shortlistedDf = shortlistedDf.set_index("Shortlisted" + str(year))
        otinanai = '|'.join(pd.Series(shortlistedDf.index))

        shortlistedDf[column+" min"] = df[df[column].str.contains('|'.join(otinanai))].groupby(column)["FestivalYear"].min()
        shortlistedDf[column+" max"] = df[df[column].str.contains('|'.join(otinanai))].groupby(column)["FestivalYear"] \
            .unique().apply(lambda x: findsecondlargest(x))
        shortlistedDf.sort_index().to_excel(writingFile, sheet_name= column+" Shortlisted")

        AppearencesDF = pd.DataFrame()
        AppearencesDF["Appearences" + str(year)] = Appearences[column].unique()
        AppearencesDF = AppearencesDF.set_index("Appearences" + str(year))
        otinanai = '|'.join(pd.Series(AppearencesDF.index))
        AppearencesDF[column+" min"] = df[df[column].str.contains('|'.join(otinanai))].groupby(column)["FestivalYear"].min()
        AppearencesDF[column +" max"] = df[df[column].str.contains('|'.join(otinanai))].groupby(column)["FestivalYear"] \
            .unique().apply(lambda x: findsecondlargest(x))

        AppearencesDF.sort_index().to_excel(writingFile, sheet_name= column+" Appearences")

    writingFile.save()



def findsecondlargest(list):
    if len(list) >=2:
        return np.sort(list)[-2]
    else:
        return 0
