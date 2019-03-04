import argparse
import PlotGraph

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a figure from raw data.")

    parser.add_argument('-v','--verbose', help='show more information about the execution.', action='store_true', default=False)
    parser.add_argument('-p','--plot', help='Create a plot figure', action='store_true', default=False)
    parser.add_argument('integers', help='a list of integers to plot', type=int, nargs='+')
    parser.add_argument('-f','--format', help="data representation with MATLAB syntax", default="")
    parser.add_argument('-t','--title', help='set the title of the figure', default="figure")

    args = parser.parse_args()
    if(args.verbose):
        print("Verbose mode activated.")
        params = vars(args)
        print(params)

    if(args.verbose):
        print("Checking graph type")
    if(args.plot):
        plot = PlotGraph.PlotGraph(args.title)
        if(args.format != ""):
            plot.draw(args.integers, args.format)
        else:
            plot.draw(args.integers)
