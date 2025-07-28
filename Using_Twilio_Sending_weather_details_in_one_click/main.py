from twilio.rest import Client
import random
import json
from flask import Flask, render_template, request, flash
from space import people_space
from weather import get_weather
from char import get_char

app = Flask(__name__)
app.secret_key = "supersecretkey"

# Twilio credentials
account_sid = "ACdb2d97135d520fd2763883e07e1cb889"
auth_token = "32e40bce1c74b5edb09de0a133e4c76a"
client = Client(account_sid, auth_token)

# Database of students (testing with one number: not to spam others)
students = {
    "Manoj": {
        "name": "manoj",
        "number": "+16477793742",  
        "lucky": random.randint(1, 10),
        "location": "Sudbury"
    },
    "Leonel": {
        "name": "Leonel",
        "number": "+16477793742", 
        "lucky": random.randint(1, 10),
        "location": "Ottawa"
    },
    "Sanju": {
        "name": "Sanju",
        "number": "+16477793742",  
        "lucky": random.randint(1, 10),
        "location": "Vancouver"
    },
    "Jacob": {
        "name": "Jacob",
        "number": "+16477793742",  
        "lucky": random.randint(1, 10),
        "location": "Toronto"
    },
    "Gautam": {
        "name": "Gautam",
        "number": "+16477793742",  
        "lucky": random.randint(1, 10),
        "location": "Thiruvananthapuram"
    },
    "Bwendo": {
        "name": "Bwendo",
        "number": "+16477793742",  
        "lucky": random.randint(1, 10),
        "location": "London"
    },
    "Dany": {
        "name": "Dany",
        "number": "+16477793742",  
        "lucky": random.randint(1, 10),
        "location": "Douala"
    },
}

# Function to send SMS and log messages
def send_sms():
    log_messages = []
    for key, value in students.items():
        msg = (
            f'Hello {value["name"].title()} ! Welcome to BTA Connected Data 7300! '
            f'Your lucky number is {value["lucky"]}. '
            f'Did you know {people_space()} people are there in space? '
            f'The weather in {value["location"]} is {get_weather(value["location"])} DegC.'
            f'Random Harry Potter character: {get_char()}.')
        print(msg)

        # Send SMS via Twilio
        message = client.messages.create(
            body=msg,
            from_="+18284265943",  # Twilio number
            to=value["number"]  
        )
        # Log the message
        log_messages.append({
            "name": value["name"],
            "message": msg,
            "status": "Sent"
        })

    # Save logs to a JSON file
    with open("message_logs.json", "w") as log_file:
        json.dump(log_messages, log_file, indent=4)

    return "Messages sent and logged successfully!"


# Flask route for the homepage
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        result = send_sms()
        flash(result)
    return render_template("index.html")


app.run(host='0.0.0.0', port=81)
