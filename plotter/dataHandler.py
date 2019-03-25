# data management
# Jérémie Regnault
# 2019-03-25

import csv
import numpy as np

def importFromCSV(filename,separator):
        with open(filename, 'r') as file:
                return np.array([[float(e) for e in row] for row in csv.reader(file, delimiter=separator, quoting=csv.QUOTE_NONE)])
