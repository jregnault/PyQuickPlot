import numpy as np

import PlotGraph as pg

class TestPlotGraph(object):
    def test_init(self):
        graph = pg.PlotGraph("title","x","y","legend")
        assert graph._title == "title"
        assert graph._x_label == "x"
        assert graph._y_label == "y"
        assert graph._legend == "legend"
    
    @pytest.mark.mpl_image_compare # flake8: noqa
    def test_drawOneLineInput(self):
        data = np.array([1,2,3])
        graph = pg.PlotGraph()
        graph.draw(data)
