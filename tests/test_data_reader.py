#testing the data reader function
from src.ingestion.data_reader import read_data

def read_data_test():
    df = read_data("data/raw/file_name.csv") #reads the data.
    assert df is not None and len(df) > 0 #make sure the dataframe exist and is not empty.