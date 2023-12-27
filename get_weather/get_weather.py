import requests
from datetime import datetime, timedelta

def get_weather(self, zipcode: int):
    """
    Gets the current weather from the internet. Set heartbeat = True and send_message the results.
    
    Args:
        zipcode (int):  The zip-code for the desired area
        
    Returns:
        str: Weather results in plain text with urls
    """
    
    def get_weather_data():
                
        api_key = "YOUR-API-KEY"
        base_url = "https://api.openweathermap.org/data/2.5/weather"

        params = {
            "zip": str(zipcode),
            "APPID": api_key,
            "mode": "json",
            "units": "imperial"
        }

        try:
            response = requests.get(base_url, params=params)
            response.raise_for_status()
            weather_data = response.json()
            return weather_data
        except requests.exceptions.RequestException as e:
            print(f"Error making the API request: {e}")
            return None

    def convert_to_est(timestamp_utc):
        utc_time = datetime.utcfromtimestamp(timestamp_utc)
        est_time = utc_time - timedelta(hours=5)  # Eastern Standard Time (EST) offset
        return est_time.strftime("%Y-%m-%d %I:%M:%S %p")

    def format_weather_output(weather_data):

        if not weather_data:
            return "Failed to retrieve weather data."
        
        radar_map = "https://radar.weather.gov/station/KMLB/standard"
        forecast = "https://openweathermap.org/city/4175437"
        
        formatted_output = (
            f"City: {weather_data['name']}\n"
            f"Temperature: {weather_data['main']['temp']} °F\n"
            f"Description: {weather_data['weather'][0]['description']}\n"
            f"Humidity: {weather_data['main']['humidity']}%\n"
            f"Wind Speed: {weather_data['wind']['speed']} mph\n"
            f"Pressure: {weather_data['main']['pressure']} hPa\n"
            f"Visibility: {weather_data['visibility']} meters\n"
            f"Cloudiness: {weather_data['clouds']['all']}%\n"
            f"Sunrise: {convert_to_est(weather_data['sys']['sunrise'])}\n"
            f"Sunset: {convert_to_est(weather_data['sys']['sunset'])}\n"
            f"Radar: {radar_map}\n"
            f"Forecast: {forecast}\n"
    )
        return formatted_output
        
    weather_data = get_weather_data()
    output = format_weather_output(weather_data)
    # print(output)
    return output
