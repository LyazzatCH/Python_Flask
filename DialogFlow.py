"""
Call from  PC (localhost): https://661a-2001-f40-909-3e31-b8be-35ea-54ac-4a93.ngrok-free.app -> http://localhost:5000
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def webhook():
    if request.method == 'GET':
        return 'Hello StringSyncBot! - Not connected to DF.'
    elif request.method == 'POST':
        payload = request.json
        user_response = payload['queryResult']['queryText']
        bot_response = generate_response()
        if user_response or bot_response != "":
            print('User: ' + user_response)
            print('Bot: ' + bot_response)
        response = {
            "fulfillmentMessages": [
                {
                    "text": {
                        "text": [bot_response]
                    }
                }
            ]
        }
        return jsonify(response)
    else:
        print(request.data)
    return "200"

def generate_response():
    current_time = datetime.now()
    hour = current_time.hour
    if 5 <= hour < 12:
        return "Good morning! I am StringSyncBot, how do you want me to address you?"
    elif 12 <= hour < 18:
        return "Good afternoon! I am StringSyncBot, how do you want me to address you?"
    else:
        return "Good evening! I am StringSyncBot, how do you want me to address you?"

if __name__ == '__main__':
    app.run(debug=True)"""

from flask import Flask, request, jsonify
from datetime import datetime
from pytz import timezone

app = Flask(__name__)

# Define the Singapore/Malaysia time zone
sg_time_zone = timezone('Asia/Singapore')

@app.route('/', methods=['POST', 'GET'])
def webhook():
    if request.method == 'GET':
        return 'Hello StringSyncBot! - Not connected to DF.'
    elif request.method == 'POST':
        payload = request.json
        user_response = payload['queryResult']['queryText']
        bot_response = generate_response(user_response)
        if user_response or bot_response != "":
            print('User: ' + user_response)
            print('Bot: ' + bot_response)
        response = {
            "fulfillmentMessages": [
                {
                    "text": {
                        "text": [bot_response]
                    }
                }
            ]
        }
        return jsonify(response)
    else:
        print(request.data)
    return "200"

def generate_response(user_response):
    # Get current time in Singapore/Malaysia time zone
    current_time = datetime.now(sg_time_zone)
    hour = current_time.hour
    if 5 <= hour < 12:
        greeting = "Good morning!"
    elif 12 <= hour < 18:
        greeting = "Good afternoon!"
    else:
        greeting = "Good evening!"

    if "picture" in user_response.lower() or "photo" in user_response.lower() or "image" in user_response.lower():
        image_path = os.path.join(os.getcwd(), "Dombyra_pic.jpg")
        return f"{greeting} Here is a picture of dombyra: {image_path}"
    else:
        return f"{greeting} I am StringSyncBot, What is your name?"

if __name__ == '__main__':
    app.run(debug=True)

