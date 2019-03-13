# data management
# Jérémie Regnault

import csv
import pandas as pd

def importFromCSV(filename,separator):
    return pd.read_csv(filename,separator)
            