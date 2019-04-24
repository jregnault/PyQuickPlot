# data management
# Jérémie Regnault
# 2019-03-25

import csv
import sys
import numpy as np

def readFromCSV(filename,separator):
        with open(filename, 'r') as file:
                return np.array([[float(e) for e in row] for row in csv.reader(file, delimiter=separator, quoting=csv.QUOTE_NONE)])

def readFromStdin():
        data = np.empty(1)
        while 1:
                line = np.fromstring(sys.stdin.readline())
                if line is None:
                        return data
                else:
                        data = np.concatenate(data, line)