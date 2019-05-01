import sys

import numpy as np
import DataHandler as dh

class TestDataHandler(object):
    def test_readFromStreamWithFile(self):
        dataH = dh.DataHandler()

        _expected = np.array([[1,2,3],[4,5,6]])
        _data = dataH.readFromStream("./tests/simple_test.csv",',')
        for exp, act in zip(_expected, _data):
            assert list(exp) == list(act)
    
    def test_readFromStreamWithStdin(self):
        sys.stdin = open("tests/simple_test.csv")
        dataH = dh.DataHandler()

        _expected = np.array([[1,2,3],[4,5,6]])
        _data = dataH.readFromStream(None, "")
        for exp, act in zip(_expected, _data):
            assert list(exp) == list(act)