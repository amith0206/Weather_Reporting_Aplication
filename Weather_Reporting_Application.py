import requests

import speech_recognition as sr

import pyttsx3 as pd


# Initialize the text-to-speech engine
engine = pd.init()

# Function to convert text to speech
def text_to_speech(text):
    engine.say(text)
    engine.runAndWait()

# WeatherAPI endpoint and API key
url = "https://api.weatherapi.com/v1/current.json"
api_key = "992f3386be2c4b1687085857230106"

#Function to turn speech to text
def say():
    r = sr.Recognizer()
    with sr.Microphone(device_index=None) as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            location = r.recognize_google(audio)
            return location # Return the recognized location
        except Exception as e:
            print("Error: " + str(e))


# City or location for which you want to fetch weather
text_to_speech("Please say your city name")
location = say()

# Request parameters
params = {
    "key": api_key,
    "q": location
}

# Send GET request to the API
response = requests.get(url, params=params)

# Parse the JSON response
data = response.json()

# Extract and display weather information
if "error" in data:
    print("Error:", data["error"]["message"])
    text_to_speech("Sorry no matching location found")
else:
    # Location and current temperature
    print("Location:", data["location"]["name"])
    location="Location:", data["location"]["name"]
    
    print("Temperature:", data["current"]["temp_c"], "°C")
    temperature="Temperature:", data["current"]["temp_c"], "degree celcius"
    
    print("Condition:", data["current"]["condition"]["text"])
    condition="Condition:", data["current"]["condition"]["text"]
    
    print("Wind:", data["current"]["wind_kph"], "km/h")
    wind="Wind:", data["current"]["wind_kph"], "kilo meters per hour"
    
    print("Humidity:", data["current"]["humidity"], "%")
    humidity="Humidity:", data["current"]["humidity"], "%"
    
    
    text_to_speech("Weather Report")
    text_to_speech(location)
    text_to_speech(temperature)
    text_to_speech(condition)
    text_to_speech(wind)
    text_to_speech(humidity)
    text_to_speech("Thank you for your time")
