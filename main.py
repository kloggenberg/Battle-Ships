from data_extraction import fetch_weather_data
from data_transformation import transform_weather_data
from data_storage import create_table, insert_weather_data
from config import DEFAULT_CITY

def run_pipeline():
    # Step 1: Fetch the weather data
    weather_data = fetch_weather_data(DEFAULT_CITY)

    # Step 2: Transform the data
    weather_df = transform_weather_data(weather_data)

    # Step 3: Store the data
    if weather_df is not None:
        create_table()
        insert_weather_data(weather_df)

if __name__ == "__main__":
    run_pipeline()
