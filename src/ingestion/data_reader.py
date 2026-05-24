import pandas as pd
from src.utils.logger import logger

#Function that will read the dataset
def read_data(path):
    try:
        logger.info(f"Reading data from {path}")
        df = pd.read_csv(path)
        logger.info(f"Data reading completed. Size of data {df}")
        return df

    except Exception as e:
        logger.info(f"Can't read data: {e}")
        raise