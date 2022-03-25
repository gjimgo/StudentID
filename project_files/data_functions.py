"""
It has only function which will be used to read data from an Excel file.
"""

import pandas as pd
from .constants import DATA_FILE


def get_data():
    return pd.read_excel(DATA_FILE)
