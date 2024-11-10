import pandas as pd
from typing import List, Dict, Any

"""
Delete the colums from the dataframe.
    Args:
        df: original dataframe extracted from CSV.
        columns: Column list needs to eradicate from df.
    Return:
        Transformed the dataframe.
"""
def delete_columns(df: pd.DataFrame, columns: List[str]) -> pd.DataFrame:
    return df.drop(columns=columns, errors="ignore")

"""
Drop rows contain null values.
    Args:
        df: step1: transformed dataframe.
    Return:
        step2 : transformed dataframe.
"""
def drop_null_rows(df: pd.DataFrame) -> pd.DataFrame:
    return df.dropna()

"""
Execute the sequence of tranformation on dataframe.
    Args:
        df: original dataframe from CSV.
        config: configuration with respect to data.
    Return:
        Final transformed dataframe.
"""
def apply_defined_transformation(df, config) -> pd.DataFrame:
    print("Transforming started......")
    #step 1 : Remove unncessary columns.
    df_transformed = delete_columns(df, config['columns_to_delete'])
    #step 2 : Filtered redudant data.
    df_transformed = drop_null_rows(df_transformed)
    print("Transforming completed......")
    return df_transformed