from flask import Flask, request, jsonify
from flask_restful import Resource, Api

from functions.spreadsheetData.spreadsheetDatafunction import spreadsheetData
from functions.generateDataframefunction import generateDataframe
from functions.getBatchDataForMonthfunction import getBatchDataForMonth
from functions.invoicesfunction import generateInvoices


class GenerateInvoices(Resource):
    def post(self):
        result = spreadsheetData()
        dataframe = generateDataframe(result)
        jsonData = request.get_json()
        month = jsonData["month"]
        batch = jsonData["batch"]
        dataframeData = getBatchDataForMonth(dataframe, batch, month)
        generateInvoices(dataframeData)
        return 201
