# Author: Pan Fan, Chun Chieh Chang, Sakshi Jain
# Date: 2020/11/27
"""Create train_df and test_df files .

Usage: src/eda.py <input_file> <output_file> <output_file1> <output_file2> <output_file3>

Options:
<input_file>     Path (including filename) to data file
<output_file>    Path (including filename) of where to locally save fig1
<output_file1>   Path (including filename) of where to locally save fig2
<output_file2>   Path (including filename) of where to locally save fig3
<output_file3>   Path (including filename) of where to locally save fig4

"""

from docopt import docopt
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import os
if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")

opt = docopt(__doc__)



def main(input_file, output_file,output_file1,output_file2, output_file3):

    # read train_df.csv
    data= pd.read_csv(input_file)
    y_train = data['quality_level']
    
    #create dist_plot
    sns.set(font_scale=2)
    fig, ax=plt.subplots(ncols=6, nrows=2, figsize=(30, 12))
    index=0
    ax=ax.flatten()
    for col, value in data.drop(['quality_level', 'wine_type'], axis=1).items():
        sns.boxplot(y=col, data=data, ax=ax[index])
        index+=1
    plt.tight_layout(pad=0.5, w_pad=0.7)
    # save box plot
    try:
        plt.savefig(output_file)
    except:
        os.makedirs(os.path.dirname(output_file))
        plt.savefig(output_file)


    # creat density plot
    fig, ax=plt.subplots(ncols=6, nrows=2, figsize=(30, 12))
    sns.set(font_scale=1.5)
    index=0
    ax=ax.flatten()
    train = data
    for col, value in data.drop(['quality_level', 'wine_type'], axis=1).items():
        sns.kdeplot(data = train, x = train[col], hue ='quality_level', ax=ax[index])
        index+=1
    fig.delaxes(ax[11])
    plt.tight_layout(pad=0.5, w_pad=0.7)
    # save density plot
    plt.savefig(output_file1)

    # creat correlation plot
    wine_pairplot = sns.pairplot(data.drop('wine_type', axis = 1), hue="quality_level")
    # save correlation plot
    wine_pairplot.savefig(output_file2)
    plt.figure()
    # create class_dist plot
    sns.set(rc={'figure.figsize':(5,5)})
    class_dist = sns.countplot(x = 'quality_level', data=pd.DataFrame(y_train))
    class_dist.figure.savefig(output_file3)

if __name__ == "__main__":
    main(opt["<input_file>"], opt["<output_file>"], opt["<output_file1>"],opt["<output_file2>"], opt["<output_file3>"])
