# data management
# Jérémie Regnault

import csv
import pandas as pd

def importFromCSV(filename,separator):
    csvDataframe = pd.read_csv(filename,separator)
    if (len(csvDataframe.columns) > 1):
        dataX = csvDataframe[0]
        dataY = csvDataframe[1]
        return dataX, dataY