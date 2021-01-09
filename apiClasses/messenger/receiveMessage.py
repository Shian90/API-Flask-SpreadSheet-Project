import random
from flask import Flask, request
from flask_restful import Resource, Api

from utils.messengerUtils.verifyFBToken import verify_fb_token
from utils.messengerUtils.sendMessage import send_message
from utils.messengerUtils.getMessage import get_message


class ReceiveMessage(Resource):
    def get(self):
        token_sent = request.args.get("hub.verify_token")
        return verify_fb_token(token_sent)

    def post(self):
        output = request.get_json()
        for event in output['entry']:
            messaging = event['messaging']
            for message in messaging:
                if message.get('message'):
                    recipient_id = message['sender']['id']
                    if message['message'].get('text'):
                        response_sent_text = get_message()
                        send_message(recipient_id, response_sent_text)
                    if message['message'].get('attachments'):
                        response_sent_nontext = get_message()
                        send_message(recipient_id, response_sent_nontext)
        return "Message Processed"
