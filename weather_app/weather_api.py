import requests
from config import API_KEY, CITIES

class WeatherAPI:
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

    def get_weather_data(self):
        weather_data = []
        for city in CITIES:
            params = {
                'q': city,
                'appid': API_KEY,  # Use your API key here
                'units': 'metric'  # Get the temperature in Celsius
            }
            try:
                print(f"Fetching weather data for {city}...")
                response = requests.get(self.BASE_URL, params=params)
                response.raise_for_status()  # Check if the request was successful
                weather_data.append(response.json())
            except requests.exceptions.RequestException as e:
                print(f"Error fetching data for {city}: {e}")
        return weather_data