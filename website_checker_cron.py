import requests as req


client = req.session()

url = "https://www.vbcvjsr.in/"
is_working = False

try:
    with client.get(url=url, headers={"REASON": "NEED TO CHECK IF YOUR WEBSITE IS WORKING OR NOT."}) as response:
        print(response.ok)
        is_working = response.ok
except Exception as e:
    print(e)

