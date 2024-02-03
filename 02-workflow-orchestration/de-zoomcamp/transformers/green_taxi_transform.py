if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):

    # Remove rows where passenger count is equal to 0 or trip distance is equal to 0
    data  = data[(data['passenger_count'] > 0) & (data['trip_distance'] > 0)]

    # Create a new column 'lpep_pickup_date' by converting 'lpep_pickup_datetime' to a date
    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date


    # Rename Columns
    data = data.rename(columns={
    'VendorID': 'vendor_id',
    'RateCodeID':'ratecode_id',
    'PULocationID' : 'pu_location_id',
    'DOLocationID' : 'do_location_id' 
    })

    return data



@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert all(output['vendor_id'].isin([1, 2])) 
    assert (output['passenger_count'] > 0).all()
    assert (output['trip_distance'] > 0).all()
