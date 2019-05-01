import sys

import numpy as np
import DataHandler as dh

class TestDataHandler(object):
    def test_readFromStreamWithFile(self):
        _expected = np.array([[1,2,3],[4,5,6]])
        _data = dh.DataHandler.readFromStream("./tests/simple_test.csv",',')
        for exp, act in zip(_expected, _data):
            assert list(exp) == list(act)
    
    def test_readFromStreamWithStdin(self):
        sys.stdin = open("./tests/simple_test.csv")
        _expected = np.array([[1,2,3],[4,5,6]])
        _data = dh.DataHandler.readFromStream(None, "")
        for exp, act in zip(_expected, _data):
            assert list(exp) == list(act)