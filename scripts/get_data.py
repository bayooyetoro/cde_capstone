import requests
import pandas as pd
import logging


logging.basicConfig(level=logging.INFO)
API_URL = "https://restcountries.com/v3.1/all"


def get_data():
    try:
        logging.info("Fetching data from API...")
        response = requests.get(API_URL)
        response.raise_for_status()
        data = response.json()
        logging.info("Data fetched successfully.")

        df = pd.json_normalize(data, sep='_')
        logging.info("Converting raw data to Parquet format...")
        df.to_parquet("./data/raw.parquet", engine="pyarrow", index=False)
        logging.info("Parquet format saved successfully")


    except Exception as e:
        logging.error(f"Error in data extraction: {e}")