# data management
# Jérémie Regnault
# 2019-04-28

import csv
import sys
import numpy as np

def readFromStream(filename,separator=""):
        if filename is not None:
                file = open(filename, 'r')
        else:
                file = sys.stdin
        if separator != "":
                __data = np.array([[float(e) for e in row] for row in csv.reader(file, delimiter=separator, quoting=csv.QUOTE_NONE)])
        else:
                __data = np.array([[float(e) for e in row] for row in csv.reader(file, quoting=csv.QUOTE_NONE)])

        if filename is not None:
                file.close()

        return __data