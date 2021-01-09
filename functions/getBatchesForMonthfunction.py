def getBatchesForMonth(dataframe, month):
    temp = dataframe[(dataframe['Shipment'] == month)
                     & (dataframe['Batch'] != 'CGM')]
    batches = temp['Batch'].unique()
    return batches
