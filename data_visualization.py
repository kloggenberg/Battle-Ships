import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

def plot_temperature_trend():
    # Reconnect to the database and load data
    conn = sqlite3.connect('weather_data.db')
    df = pd.read_sql('SELECT * FROM weather', conn)
    conn.close()

    # Plot temperature trend
    plt.figure(figsize=(10,6))
    plt.plot(pd.to_datetime(df['date']), df['temperature'], marker='o')
    plt.title(f"Temperature Trend in {df['city'][0]}")
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
