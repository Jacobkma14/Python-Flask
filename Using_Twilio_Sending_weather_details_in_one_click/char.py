import urllib.request 
import json
import requests
import random

# Function to get a random Harry Potter character using HP API
def get_char():
    response = requests.get("https://hp-api.onrender.com/api/characters")
    characters = response.json()
    character = random.choice(characters)
    return character['name']