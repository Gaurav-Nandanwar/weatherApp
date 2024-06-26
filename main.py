import requests
import json


city = input("Enter the name of the city: ")

# Properly construct the URL with the city query parameter
url = f"https://api.weatherbit.io/v2.0/forecast/daily?city={city}&key=97c840ccd9574c22a7a8b0d4f32ff844"

r = requests.get(url)
print(r.text)
wdic = json.loads(r.text)
print(wdic["data"][0]["app_max_temp"])


