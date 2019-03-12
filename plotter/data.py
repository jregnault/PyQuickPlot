# data management
# Jérémie Regnault

import csv
import numpy as np

def importFromCSV(filename,separator):
    data = np.empty([1,1])
    with open(filename, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=separator)
        for l in reader:
            np.reshape(data,[len(data),len(l)])
            np.append(data, np.asarray(l))