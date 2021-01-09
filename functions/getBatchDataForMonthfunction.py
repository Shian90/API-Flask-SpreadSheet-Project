def getBatchDataForMonth(dataframe, batch, month):
    temp = dataframe[(dataframe['Shipment'] == month)
                     & (dataframe['Batch'] == batch)]
    return temp
