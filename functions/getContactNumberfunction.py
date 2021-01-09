def getContactNumber(dataframe):
    contactNumber = ""
    for i in dataframe.index:
        if(dataframe.loc[i, 'Number'][0] == "0"):
            contactNumber = dataframe.loc[i, 'Number'].strip()
            break
    return contactNumber
