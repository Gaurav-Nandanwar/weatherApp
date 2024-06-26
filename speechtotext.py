import requests
import json
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

city = input("Enter the name of the city: ")
url = f"https://api.weatherbit.io/v2.0/forecast/daily?city={city}&key=97c840ccd9574c22a7a8b0d4f32ff844"
r = requests.get(url)

# Check if the request was successful
if r.status_code == 200:
    wdic = json.loads(r.text)
    # Access the first element in the data list
    if "data" in wdic and len(wdic["data"]) > 0:
        app_max_temp = wdic["data"][0]["app_max_temp"]
        print(f"The apparent maximum temperature of {city} is {app_max_temp}°C")
        # Speak the temperature
        speak(f"The apparent maximum temperature of {city} is {app_max_temp} degrees Celsius")
    else:
        error_message = "No weather data available"
        print(error_message)
        speak(error_message)
else:
    error_message = "Error fetching weather data"
    print(error_message)
    speak(error_message)
