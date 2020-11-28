"""Create train_df and test_df files .

Usage: src/eda_figs.py <input_file> <output_file> <output_file1> <output_file2>

Options:
<input_file>     Path (including filename) to data file
<output_file>    Path (including filename) of where to locally save fig1
<output_file1>   Path (including filename) of where to locally save fig2
<output_file2>   Path (including filename) of where to locally save fi3

"""

from docopt import docopt
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys

if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")

opt = docopt(__doc__)



def main(input_file, output_file,output_file1,output_file2):

    # read train_df.csv
    data= pd.read_csv(input_file)
    #create box plot
    fig, ax=plt.subplots(ncols=6, nrows=2, figsize=(30, 12))
    index=0
    ax=ax.flatten()
    for col, value in data.drop(['quality_level', 'wine_type'], axis=1).items():
        sns.boxplot(y=col, data=data, ax=ax[index])
        index+=1
    plt.tight_layout(pad=0.5, w_pad=0.7)
    # save box plot
    plt.savefig(output_file)


    # creat density plot
    fig, ax=plt.subplots(ncols=6, nrows=2, figsize=(30, 12))
    index=0
    ax=ax.flatten()

    for col, value in data.drop(['quality_level', 'wine_type'], axis=1).items():
        sns.distplot(value, ax=ax[index])
        index+=1

    plt.tight_layout(pad=0.5, w_pad=0.7)
    # save density plot
    plt.savefig(output_file1)

    # creat correlation plot
    wine_pairplot = sns.pairplot(data.drop('wine_type', axis = 1), hue="quality_level")
    # save correlation plot
    wine_pairplot.savefig(output_file2)

if __name__ == "__main__":
    main(opt["<input_file>"], opt["<output_file>"], opt["<output_file1>"],opt["<output_file2>"])
