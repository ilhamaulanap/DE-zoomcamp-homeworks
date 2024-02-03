import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

year = 2020
months = [10,11,12]

@data_loader
def load_data(*args, **kwargs):
    base_url = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/'

    # create an empty list to store DataFrames
    green_taxi_dataframes = []

    for month in months:
        file_name = f'green_tripdata_{year}-{month:02d}.csv.gz'
        url = base_url + file_name
        #taxi dtypes 
        taxi_dtypes = {
                        'VendorID':pd.Int64Dtype(),
                        'passenger_count': pd.Int64Dtype(),
                        'trip_distance': float,
                        'RatecodeID':pd.Int64Dtype(),
                        'store_and_fwd_flag':str,
                        'PULocationID':pd.Int64Dtype(),
                        'DOLocationID':pd.Int64Dtype(),
                        'Payment_type': pd.Int64Dtype(),
                        'fare_amount':float,
                        'extra':float,
                        'mta_tax':float,
                        'tip_amount':float,
                        'tolls_amount':float,
                        'improvement_surcharge':float,
                        'total_amount': float,
                        'congestion_surcharge':float
                        }
        
        #parse the columns to datetime
        parse_dates = ['lpep_pickup_datetime','lpep_dropoff_datetime']
        
        #read the compressed csv data
        green_taxi = pd.read_csv(url, sep=",", compression="gzip", dtype=taxi_dtypes, parse_dates=parse_dates)
        
        #append the green_taxi to dataframes
        green_taxi_dataframes.append(green_taxi)

    #combine the green_taxi_dataframes
    Q4_green_taxi = pd.concat(green_taxi_dataframes,ignore_index=True)

    return Q4_green_taxi


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
