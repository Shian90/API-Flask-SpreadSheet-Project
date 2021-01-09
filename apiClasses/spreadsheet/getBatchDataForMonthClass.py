from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import json
import pandas as pd

from functions.getBatchDataForMonthfunction import getBatchDataForMonth
from functions.spreadsheetData.spreadsheetDatafunction import spreadsheetData
from functions.generateDataframefunction import generateDataframe


class GetBatchDataForMonth(Resource):
    def post(self):
        result = spreadsheetData()
        dataframe = generateDataframe(result)
        jsonData = request.get_json()
        month = jsonData["month"]
        batch = jsonData["batch"]
        dataframeData = getBatchDataForMonth(dataframe, batch, month)
        print(dataframeData)
        return pd.DataFrame(dataframeData).to_json(orient="split")
