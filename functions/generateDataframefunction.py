import pandas as pd
import numpy as np


def generateDataframe(spreadsheetFetchResults):
    data = spreadsheetFetchResults['values']

    numRows = len(data)

      numCols = len(data[0])

      for i in range(1, numRows):
        if ( len(data[i]) < 25 ):
          for j in range(numCols-len(data[i])):
            data[i].append("n/a")


      columns = []
      datarows = np.empty([numRows-1, numCols], dtype = object)

      for column in data[0]: # column names
        columns.append(column.strip())

      for i in range(numRows):
        if i == 0:
          continue
        else:
          for j in range(numCols):
            datarows[i-1][j] = data[i][j]

    dataframe = pd.DataFrame(data=datarows, columns=columns)
    for index in range(len(dataframe)):
        dataframe.loc[index, 'Facebook Name'] = " ".join(
            dataframe.loc[index, 'Facebook Name'].split())

    return dataframe
