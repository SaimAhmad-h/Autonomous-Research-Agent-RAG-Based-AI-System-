from langchain.tools import tool
import pandas as pd

df = pd.read_csv("data/sensor_data.csv")

@tool
def check_sensor_data(query: str):
    """Returns sensor dataset"""
    return df.head(20).to_string()