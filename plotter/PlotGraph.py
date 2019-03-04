import matplotlib.pyplot as plt

class PlotGraph:

    def __init__(self, title="plot", x_label="x", y_label="y"):
        self.title = title
        self.x_label = x_label
        self.y_label = y_label

    def draw(self, data, format="bo-"):
        plt.plot(data, format)
        plt.title(self.title)
        plt.xlabel(self.x_label)
        plt.ylabel(self.y_label)
        plt.show()