# ==========================================================
# response.py
# Generates chatbot responses
# ==========================================================

# Import intent prediction function
from chatbot.predict import predict_intent

# Import weather API functions
from api.weather_api import (
    get_temperature,
    get_feels_like,
    get_min_temperature,
    get_max_temperature,
    get_humidity,
    get_pressure,
    get_wind_speed,
    get_wind_direction,
    get_wind_gust,
    get_visibility,
    get_cloud_percentage,
    get_weather_description,
    get_rain_status,
    get_snow_status,
    get_sunrise,
    get_sunset,
    get_timezone
)


# ==========================================================
# Generate Chatbot Response
# ==========================================================

def get_response(user_input, city):
    """
    Predict the user's intent and return the appropriate
    weather response.

    Parameters
    ----------
    user_input : str
        User's question.

    city : str
        City name.

    Returns
    -------
    str
        Chatbot response.
    """

    # Predict intent
    intent, confidence = predict_intent(user_input)

    # -----------------------------
    # Unknown Intent
    # -----------------------------
    if intent == "unknown":
        return "Sorry, I couldn't understand your question."

    # -----------------------------
    # Current Temperature
    # -----------------------------
    elif intent == "current_temperature":

        temperature = get_temperature(city)

        if temperature is None:
            return f"Sorry, I couldn't find weather data for {city}."

        return f"The current temperature in {city} is {temperature}°C."

    # -----------------------------
    # Feels Like Temperature
    # -----------------------------
    elif intent == "feels_like_temperature":

        feels_like = get_feels_like(city)

        return f"It feels like {feels_like}°C in {city}."

    # -----------------------------
    # Minimum Temperature
    # -----------------------------
    elif intent == "minimum_temperature":

        temp = get_min_temperature(city)

        return f"The minimum temperature in {city} is {temp}°C."

    # -----------------------------
    # Maximum Temperature
    # -----------------------------
    elif intent == "maximum_temperature":

        temp = get_max_temperature(city)

        return f"The maximum temperature in {city} is {temp}°C."

    # -----------------------------
    # Humidity
    # -----------------------------
    elif intent == "humidity":

        humidity = get_humidity(city)

        return f"The current humidity in {city} is {humidity}%."

    # -----------------------------
    # Pressure
    # -----------------------------
    elif intent == "pressure":

        pressure = get_pressure(city)

        return f"The atmospheric pressure in {city} is {pressure} hPa."

    # -----------------------------
    # Wind Speed
    # -----------------------------
    elif intent == "wind_speed":

        speed = get_wind_speed(city)

        return f"The current wind speed in {city} is {speed} m/s."

    # -----------------------------
    # Wind Direction
    # -----------------------------
    elif intent == "wind_direction":

        direction = get_wind_direction(city)

        return f"The wind direction in {city} is {direction}°."

    # -----------------------------
    # Wind Gust
    # -----------------------------
    elif intent == "wind_gust":

        gust = get_wind_gust(city)

        return f"The wind gust in {city} is {gust} m/s."

    # -----------------------------
    # Visibility
    # -----------------------------
    elif intent == "visibility":

        visibility = get_visibility(city)

        return f"The visibility in {city} is {visibility} meters."

    # -----------------------------
    # Cloud Percentage
    # -----------------------------
    elif intent == "cloud_percentage":

        cloud = get_cloud_percentage(city)

        return f"The cloud coverage in {city} is {cloud}%."

    # -----------------------------
    # Weather Description
    # -----------------------------
    elif intent == "weather_description":

        description = get_weather_description(city)

        return f"The weather in {city} is {description}."

    # -----------------------------
    # Rain Status
    # -----------------------------
    elif intent == "rain_status":

        rain = get_rain_status(city)

        if rain == "Yes":
            return f"Yes, it is currently raining in {city}."

        return f"No, it is not raining in {city}."

    # -----------------------------
    # Snow Status
    # -----------------------------
    elif intent == "snow_status":

        snow = get_snow_status(city)

        if snow == "Yes":
            return f"Yes, it is currently snowing in {city}."

        return f"No, it is not snowing in {city}."

    # -----------------------------
    # Sunrise Time
    # -----------------------------
    elif intent == "sunrise_time":

        sunrise = get_sunrise(city)

        return f"Today's sunrise time in {city} is {sunrise}."

    # -----------------------------
    # Sunset Time
    # -----------------------------
    elif intent == "sunset_time":

        sunset = get_sunset(city)

        return f"Today's sunset time in {city} is {sunset}."

    # -----------------------------
    # Timezone
    # -----------------------------
    elif intent == "local_timezone":

        timezone = get_timezone(city)

        return f"The timezone offset for {city} is {timezone} seconds from UTC."

    # -----------------------------
    # Default
    # -----------------------------
    return "Sorry, something went wrong."
    
    
# ==========================================================
# Test response.py
# ==========================================================

if __name__ == "__main__":

    print("=" * 50)
    print("Weather Chatbot")
    print("=" * 50)

    city = input("Enter city name: ")

    while True:

        question = input("\nYou: ")

        if question.lower() == "exit":
            print("Goodbye!")
            break

        response = get_response(question, city)

        print("\nBot:", response)