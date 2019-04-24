import argparse

import PlotGraph
import dataHandler

if __name__ == "__main__":
    # Parser creation
    parser = argparse.ArgumentParser(description="Create a figure from raw data.")

    # General options
    parser.add_argument('-v','--verbose', help='show more information about the execution.', action='store_true', default=False)
    parser.add_argument('-s', '--save', help='Save the figure in the given file. The extension defines the encoding used.', default="")

    # Graphs types
    parser.add_argument('-p','--plot', help='Create a plot figure', action='store_true', default=False)

    # Input options
    parser.add_argument('--csv', help='input and parse a csv file using the separator', nargs=2, metavar=('CSVFILE','SEPARATOR'), default=("",","))

    # Customization options
    parser.add_argument('-f','--format', help="data representation with MATLAB syntax", default="")
    parser.add_argument('-t','--title', help='set the title of the figure', default="")
    parser.add_argument('--xlabel', help='set the x axis label in the figure', default="")
    parser.add_argument('--ylabel', help='set the y axis label in the figure', default="")
    parser.add_argument('-l','--legend', help='show the legend in the figure', default="")

    args = parser.parse_args()

    # input retrieve
    if args.csv[0] != "":
        data = dataHandler.readFromCSV(args.csv[0],args.csv[1])
    else:
        data = dataHandler.readFromStdin()

    # figure creation
    fig = PlotGraph.PlotGraph(args.title, args.xlabel, args.ylabel, args.legend)
    fig.draw(data, args.format, args.save)
