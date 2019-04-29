import numpy as np
import DataHandler as dh

class DataHandlerTest(object):
    def test_readFromStreamWithFile(self):
        _expected = np.array([[1,2,3][4,5,6]])
        _data = dh.DataHandler.readFromStream("simple_test.csv",',')
        assert _expected == _data