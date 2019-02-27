import argparse
import PlotGraph

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a figure from raw data.")

    parser.add_argument('-v','--verbose', help='show more information about the execution.', action='store_true', default=False)
    parser.add_argument('--plot', help='Create a plot figure', action='store_true')
    parser.add_argument('integers', help='a list of integers to plot', type=int, nargs='+')

    args = parser.parse_args()
    if(args.verbose):
        print("Verbose mode activated.")
    
    params = vars(args)
    print(params)

    if(args.verbose):
        print("Checking options")
    if(args.plot):
        plot = PlotGraph()
        plot.draw(args.integers)
