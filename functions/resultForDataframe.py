from functions.generateDataframefunction import generateDataframe

global resultToPass


def resultForDataframe(result):
    global resultToPass
    resultToPass = result
    return result


def getResult():
    return resultToPass
