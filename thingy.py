import requests
import pprint
import json
import numpy
import os
from dotenv import load_dotenv
import pandas
load_dotenv()

AUTH_TOKEN = os.environ.get("KEY")
LIMIT = 10
HEADERS = {"X-API-Key": f"{AUTH_TOKEN}"}
req = requests.get("https://vitary.pythonanywhere.com/api/feed", headers=HEADERS, params={"limit": LIMIT})

# pprint.pprint(req.json())

vits = [i for i in json.loads(req.text).get("items")]


print(pandas.DataFrame(vits))