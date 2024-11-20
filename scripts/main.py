from get_data import *
from load_to_s3 import *


url = "https://restcountries.com/v3.1/all"
file_name = "data/raw.parquet"
bucket = "cde-raw-data"


def main():
    get_data()

    upload_to_s3(file_name=file_name, 
                 bucket_name=bucket, 
                 object_name="rawdata.parquet"
                 )


if __name__ == "__main__":
    main()