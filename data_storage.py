import sqlite3

def create_table():
    conn = sqlite3.connect('weather_data.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS weather
                      (city TEXT, temperature REAL, humidity INTEGER, pressure INTEGER, weather TEXT, date TEXT)''')
    conn.commit()
    conn.close()

def insert_weather_data(df):
    conn = sqlite3.connect('weather_data.db')
    df.to_sql('weather', conn, if_exists='append', index=False)
    conn.commit()
    conn.close()
