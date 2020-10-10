#!/usr/bin/env python3
import vonage
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/webhooks/answer")
def answer_call():
    ncco = [
        {
            "action": "talk",
            "text": "Hi, we will shortly forward your call. This call is recorded for quality assurance purposes."
        },
        {
            "action": "record",
            "split" : "conversation",
            "channels" : 2,
            "eventUrl": ["https://demo.ngrok.io/webhooks/recordings"]
        },
        {
            "action": "connect",
            "eventUrl": ["https://demo.ngrok.io/webhooks/event"],
            "from": "VONAGE_NUMBER",
            "endpoint": [
                {
                    "type": "phone",
                    "number": "RECIPIENT_NUMBER"
                }
            ]
        }
    ]
    return jsonify(ncco)

@app.route("/webhooks/recordings", methods=['POST'])
def recordings():
    data = request.get_json()
    pprint(data)
    return "Webhook received"

if __name__ == '__main__':
    app.run(port=3000)
