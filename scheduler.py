import time
from main import run_pipeline

def schedule_pipeline(interval=3600):
    while True:
        run_pipeline()  # Run the entire pipeline
        time.sleep(interval)  # Wait for the specified interval (in seconds)
