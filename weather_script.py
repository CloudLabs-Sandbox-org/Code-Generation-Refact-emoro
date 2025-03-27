import requests

def get_weather_data(city, api_key):
    """
    Fetch weather data from OpenWeatherMap API for a given city.
    """
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # Use "metric" for Celsius, "imperial" for Fahrenheit
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

def display_weather_info(weather_data):
    """
    Process and display weather information.
    """
    if weather_data:
        city = weather_data.get("name")
        country = weather_data["sys"].get("country")
        temperature = weather_data["main"].get("temp")
        humidity = weather_data["main"].get("humidity")
        weather_condition = weather_data["weather"][0].get("description")

        print("=" * 40)
        print(f"Weather in {city}, {country}")
        print("=" * 40)
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {weather_condition.capitalize()}")
        print("=" * 40)
    else:
        print("Unable to display weather information.")

def main():
    """
    Main function to get user input and fetch weather data.
    """
    print("Welcome to the Weather App!")
    api_key = input("c5d2ac0f1b978e9f90b03cc188d90142")

    while True:
        city = input("Enter the name of the city (or type 'exit' to quit): ")
        if city.lower() == "exit":
            print("Thank you for using the Weather App. Goodbye!")
            break

        weather_data = get_weather_data(city, api_key)
        display_weather_info(weather_data)

if __name__ == "__main__":
    main()