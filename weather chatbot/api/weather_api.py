
# ==========================================
# weather_api.py
# ==========================================

import requests
from datetime import datetime

# ==========================================
# OpenWeather API Configuration
# ==========================================

API_KEY = "your api key"

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


# ==========================================
# Get Complete Weather Data
# ==========================================


def get_weather(city):
    """
    Fetch complete weather information for a city.

    Parameters:
        city (str): Name of the city

    Returns:
        dict : Weather JSON data
        None : If city not found or request fails
    """




    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        return response.json()

    return None


# ==========================================
# Current Temperature
# ==========================================

def get_temperature(city):

    weather = get_weather(city)

    if weather:
        return weather["main"]["temp"]

    return None


# ==========================================
# Feels Like Temperature
# ==========================================

def get_feels_like(city):

    weather = get_weather(city)

    if weather:
        return weather["main"]["feels_like"]

    return None


# ==========================================
# Minimum Temperature
# ==========================================

def get_min_temperature(city):

    weather = get_weather(city)

    if weather:
        return weather["main"]["temp_min"]

    return None


# ==========================================
# Maximum Temperature
# ==========================================

def get_max_temperature(city):

    weather = get_weather(city)

    if weather:
        return weather["main"]["temp_max"]

    return None


# ==========================================
# Humidity
# ==========================================

def get_humidity(city):

    weather = get_weather(city)

    if weather:
        return weather["main"]["humidity"]

    return None


# ==========================================
# Pressure
# ==========================================

def get_pressure(city):

    weather = get_weather(city)

    if weather:
        return weather["main"]["pressure"]

    return None


# ==========================================
# Wind Speed
# ==========================================

def get_wind_speed(city):

    weather = get_weather(city)

    if weather:
        return weather["wind"]["speed"]

    return None


# ==========================================
# Wind Direction
# ==========================================

def get_wind_direction(city):

    weather = get_weather(city)

    if weather:
        return weather["wind"]["deg"]

    return None


# ==========================================
# Wind Gust
# ==========================================

def get_wind_gust(city):

    weather = get_weather(city)

    if weather:
        return weather["wind"].get("gust", "Not Available")

    return None


# ==========================================
# Visibility
# ==========================================

def get_visibility(city):

    weather = get_weather(city)

    if weather:
        return weather["visibility"]

    return None


# ==========================================
# Cloud Percentage
# ==========================================

def get_cloud_percentage(city):

    weather = get_weather(city)

    if weather:
        return weather["clouds"]["all"]

    return None


# ==========================================
# Weather Description
# ==========================================

def get_weather_description(city):

    weather = get_weather(city)

    if weather:
        return weather["weather"][0]["description"]

    return None


# ==========================================
# Rain Status
# ==========================================

def get_rain_status(city):

    weather = get_weather(city)

    if weather:
        return "Yes" if "rain" in weather else "No"

    return None


# ==========================================
# Snow Status
# ==========================================

def get_snow_status(city):

    weather = get_weather(city)

    if weather:
        return "Yes" if "snow" in weather else "No"

    return None


# ==========================================
# Sunrise Time
# ==========================================

def get_sunrise(city):

    weather = get_weather(city)

    if weather:
        timestamp = weather["sys"]["sunrise"]
        return datetime.fromtimestamp(timestamp).strftime("%H:%M:%S")

    return None


# ==========================================
# Sunset Time
# ==========================================

def get_sunset(city):

    weather = get_weather(city)

    if weather:
        timestamp = weather["sys"]["sunset"]
        return datetime.fromtimestamp(timestamp).strftime("%H:%M:%S")

    return None


# ==========================================
# Timezone
# ==========================================

def get_timezone(city):

    weather = get_weather(city)

    if weather:
        return weather["timezone"]

    return None


# ==========================================
# Complete Weather Data
# ==========================================

def get_complete_weather(city):

    weather = get_weather(city)

    if weather is None:
        return None

    return {

        "City": weather["name"],

        "Country": weather["sys"]["country"],

        "Temperature": weather["main"]["temp"],

        "Feels Like": weather["main"]["feels_like"],

        "Minimum Temperature": weather["main"]["temp_min"],

        "Maximum Temperature": weather["main"]["temp_max"],

        "Humidity": weather["main"]["humidity"],

        "Pressure": weather["main"]["pressure"],

        "Wind Speed": weather["wind"]["speed"],

        "Wind Direction": weather["wind"]["deg"],

        "Wind Gust": weather["wind"].get("gust", "Not Available"),

        "Visibility": weather["visibility"],

        "Cloud Percentage": weather["clouds"]["all"],

        "Description": weather["weather"][0]["description"],

        "Rain": "Yes" if "rain" in weather else "No",

        "Snow": "Yes" if "snow" in weather else "No",

        "Sunrise": datetime.fromtimestamp(
            weather["sys"]["sunrise"]
        ).strftime("%H:%M:%S"),

        "Sunset": datetime.fromtimestamp(
            weather["sys"]["sunset"]
        ).strftime("%H:%M:%S"),

        "Timezone": weather["timezone"]
    }


# ==========================================
# Test the File
# ==========================================

if __name__ == "__main__":

    city = input("Enter City Name: ")

    weather = get_complete_weather(city)

    if weather:

        print("\nWeather Information\n")

        for key, value in weather.items():
            print(f"{key} : {value}")

    else:
        print("City not found!") 