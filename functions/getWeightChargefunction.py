import re


def getWeightCharge(dataframe):
    wc = 0
    for val in dataframe['WC']:
        if (val != '' and re.search('[a-zA-Z]+', val) == None):
            wc += int(val)
    return int(wc)
