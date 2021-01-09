from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import numpy as np
import pandas as pd

from functions.spreadsheetData.spreadsheetDatafunction import spreadsheetData
from functions.generateDataframefunction import generateDataframe
from functions.getMonthsfunction import getMonths


class GetMonths(Resource):
    def get(self):
        result = spreadsheetData()
        dataframe = generateDataframe(result)
        months = getMonths(dataframe)
        print(months)
        return pd.Series(months).to_json(orient='values'), 200
