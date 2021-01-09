from flask import Flask, request
from flask_restful import Resource, Api


def send_message(recipient_id, response):
   # bot.send_text_message(recipient_id, response)
    return "success"
