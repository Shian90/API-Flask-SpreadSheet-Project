def getTotalPrice(dataframe):
    sum = 0
    for price in dataframe['Price']:
        if ( price != '' ):
            sum += int(price)
    return int(sum)
