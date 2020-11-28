# Author: Pan Fan, Chun Chieh Chang, Sakshi Jain
# Date: 2020/11/27
"""Create transformed train and test files .

Usage: src/eda_figs.py <input_file> <input_file1> <output_file> <output_file1>

Options:
<input_file>     Path (including filename and file extension) to train file
<input_file1>    Path (including filename and file extension) to test file
<output_file>   Path (including filename and file extension) to transformed train file
<output_file1>   Path (including filename and file extension) to transformed test file

"""

from docopt import docopt
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys
from sklearn.compose import ColumnTransformer, TransformedTargetRegressor, make_column_transformer
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder, StandardScaler


if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")

opt = docopt(__doc__)



def main(input_file, input_file1, output_file,output_file1):

    # read train_df.csv
    train = pd.read_csv(input_file)
    test = pd.read_csv(input_file1)

    #create split the train_df
    X_train, y_train = train.drop(columns=["quality_level"]), train["quality_level"]
    X_test, y_test = test.drop(columns=["quality_level"]), test["quality_level"]

    # categorize the features

    numeric_features = ["fixed_acidity", "volatile_acidity", "citric_acid", "residual_sugar", "chlorides", "free_sulfur_dioxide", "total_sulfur_dioxide", "density", "pH", "sulphates", "alcohol"]
    binary_features = ['wine_type']
    target = ['quality_level']

    # make preprocessor
    preprocessor = make_column_transformer(
    (StandardScaler(), numeric_features),
    (OneHotEncoder(handle_unknown="error", drop="if_binary"), binary_features))

    # transform data
    preprocessor.fit(X_train)
    col = numeric_features + list(preprocessor.named_transformers_["onehotencoder"].get_feature_names())
    X_train_pp = preprocessor.transform(X_train)
    X_test_pp = preprocessor.transform(X_test)

    # create transformed test and train data

    transformed_train = pd.DataFrame(X_train_pp, index = X_train.index , columns = col)
    train_pp = pd.concat([transformed_train, y_train], axis=1)
    transformed_test = pd.DataFrame(X_test_pp, index = X_test.index , columns = col)
    test_pp = pd.concat([transformed_test, y_test], axis=1)

    try:
        train_pp.to_csv(output_file, index = False)
        test_pp.to_csv(output_file1, index = False)
    except:
        os.makedirs(os.path.dirname(output_file))
        train_pp.to_csv(output_file, index = False)
        test_pp.to_csv(output_file1, index = False)

    

if __name__ == "__main__":
    main(opt["<input_file>"], opt["<input_file1>"], opt["<output_file>"],opt["<output_file1>"])
