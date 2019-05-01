# data management
# Jérémie Regnault
# 2019-04-28

import csv
import sys
import numpy as np
import logging

class DataHandler(object):
        
    def readFromStream(self, filename, separator=""):
        if filename != None:
            file = open(filename)
        else:
            file = sys.stdin
        if separator != "":
            _data = np.array([[float(e) for e in row] for row in csv.reader(file, delimiter=separator, quoting=csv.QUOTE_NONE)])
        else:
            _data = np.array([[float(e) for e in row] for row in csv.reader(file, delimiter=" ", quoting=csv.QUOTE_NONE)])
        
        if filename is not None:
            file.close()

        return _data