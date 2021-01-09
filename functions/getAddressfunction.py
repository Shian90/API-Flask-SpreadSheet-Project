def getAddress(dataframe):
    address = ""
    for i in dataframe.index:
        if(dataframe.loc[i, 'Address'] != ""):
            address = dataframe.loc[i, 'Address'].strip()
            break
    return address
