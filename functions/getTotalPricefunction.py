def getTotalPrice(dataframe):
    sum = 0
    for price in dataframe['Price']:
        sum += int(price)
    return int(sum)
