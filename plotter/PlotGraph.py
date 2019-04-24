import matplotlib.pyplot as plt
import pandas as pd

class PlotGraph:

    def __init__(self, title="plot", x_label="", y_label="", legend=""):
        self._title = title
        self._x_label = x_label
        self._y_label = y_label
        self._legend = legend

    def draw(self, data, format="", output=""):
        plt.plot(data, format)
        plt.title(self._title)
        plt.xlabel(self._x_label)
        plt.ylabel(self._y_label)
        if self._legend != "":
            plt.legend([self._legend])
        if output != "":
            plt.savefig(output)
        else:
            plt.show()
