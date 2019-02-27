import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a figure from raw data.")
    parser.add_argument('-v','--verbose', help='show more information about the execution.', action='store_true', default=False)
    parser.add_argument('--plot', help='Create a plot figure', action='store_true')
    args = parser.parse_args()

    if(args.verbose):
        print("Verbose mode activated.")
    