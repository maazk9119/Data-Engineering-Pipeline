import requests
import pandas as pd
from io import StringIO

"""
Extract a CSV file from a given URL
Args: 
    Url: CSV file download url.
Return: Dataframe
"""
def get_dataframe(url: str) -> pd.DataFrame:
    response = requests.get(url)
    response.raise_for_status()
    data = StringIO(response.text)
    df = pd.read_csv(data)
    return df