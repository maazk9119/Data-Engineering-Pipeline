from fixtures import(test_data, test_delete_data)
from etl import transform as t

def test_delete_columns(test_data):
    transformed_df= t.delete_columns(test_data, test_delete_data)
    #assert 'C' not in transformed_df, "column C is not deleted"
    assert 1 not in transformed_df, "1 is not deleted"
    assert 6 not in transformed_df, "6 is not deleted"
    assert 10 not in transformed_df, "10 is not deleted"