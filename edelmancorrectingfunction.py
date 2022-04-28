
def correctingEdelmanCreative(df, companynamecolumn, companynamefinalcolumn, networknamecolumn):
    df.loc[((df[companynamecolumn]== "EDELMAN")
            | (df[companynamecolumn] == "ELAN EDELMAN")
            | (df[companynamecolumn] == "EDELMAN DEPORTIVO")
            ), companynamefinalcolumn] = "EDELMAN " +df["coTown"].str.upper()

    df.loc[((df[companynamecolumn].str.contains( "ASSEMBLY", case = False, na=False))
            ), companynamefinalcolumn] = "ASSEMBLY " +df["coTown"].str.upper()

    df.loc[((df[companynamecolumn].str.contains( "REVERE", case = False, na=False))
            ), companynamefinalcolumn] = "REVERE " +df["coTown"].str.upper()

    df.loc[((df[companynamecolumn].str.contains( "EDIBLE", case = False, na=False))
            ), companynamefinalcolumn] = "EDIBLE " +df["coTown"].str.upper()


    df.loc[((df[companynamecolumn].str.contains("SALUTEM", case = False, na=False))
            ), companynamefinalcolumn] = "SALUTEM " +df["coTown"].str.upper()

    df.loc[((df[companynamefinalcolumn].str.contains("EDELMAN", case = False, na=False))
            |(df[companynamefinalcolumn].str.contains("SALUTEM", case = False, na=False))
            | (df[companynamefinalcolumn].str.contains("ASSEMBLY", case=False, na=False))
            | (df[companynamefinalcolumn].str.contains("REVERE", case=False, na=False))
            | (df[companynamefinalcolumn].str.contains("EDIBLE", case=False, na=False))
            | (df[companynamefinalcolumn].str.contains("UNITED ENTERTAINMENT GROUP", case=False, na=False))

            ), networknamecolumn] = "EDELMAN"

    return df
