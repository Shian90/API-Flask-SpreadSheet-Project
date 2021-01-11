def getBatchesForMonth(dataframe, month):
    temp = dataframe[(dataframe['Shipment'] == month)]
    batches = temp['Batch'].unique()
    return batches
