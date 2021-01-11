def getProducts(dataframe, message):
  j = 1
  for i in dataframe.index:
        brand = dataframe.loc[i, 'Item Brand']
        name = dataframe.loc[i, 'Item Name']
        specifics = ""
        advanced = ""
        if ( dataframe.loc[i, 'Shade and/or Size'] != "" ):
          specifics = " (" + dataframe.loc[i, 'Shade and/or Size'] + ")"
        else:
          specifics = ""
        if ( dataframe.loc[i, 'Adv.'] != ""):
          advanced = " (" + dataframe.loc[i, 'Adv.'] + " BDT advanced)"
        else:
          advanced = ""
        message+= str(j) + ". " + brand + " - " + name + specifics + " (x" + dataframe.loc[i, '#'] + ") - " + dataframe.loc[i, 'Price'] + " BDT" + advanced
        if ( dataframe.loc[i, 'WC'] != '' ):
          message += " - " + dataframe.loc[i, 'WC'] + " BDT (Weight charge)"
        message += "\n"
        j = j+1
  return message
