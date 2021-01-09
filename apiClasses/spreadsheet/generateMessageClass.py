from flask import Flask, request, jsonify
from flask_restful import Resource, Api

from functions.getBatchDataForMonthfunction import getBatchDataForMonth
from functions.spreadsheetData.spreadsheetDatafunction import spreadsheetData
from functions.generateDataframefunction import generateDataframe
from functions.generateMessagefunction import generateMessage

import json


class GenerateMessage(Resource):
    def post(self):
        result = spreadsheetData()
        dataframe = generateDataframe(result)
        jsonData = request.get_json()
        month = jsonData["month"]
        batch = jsonData["batch"]
        dataframeData = getBatchDataForMonth(dataframe, batch, month)
        messages = generateMessage(dataframeData)
        print(messages)
        return json.dumps(messages), 200
