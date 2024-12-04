import pytest
import os
import subprocess
import pandas as pd
import sys
sys.path.append(os.path.abspath('./project'))

"""
This file contains all the fixture. Fixtures are resuable components which help to test the
implementation of advance data engineering pipeline, and etl implementation.
"""

@pytest.fixture
def test_url() -> str:
    return "http://example.com/test.csv"


@pytest.fixture
def execute_pipeline():
    subprocess.run(["python", "./project/pipeline.py"], check=True)


@pytest.fixture()
def delete_output_filePath():
    if os.path.exists("./data/UnequalGroundsDB.db"):
        os.remove("./data/UnequalGroundsDB.db")
    yield


@pytest.fixture
def test_data():
    test_df = pd.DataFrame({"Values": range(11)})
    return test_df


@pytest.fixture
def test_delete_data():
    columnToDelete = [1,6,10]
    return columnToDelete