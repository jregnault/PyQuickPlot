import matplotlib.pyplot as plt
import pandas as pd

class PlotGraph:

    def __init__(self, show_legend, title="plot", x_label="", y_label=""):
        self.title = title
        self.x_label = x_label
        self.y_label = y_label
        self._show_legend = show_legend

    def draw(self, data, format="", output=""):
        plt.plot(data, format)
        plt.title(self.title)
        plt.xlabel(self.x_label)
        plt.ylabel(self.y_label)
        if self._show_legend:
            plt.legend()
        if output != "":
            plt.savefig(output)
        else:
            plt.show()
