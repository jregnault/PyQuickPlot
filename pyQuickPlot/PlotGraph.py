import matplotlib.pyplot as plt

class PlotGraph(object):

    def __init__(self, title="plot", x_label="", y_label="", legend=""):
        self._title = title
        self._x_label = x_label
        self._y_label = y_label
        self._legend = legend

    def draw(self, data, format=""):
        if len(data) == 1:
            plt.plot(data[0], format)
        else:
            plt.plot(data, format)
        plt.title(self._title)
        plt.xlabel(self._x_label)
        plt.ylabel(self._y_label)
        if self._legend != "":
            plt.legend([self._legend])
    
    def show(self, output=""):
        if output != "":
            plt.savefig(output)
        else:
            plt.show()