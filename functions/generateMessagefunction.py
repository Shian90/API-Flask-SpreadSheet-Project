from functions.makeMessagefunction import makeMessage


def generateMessage(dataframe):  # to be completed
    messages = []
    names = dataframe['Facebook Name'].unique()
    for name in names:
        finalDataframe = dataframe[(dataframe['Facebook Name'] == name)]
        messages.append(makeMessage(finalDataframe, name))

    return messages
