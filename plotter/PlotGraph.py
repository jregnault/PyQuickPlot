import matplotlib.pyplot as plt

class PlotGraph:

    def __init__(self, title="plot", x_label="", y_label=""):
        self.title = title
        self.x_label = x_label
        self.y_label = y_label

    def draw(self, data, format=""):
        plt.plot(data, format)
        plt.title(self.title)
        plt.xlabel(self.x_label)
        plt.ylabel(self.y_label)
        plt.show()
    
    def draw(self, dataX, dataY, format=""):
        plt.plot(dataX, dataY, format)
        plt.title(self.title)
        plt.xlabel(self.x_label)
        plt.ylabel(self.y_label)
        plt.show()