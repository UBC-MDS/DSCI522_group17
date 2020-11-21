# author: Chun Chieh Chang, Pan Fan, Sakshi Jain
# date: 2020-11-21

"""This is a script that will take a url that contains the data and save it at a user defined path from the root of where the script is ran
Usage: src/data_download.py --url=<url> --delim=<delim> --filepath=<filepath> --filename=<filename>

Options:
--url The url where the data is located
--delim Delimiter that separates the data
--filepath The user defined path to save the data, must end with `/`
--filenmae The user defined name to save the data, must end with the file format, i.e, .csv, .data
"""
import os
import pandas as pd
from docopt import docopt
import requests

opt = docopt(__doc__)


def main(url, delim, filepath, filename):
    # check if URL is valid
    try:
        req = requests.get(url)
    except Exception as error:
        print("Invalid URL, please enter a valid URL")
        raise

    data = pd.read_csv(url, delimiter=delim, engine="python")
    try:
        data.to_csv(filepath + filename, index=False)
    except:
        # create a new directory
        print("path does not exist, creating path...")
        os.makedirs(os.path.dirname(filepath))
        data.to_csv(filepath + filename, index=False)

    data.to_csv(filepath + filename, index=False)


if __name__ == "__main__":
    main(opt["--url"], opt["--delim"], opt["--filepath"], opt["--filename"])

