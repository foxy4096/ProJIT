import requests
import pprint
import json
import numpy
import os
from dotenv import load_dotenv
import pandas
load_dotenv()

AUTH_TOKEN = os.environ.get("KEY")
HEADERS = {"X-API-Key": f"{AUTH_TOKEN}"}

def get_zen():
    req = requests.get("https://vitary.pythonanywhere.com/api/zen", headers=HEADERS)
    pprint.pprint(req.json(), indent=2, compact=True)

for i in range(20):
    get_zen()