import argparse
import PlotGraph

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a figure from raw data.")

    # General options
    parser.add_argument('-v','--verbose', help='show more information about the execution.', action='store_true', default=False)

    # Graphs types
    graphGroup = parser.add_mutually_exclusive_group()
    graphGroup.add_argument('-p','--plot', help='Create a plot figure', action='store_true', default=False)

    # Input options
    # parser.add_argument('integers', help='a list of integers to plot', type=int, nargs='+')
    parser.add_argument('--csv', help='input and parse a csv file using the separator', nargs=2, metavar=('CSVFILE','SEPARATOR'))

    # Customization options
    parser.add_argument('-f','--format', help="data representation with MATLAB syntax", default="")
    parser.add_argument('-t','--title', help='set the title of the figure', default="")
    parser.add_argument('--xlabel', help='set the x axis label in the figure', default="")
    parser.add_argument('--ylabel', help='set the y axis label in the figure', default="")

    args = parser.parse_args()
    if(args.verbose):
        print("Verbose mode activated.")
        params = vars(args)
        print(params)

    if(args.verbose):
        print("Checking graph type")
    if(args.plot):
        plot = PlotGraph.PlotGraph(args.title, args.xlabel, args.ylabel)
        if(args.verbose):
            print("Drawing figure.")
        if(args.format != ""):
            plot.draw(args.integers, args.format)
        else:
            plot.draw(args.integers)
    if(args.verbose):
        print("Closing.")