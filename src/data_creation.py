# Author: Pan Fan, Chun Chieh Chang, Sakshi Jain
# Date: 2020/11/27
"""Create train_df and test_df files .

Usage: src/data_creation.py <input_file> <input_file2> <output_file> <output_file2>

Options:
<input_file>     Path (including filename) to data file
<input_file2>    Path (including filename) to data file
<output_file>    Path (including filename) of where to locally create train_df
<output_file2>   Path (including filename) of where to locally create test_df
"""

import os
from docopt import docopt
import pandas as pd
from sklearn.model_selection import train_test_split

opt = docopt(__doc__)

def main(input_file, input_file2,output_file,output_file2):

    # read in two datasets, one for redwine, one for whitewine
    data_red= pd.read_csv(input_file)
    #cleaning data
    data_red = data_red.rename(columns=lambda x: x.replace(" ","_"))

    #creating levels for 'quality_level' column
    data_red['quality_level'] = ["Excellent" if x >= 7 else "Good" if x >= 5 else "Bad" for x in data_red['quality']]
    data_red['wine_type']= "red"


    data_white = pd.read_csv(input_file2)
    #cleaning data
    data_white = data_white.rename(columns=lambda x: x.replace(" ","_"))

    #creating levels for 'quality_level' column
    data_white['quality_level'] = ["Excellent" if x >= 7 else "Good" if x >= 5 else "Bad" for x in data_white['quality']]
    data_white['wine_type']= "white"

    #merging red wine and white wine data set
    full_data = pd.concat([data_white, data_red], axis=0)
    full_data = full_data.drop('quality', axis = 1)

    train_df, test_df = train_test_split(full_data, test_size=0.25, random_state=2020)

    try:
        train_df.to_csv(output_file, index = False)
    except:
        os.makedirs(os.path.dirname(output_file))
        train_df.to_csv(output_file, index = False)

    try:
        test_df.to_csv(output_file2, index = False)
    except:
        os.makedirs(os.path.dirname(output_file2))
        test_df.to_csv(output_file2, index = False)


if __name__ == "__main__":
    main(opt["<input_file>"], opt["<input_file2>"], opt["<output_file>"],opt["<output_file2>"])