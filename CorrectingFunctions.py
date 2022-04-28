import pandas as pd
import numpy as np


def correctingFCB(df):
    df["CompanyNameFinal"] = df["companyName"]
#FCB health new york
    df.loc[((df["companyName"] == "FCB HEALTH")&(df["coTown"] == "New York")), "CompanyNameFinal"] = "FCB Health New York"
#fcb health toronto
    df.loc[((df["companyName"] == "FCB HEALTH")&(df["coTown"] == "Toronto")), "CompanyNameFinal"] = "FCB Health Toronto"
#fcb partners milan
    df.loc[((df["companyName"] == "FCB PARTNERS")&(df["coTown"] == "Milan")), "CompanyNameFinal"] = "FCB Partners Milan"
#fcb fire buenos aires
    df.loc[((df["companyName"] == "FCB&FIRE")&(df["coTown"] == "Buenos Aires")), "CompanyNameFinal"] = "FCB&FiRe Buenos Aires"
#fcb fire madrid
    df.loc[((df["companyName"] == "FCB&FIRE")&(df["coTown"] == "Madrid")), "CompanyNameFinal"] = "FCB&FiRe Madrid"
# happiness brusselsf
    df.loc[((df["companyName"].str.contains("HAPPINESS", case = False)) & (df["Country"].str.contains("BELGIUM", case = False)))\
    , "CompanyNameFinal"] = "Happiness Brussels"
# happiness saigon
    df.loc[((df["companyName"].str.contains("Happiness", case = False)) & (df["Country"] == "VIETNAM"))\
    , "CompanyNameFinal"] = "Happiness Saigon"

#HelloFCB+ (formerly FCB Cape Town)
    df.loc[((df["companyName"].str.contains("HELLOFCB+", case =False)) | (df["companyName"].str.contains("FCB CAPE TOWN", case = False))), "CompanyNameFinal"] ="HelloFCB+"

#fcb company name ulka
    df.loc[(df["companyName"].str.contains("FCBULKA", case = False)), "CompanyNameFinal"] = "FCB Ulka"
#Horizon FCB Dubai
    df.loc[((df["companyName"] == "HORIZON FCB") | (df["companyName"].str.contains("FCB") & df["coTown"] == "Dubai")), "CompanyNameFinal"] ="Horizon FCB Dubai"
#ONEIGHTY - AN FCB ALLIANCE
    df.loc[(df["companyName"].str.contains("ONEIGHTY", case = False)), "CompanyNameFinal"] = "ONEIGHTY/FCB"

#fcb chicago/fcb new york
    df.loc[(df["companyName"].str.contains("FCB CHICAGO", case = False))
           &(df["Second Idea Company"].str.contains("FCB NEW YORK", case = False)),
           "CompanyNameFinal"] = "Chicago / New York FCB"
#excluding fcb new york from chicago
    df.loc[(df["companyName"].str.contains("FCB CHICAGO", case = False))
           &(df["Second Idea Company"]!= "FCB NEW YORK"),
           "CompanyNameFinal"] = "FCB CHICAGO"

#brand
    df.loc[(df["companyName"].str.contains("BRAND STATION", case = False)), "CompanyNameFinal"] = "BRAND STATION"
    print("end of fixing fcb")
    return df



def correctingVLMYR(df):
    listOfColumnsToCorrect = ["companyName", "coTown", "Country", "NetworkName"]

    for column in listOfColumnsToCorrect:
        df[column] = df[column].str.lstrip()
        df[column] = df[column].str.rstrip()

    df.loc[((df["companyName"] == "VML")
            |(df["companyName"] == "Y&R")
            | (df["companyName"] == "VMLY&R")
            )
    , "CompanyNameFinal"] = "VMLY&R "+df["coTown"]


    df.loc[((df["companyName"].str.contains("SCHOLZ & FRIENDS", case=False)))
           |((df["NetworkName"].str.contains("SCHOLZ & FRIENDS", case=False)))
    , "NetworkNameFinal"] = "VMLY&R"

    df.loc[(((df["companyName"].str.contains("SCHOLZ & FRIENDS", case=False))
           |(df["NetworkName"].str.contains("SCHOLZ & FRIENDS", case=False)))
            &(df["companyName"]!= "SCHOLZ & FRIENDS HAMBURG")
            )
    , "CompanyNameFinal"] = "SCHOLZ & FRIENDS " + df["coTown"]

    df.loc[(df["companyName"]== "SCHOLZ & FRIENDS HAMBURG")
    , "CompanyNameFinal"] = "SCHOLZ & FRIENDS Hamburg"


    df.loc[((df["companyName"]== "VMLY&R COMMERCE"))
    , "CompanyNameFinal"] = "VMLY&R COMMERCE "+df["coTown"]


    df.loc[((df["companyName"] == "PROLAM Y&R")), "CompanyNameFinal"] = "VMLY&R Santiago"
    df.loc[((df["companyName"] == "Y&R BRAZIL")), "CompanyNameFinal"] = "VMLY&R São Paulo"
    df.loc[((df["companyName"].str.contains("YVMLY&R BRAZIL", case= False))), "CompanyNameFinal"] = "VMLY&R São Paulo"
    df.loc[((df["CompanyNameFinal"].str.contains("YVMLY&R BRAZIL", case= False))), "CompanyNameFinal"] = "VMLY&R São Paulo"

    df.loc[((df["CompanyNameFinal"] == "YVMLY&R BRAZIL")), "CompanyNameFinal"] = "VMLY&R São Paulo"

    df.loc[((df["companyName"] == "VML")&(df["coTown"] == "Warsaw")), "CompanyNameFinal"] = "VMLY&R POLAND"


    df.loc[((df["companyName"] == "Y&R DUBAI")), "CompanyNameFinal"] = "VMLY&R Dubai"
    df.loc[((df["companyName"] == "Y&R MADRID")), "CompanyNameFinal"] = "VMLY&R MADRID"
    df.loc[((df["companyName"] == "Y&R MADRID")), "coTown"] = "Madrid"

    df.loc[((df["companyName"] == "Y&R PRAGUE")), "CompanyNameFinal"] = "VMLY&R PRAGUE"
    df.loc[((df["companyName"].str.contains("VMLY&R", case = False))& (df["coTown"] == "Prague")), "CompanyNameFinal"] = "VMLY&R PRAGUE"

    df.loc[((df["companyName"] == "Y&R PRAGUE")), "coTown"] = "PRAGUE"

    df.loc[((df["companyName"] == "Y&R ANZ")&(df["coTown"].str.contains( "Auckland", case = False))), "CompanyNameFinal"] = "VMLY&R Auckland"
    df.loc[((df["companyName"] == "Y&R ANZ")&(df["coTown"].str.contains( "MELBOURNE", case = False))), "CompanyNameFinal"] = "VMLY&R Melbourne"
    df.loc[((df["companyName"] == "VMLY&R MELBOURNE")), "CompanyNameFinal"] = "VMLY&R Melbourne"


    df.loc[((df["companyName"] == "Y&R NEW YORK")), "CompanyNameFinal"] = "VMLY&R NEW YORK"


    df.loc[((df["companyName"] == "Y&R ISTANBUL")), "CompanyNameFinal"] = "VMLY&R Istanbul"
    df.loc[((df["companyName"].str.contains( "VMLY&R ISTANBUL", case = False))), "CompanyNameFinal"] = "VMLY&R Istanbul"

    df.loc[((df["companyName"] == "DHÉLET VMLY&R")), "CompanyNameFinal"] = "DHELET VMLY&R"
    df.loc[((df["companyName"] == "DHÉLET Y&R")), "CompanyNameFinal"] = "DHELET VMLY&R"

    df.loc[((df["companyName"].str.contains( "Y&R LONDON", case = False))), "CompanyNameFinal"] = "VMLY&R London"
    df.loc[((df["companyName"] == "Y&R LONDON")), "coTown"] = "London"



    df.loc[((df["companyName"] == "Y&R PARIS")), "CompanyNameFinal"] = "VMLY&R Paris"
    df.loc[((df["companyName"] == "VMLY&R PARIS")), "CompanyNameFinal"] = "VMLY&R Paris"

    df.loc[((df["companyName"] == "VMLY&R PARIS")), "coTown"] = "PARIS"

    df.loc[((df["companyName"].str.contains("VMLY&R", case = False))& (df["coTown"] == "Lima")), "CompanyNameFinal"] = "VMLY&R LIMA"
    df.loc[((df["companyName"] == "VMLY&R LIMA")), "coTown"] = "Lima"

    df.loc[((df["companyName"] == "VMLY&R")& (df["coTown"] == "Istanbul")), "CompanyNameFinal"] = "VMLY&R Istanbul"
    df.loc[((df["companyName"] == "VMLY&R ISTANBUL")), "coTown"] = "Istanbul"

    df.loc[((df["companyName"].str.contains("VML", case = False))& (df["Country"] == "SOUTH AFRICA")), "CompanyNameFinal"] = "VMLY&R SOUTH AFRICA"


    df.loc[((df["companyName"] == "Y&R SOUTH AFRICA")), "CompanyNameFinal"] = "VMLY&R SOUTH AFRICA"
    #taxi
    df.loc[((df["companyName"] == "TAXI")&(df["coTown"] == "Montréal")), "CompanyNameFinal"] = "TAXI Montréal"
    df.loc[((df["companyName"] == "TAXI TORONTO")), "coTown"] = "TORONTO"
    df.loc[((df["companyName"] == "TAXI VANCOUVER")), "coTown"] = "VANCOUVER"
    df.loc[((df["companyName"] == "TAXI")&(df["coTown"] == "New York")), "CompanyNameFinal"] = "TAXI New York"
    df.loc[((df["companyName"] == "TAXI CANADA")&(df["coTown"] == "Toronto")), "CompanyNameFinal"] = "TAXI TORONTO"

    df.loc[((df["companyName"] == "VMLY&R MEXICO")), "CompanyNameFinal"] = "VMLY&R Mexico City"


    df.loc[((df["companyName"] == "THE CLASSIC PARTNERSHIP ADVERTISING")), "CompanyNameFinal"] = "THE CLASSIC PARTNERSHIP"


    df = df.groupby("CompanyNameFinal").filter((lambda x: (len(x) >= 30) | (len(x[x["Winner"].notnull()]) >= 1)))

    return df


def correctingWT(df):
    df["companyNameFinal"] = df["companyName"]

    df.loc[((df["companyName"] == "WUNDERMAN THOMPSON")
            |(df["companyName"] == "J. WALTER THOMPSON")
            |(df["companyName"] == "POSSIBLE")
            | (df["companyName"] == "WUNDERMAN")
            ), "CompanyNameFinal"] = "WUNDERMAN THOMPSON " +df["coTown"].str.upper()

    df.loc[((df["companyName"] == "SANTO")
           ), "CompanyNameFinal"] = "SANTO " + df["coTown"].str.upper()

    df.loc[((df["companyName"] == "SWIFT")
           ), "CompanyNameFinal"] = "SWIFT " + df["coTown"].str.upper()

    df.loc[((df["companyName"] == "MIRUM AGENCY")
            ), "CompanyNameFinal"] = "MIRUM"

    df.loc[((df["CompanyNameFinal"] == "MIRUM")
           ), "CompanyNameFinal"] = "MIRUM " + df["coTown"].str.upper()

    df.loc[((df["companyName"] == "J. WALTER THOMPSON ARGENTINA")
            |(df["companyName"] == "WUNDERMAN THOMPSON ARGENTINA")
            | (df["companyName"] == "WUNDERMAN CATO JOHNSON")
            ), "CompanyNameFinal"] = "WUNDERMAN THOMPSON BUENOS AIRES"

    df.loc[((df["companyName"] == "WUNDERMAN BRAZIL")
            |(df["companyName"] == "J. WALTER THOMPSON BRAZIL")
            ), "CompanyNameFinal"] = "WUNDERMAN THOMPSON SAO PAULO"

    df.loc[((df["companyName"] == "J. WALTER THOMPSON TAIWAN")
            ), "CompanyNameFinal"] = "WUNDERMAN THOMPSON TAIPEI"

    df.loc[((df["companyName"] == "J. WALTER THOMPSON COLOMBIA")
            ), "CompanyNameFinal"] = "WUNDERMAN THOMPSON BOGOTÁ"

    df.loc[((df["companyName"] == "J. WALTER THOMPSON COSTA RICA")
            ), "CompanyNameFinal"] = "WUNDERMAN THOMPSON SAN JOSE"

    df.loc[((df["companyName"] == "J. WALTER THOMPSON FOLK")
            |(df["companyName"] == "FOLK WUNDERMAN THOMPSON")
            ), "CompanyNameFinal"] = "WUNDERMAN THOMPSON DUBLIN"

    df.loc[(((df["companyName"] == "J. WALTER THOMPSON INDIA")
            |(df["companyName"] == "WUNDERMAN THOMPSON ")
            )&(df["coTown"].str.contains("Kolkata", case = False)))
            , "CompanyNameFinal"] = "WUNDERMAN THOMPSON KOLKATA"

    df.loc[(((df["companyName"] == "J. WALTER THOMPSON INDIA")
            )&df["coTown"].str.contains("Gurgaon", case = False))
            , "CompanyNameFinal"] = "WUNDERMAN THOMPSON GURGAON"


    df.loc[(((df["companyName"] == "J. WALTER THOMPSON INDIA")
            )&df["coTown"].str.contains("Mumbai", case = False))
            , "CompanyNameFinal"] = "WUNDERMAN THOMPSON MUMBAI"

    df.loc[((df["companyName"] == "J. WALTER THOMPSON ITALY")
            |(df["companyName"] == "WUNDERMAN THOMPSON ")
            &( df["coTown"] =="Milan")
            ), "CompanyNameFinal"] = "WUNDERMAN THOMPSON MILAN"


    df.loc[((df["companyName"] == "J. WALTER THOMPSON JAPAN")
            |(df["companyName"] == "WUNDERMAN THOMPSON ")
            &( df["coTown"] =="Tokyo")
            ), "CompanyNameFinal"] = "WUNDERMAN THOMPSON TOKYO"

    df.loc[((df["companyName"] == "J. WALTER THOMPSON MEXICO")
            |(df["companyName"] == "WUNDERMAN MEXICO")
            ), "CompanyNameFinal"] = "WUNDERMAN THOMPSON MEXICO CITY"

    df.loc[((df["companyName"] == "WUNDERMAN THOMPSON NEW ZEALAND")
            |(df["companyName"] == "J. WALTER THOMPSON NEW ZEALAND")
            ), "CompanyNameFinal"] = "WUNDERMAN THOMPSON AUCKLAND"


    df.loc[((df["companyName"] == "WUNDERMAN PHANTASIA")& (df["coTown"] =="Lima"))
        |((df["companyName"] == "J. WALTER THOMPSON PERU")& (df["coTown"] =="Lima"))
            , "CompanyNameFinal"] = "WUNDERMAN THOMPSON LIMA"

    df.loc[((df["companyName"] == "J. WALTER THOMPSON PUERTO RICO")
            ), "CompanyNameFinal"] = "WUNDERMAN THOMPSON SAN JUAN"

    df.loc[((df["companyName"] == "J. WALTER THOMPSON RUSSIA")
            ), "CompanyNameFinal"] = "WUNDERMAN THOMPSON MOSCOW"

    df.loc[((df["companyName"] == "WUNDERMAN THOMPSON ")& (df["coTown"] =="Bangkok")
            ), "CompanyNameFinal"] = "WUNDERMAN THOMPSON BANGKOK"

    df.loc[((df["companyName"] == "J. WALTER THOMPSON PHILIPPINES")& (df["coTown"] =="Makati City"))
        |((df["companyName"] == "WUNDERMAN THOMPSON ")& df["coTown"] =="Makati City")
            , "CompanyNameFinal"] = "WUNDERMAN THOMPSON MAKATI CITY"

    df.loc[((df["companyName"] == "MANAJANS/J. WALTER THOMPSON")& df["coTown"] =="Istanbul")
            , "CompanyNameFinal"] = "WUNDERMAN THOMPSON ISTANBUL"

    df.loc[((df["companyName"] == "WUNDERMAN DUBAI")
            ), "CompanyNameFinal"] = "WUNDERMAN THOMPSON DUBAI"

    df.loc[((df["companyName"] == "WUNDERMAN THOMPSON SPAIN")
            ), "CompanyNameFinal"] = "WUNDERMAN THOMPSON MADRID"



    df.loc[((df["companyName"] == "WUNDERMAN HEALTH")
            ), "CompanyNameFinal"] = "WUNDERMAN THOMPSON HEALTH"

    df.loc[((df["companyName"] == "WUNDERMAN MEXICO")
            ), "CompanyNameFinal"] = "WUNDERMAN THOMPSON MEXICO CITY"



    df['CompanyNameFinal'] = df['CompanyNameFinal'].str.replace('J. WALTER THOMPSON', 'WUNDERMAN THOMPSON')

    return df


def correctingDeloitte(df):

    df.loc[((df["companyName"].str.contains("DELOITTE", case = False) )
        |((df["NetworkName"].str.contains("DELOITTE", case = False) ))
           ), "NetworkNameFinal"] = "DELOITTE"
    return df

def correctingDroga(df):

    df.loc[((df["companyName"].str.contains("DROGA5", case = False) )
        |((df["NetworkName"].str.contains("DROGA5", case = False) ))
           ), "NetworkNameFinal"] = "DROGA5"
    return df

def correctingWeberShandwick(df):

    df.loc[((df["companyName"].str.contains("SHANDWICK", case = False) )
           ), "NetworkNameFinal"] = "WEBER SHANDWICK"
    return df

def correctingEdelmanComperers(df):
    df = correctingDroga(df)
    df = correctingDeloitte(df)
    df = correctingWeberShandwick(df)
    return df

def correctingEdelman(df):
    df.loc[((df["companyName"]== "EDELMAN")
            | (df["companyName"] == "ELAN EDELMAN")
            | (df["companyName"] == "EDELMAN DEPORTIVO")
            ), "CompanyNameFinal"] = "EDELMAN " +df["coTown"].str.upper()

    df.loc[((df["companyName"].str.contains( "ASSEMBLY", case = False))
            ), "CompanyNameFinal"] = "ASSEMBLY " +df["coTown"].str.upper()

    df.loc[((df["companyName"].str.contains( "REVERE", case = False))
            ), "CompanyNameFinal"] = "REVERE " +df["coTown"].str.upper()

    df.loc[((df["companyName"].str.contains( "EDIBLE", case = False))
            ), "CompanyNameFinal"] = "EDIBLE " +df["coTown"].str.upper()


    df.loc[((df["companyName"].str.contains("SALUTEM", case = False))
            ), "CompanyNameFinal"] = "SALUTEM " +df["coTown"].str.upper()

    df.loc[((df["CompanyNameFinal"].str.contains("EDELMAN", case = False))
            |(df["CompanyNameFinal"].str.contains("SALUTEM", case = False))
            | (df["CompanyNameFinal"].str.contains("ASSEMBLY", case=False))
            | (df["CompanyNameFinal"].str.contains("REVERE", case=False))
            | (df["CompanyNameFinal"].str.contains("EDIBLE", case=False))
            | (df["CompanyNameFinal"].str.contains("UNITED ENTERTAINMENT GROUP", case=False))

            ), "NetworkNameFinal"] = "EDELMAN"

    return df


def correctingMullenlowe(df):

    df.loc[((df["NetworkNameFinal"].str.contains("McCann", case = False))
            & (df["CompanyNameFinal"].str.contains("MARTIN AGENCY", case = False))
            ), "NetworkNameFinal"] = "MULLENLOWE GROUP"

    return df

def correctingTBWA(df):
    df.loc[((df["CompanyNameFinal"].str.contains("INTEGER", case=False))
            ), "CompanyNameFinal"] = "THE INTEGER GROUP "  +df["coTown"].str.upper()

    #df["CompanyNameFinal"] = df["CompanyNameFinal"].str.replace("\\\\", " ")
    df["CompanyNameFinal"] = df["CompanyNameFinal"].str.replace("\\", " ", regex = True)
    df["CompanyNameFinal"] = df["CompanyNameFinal"].str.replace("  ", " ")

    df.loc[((df["CompanyNameFinal"].str.contains("MEDIA ARTS LAB", case=False))
            ), "CompanyNameFinal"] = df["CompanyNameFinal"].str.upper() +" "+df["coTown"].str.upper()

    df.loc[((df["CompanyNameFinal"].str.contains("raad", case=False))
            ), "CompanyNameFinal"] = df["CompanyNameFinal"] +" " +df["coTown"].str.upper()

    df.loc[((df["CompanyNameFinal"].str.rstrip()=="TBWA HUNT LASCARIS")
            ), "CompanyNameFinal"] = df["CompanyNameFinal"] +" " +df["coTown"].str.upper()

    df.loc[((df["CompanyNameFinal"]=="TBWA GERMANY")
            ), "CompanyNameFinal"] = df["CompanyNameFinal"] +" " +df["coTown"].str.upper()

    df.loc[((df["CompanyNameFinal"].str.rstrip() =="HEIMAT")
            ), "CompanyNameFinal"] = "HEIMAT" +" " +df["coTown"].str.upper()

    df.loc[((df["CompanyNameFinal"].str.rstrip() =="HEIMAT ZÜRICH")
            ), "CompanyNameFinal"] = "HEIMAT ZURICH"

    df.loc[((df["CompanyNameFinal"]=="GRID WORLDWIDE")
            ), "CompanyNameFinal"] = df["CompanyNameFinal"] +" " +df["coTown"].str.upper()

    df.loc[((df["CompanyNameFinal"].str.rstrip()=="TBWA CHIAT DAY")
            ), "CompanyNameFinal"] = "TBWA CHIAT DAY" +" " +df["coTown"].str.upper()

#TO DO: 3 QUESTIONS THAT HAS BEEN ASKED IN JONATHANS CHANNEL



    return df


def addingAllCorrectingFunctions(df):
    df = correctingDroga(df)
    df = correctingDeloitte(df)
    df = correctingWeberShandwick(df)
    df = correctingTBWA(df)
    df = correctingMullenlowe(df)
    df = correctingEdelman(df)
    df = correctingWT(df)
    df = correctingVLMYR(df)
    df = correctingEdelmanComperers(df)
    return df