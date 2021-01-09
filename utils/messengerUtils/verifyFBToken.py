from flask import Flask, request


def verify_fb_token(token_sent):
    if token_sent == 'VERIFY_TOKEN':
        return request.args.get("hub.challenge")
    return 'Invalid verification token'
