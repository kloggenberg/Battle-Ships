import pandas as pd
from datetime import datetime

def transform_weather_data(weather_data):
    if weather_data:
        weather_info = {
            'city': weather_data['name'],
            'temperature': weather_data['main']['temp'],
            'humidity': weather_data['main']['humidity'],
            'pressure': weather_data['main']['pressure'],
            'weather': weather_data['weather'][0]['description'],
            'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        # Convert to DataFrame for easier manipulation
        return pd.DataFrame([weather_info])
    else:
        print("No data to transform")
        return None
