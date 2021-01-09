from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import pandas as pd
import numpy as np

from functions.getBatchesForMonthfunction import getBatchesForMonth
from functions.spreadsheetData.spreadsheetDatafunction import spreadsheetData
from functions.generateDataframefunction import generateDataframe


class GetBatches(Resource):
    def post(self):
        result = spreadsheetData()
        dataframe = generateDataframe(result)
        month = request.get_json()
        batches = getBatchesForMonth(dataframe, month["month"])
        print(pd.Series(batches).to_json(orient='values'))
       # return jsonify(np.ndarray.tolist(batches))
        return jsonify(pd.Series(batches).to_json(orient='values'))
