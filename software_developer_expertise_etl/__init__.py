import logging
from io import BytesIO
import azure.functions as func
import pandas as pd


def main(inputBlob: func.InputStream):
    logging.info(f"Python blob trigger function processed blob \n"
                 f"Name: {inputBlob.name}\n"
                 f"Blob URI: {inputBlob.uri}\n"
                 f"Blob Size: {inputBlob.length} bytes")

    # logging.info(f"Readlines: \n")
    # print(inputBlob.readlines())

    blob_bytes = inputBlob.read()
    logging.info(f"Blob Size: {len(blob_bytes)} bytes")

    blob_data = BytesIO(blob_bytes)
    
    file_delimiter = ','
    df = pd.read_csv(blob_data, delimiter=file_delimiter)

    print(df)
    logging.info(df.head(5))
