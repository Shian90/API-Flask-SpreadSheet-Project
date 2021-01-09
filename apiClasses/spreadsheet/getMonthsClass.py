from flask import Flask, request, jsonify
from flask_restful import Resource, Api

from functions.spreadsheetData.spreadsheetDatafunction import spreadsheetData
from functions.generateDataframefunction import generateDataframe
from functions.getMonthsfunction import getMonths


class GetMonths(Resource):
    def get(self):
        result = spreadsheetData()
        dataframe = generateDataframe(result)
        months = getMonths(dataframe)
        print(jsonify({"months": months}))
        return jsonify({"months": months}), 200
