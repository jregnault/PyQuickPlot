import argparse
import sys
import logging

import PlotGraph as pg
import DataHandler as dh

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

    if args.verbose:
        # logging config
        LOG_FORMAT = "[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s"
        LOG_LEVEL = logging.DEBUG
        logging.basicConfig(format=LOG_FORMAT, level=LOG_LEVEL)

    __input_file = None
    __input_separator = ""

    # input retrieve
    logging.info("Retrieving data")
    if args.csv[0] != "":
        __input_file = args.csv[0]
        __input_separator = args.csv[1]
    
    data = dh.readFromStream(__input_file, __input_separator)
    logging.debug(f'data = {data}')
    logging.debug(f'data length = {len(data)}')

    # figure creation
    logging.info("Creating figure")
    fig = pg.PlotGraph(args.title, args.xlabel, args.ylabel, args.legend)
    logging.info("drawing figure")
    fig.draw(data, args.format, args.save)
