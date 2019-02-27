import matplotlib.pyplot as plt

class PlotGraph:

    def __init__(self, title="plot", x_label="", y_label=""):
        self.title = title
        self.x_label = x_label
        self.y_label = y_label
    
    def drawFigure(self, data, format):
        
        plt.plot(data, format)
        plt.show()