def getProducts(dataframe, message):
    j = 1
    for i in dataframe.index:
        message += str(j) + ". " + dataframe.loc[i, 'Item Brand'] + " - " + dataframe.loc[i, 'Item Name'] + " (" + dataframe.loc[i, 'Shade and/or Size'] + \
            ") (x" + dataframe.loc[i, '#'] + ") - " + dataframe.loc[i,
                                                                    'Price'] + " BDT (" + dataframe.loc[i, 'Adv.'] + " BDT advanced)"
        if (dataframe.loc[i, 'WC'] != ''):
            message += " " + dataframe.loc[i, 'WC'] + " (Weight charge)"
            message += "\n"
            j = j+1
    return message
