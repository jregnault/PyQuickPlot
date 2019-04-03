import matplotlib.pyplot as plt
import pandas as pd

class PlotGraph:

    def __init__(self, title="plot", x_label="", y_label=""):
        self.title = title
        self.x_label = x_label
        self.y_label = y_label

    def draw(self, data, format="", output=""):
        plt.plot(data, format)
        plt.title(self.title)
        plt.xlabel(self.x_label)
        plt.ylabel(self.y_label)
        if output != "":
            plt.savefig(output)
        else:
            plt.show()