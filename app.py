from __future__ import print_function
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2 import service_account
from flask import Flask, request
from flask_restful import Resource, Api
from pymessenger.bot import Bot

from functions.spreadsheetData.spreadsheetDatafunction import spreadsheetData
from functions.resultForDataframe import resultForDataframe
from apiClasses.messenger.receiveMessage import ReceiveMessage
from utils.messengerUtils.verifyFBToken import verify_fb_token

from apiClasses.spreadsheet.getMonthsClass import GetMonths
from apiClasses.spreadsheet.getBatchesClass import GetBatches
from apiClasses.spreadsheet.getBatchDataForMonthClass import GetBatchDataForMonth
from apiClasses.spreadsheet.generateMessageClass import GenerateMessage
from apiClasses.spreadsheet.generateInvoicesClass import GenerateInvoices

import pickle
import os.path
import pandas as pd
import numpy as np
import math

import random


app = Flask(__name__)
api = Api(app)

# messenger bot
ACCESS_TOKEN = 'ACCESS_TOKEN'
VERIFY_TOKEN = 'VERIFY_TOKEN'
bot = Bot(ACCESS_TOKEN)

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of a sample spreadsheet.
# Take as user input?
SAMPLE_SPREADSHEET_ID = '1xl0OP_IhryWg4eXU5F8K6GoFVDKe0gpdNo5u13WjLlI'
SAMPLE_RANGE_NAME = 'Sheet1!A1:Z1000'

# just need to redefine this
SERVICE_ACCOUNT_FILE = 'cherie-notebook-cred.json'

spreadsheetData()


# API calls
api.add_resource(ReceiveMessage, '/message')
api.add_resource(GetMonths, '/months')
api.add_resource(GetBatches, '/batches')
api.add_resource(GetBatchDataForMonth, '/batchdata')
api.add_resource(GenerateMessage, '/generatemessage')
api.add_resource(GenerateInvoices, '/generateinvoices')


if __name__ == '__main__':
    app.run(debug=True)
