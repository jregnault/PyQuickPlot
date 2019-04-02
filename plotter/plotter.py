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
    #parser.add_argument('integers', help='a list of integers to plot', type=int, nargs='+')
    parser.add_argument('--csv', help='input and parse a csv file using the separator', nargs=2, metavar=('CSVFILE','SEPARATOR'), default=("",","))

    # Customization options
    parser.add_argument('-f','--format', help="data representation with MATLAB syntax", default="")
    parser.add_argument('-t','--title', help='set the title of the figure', default="")
    parser.add_argument('--xlabel', help='set the x axis label in the figure', default="")
    parser.add_argument('--ylabel', help='set the y axis label in the figure', default="")

    args = parser.parse_args()

    # input retrieve
    if args.verbose:
        print("Parsing CSV file")
    if args.csv[0] != "":
        data = dataHandler.importFromCSV(args.csv[0],args.csv[1])

    # figure creation
    if(args.verbose):
        print("Checking graph type")
    if(args.plot):
        fig = PlotGraph.PlotGraph(args.title, args.xlabel, args.ylabel)
        if(args.verbose):
            print("Drawing figure.")
        fig.draw(data, args.format, args.save)
    if(args.verbose):
        print("Closing.")
