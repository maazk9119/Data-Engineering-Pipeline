from pathlib import Path
import sqlite3
import pandas as pd

"""
Loads dataframe into database -sqlite
Args:
    table: Define the table name.
    df: dataframe store into database
Return: None
"""
def load_data_to_sqlitedb(table, df) -> None:
    db_name = Path("./data/UnequalGroundsDB.db")
    conn = sqlite3.connect(db_name)
    df.to_sql(table, conn, if_exists="replace", index=False)
    conn.close()