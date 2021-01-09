def getAdvance(dataframe):
    adv = 0
    for advance in dataframe['Adv.']:
        if (advance != ''):
            adv += int(advance)
    return int(adv)
