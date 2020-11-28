# Author: Pan Fan, Chun Chieh Chang, Sakshi Jain
# Date: 2020/11/27
"""Compare the performance of different classifier .

Usage: src/eda_figs.py <input_file> <output_file>

Options:
<input_file>     Path (including filename and file extension) to transformed train file
<output_file>   Path (including filename and file extension) to training result file
"""

from docopt import docopt
import pandas as pd
import sys
import os

from sklearn.dummy import DummyClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import (
    cross_validate
)
from joblib import dump, load

if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")

opt = docopt(__doc__)



def main(input_file,output_file):

    # read train_df.csv
    train = pd.read_csv(input_file)
 

    # create split the train_df
    X_train, y_train = train.drop(columns=["quality_level"]), train["quality_level"]
  
    
    # define classifiers
    classifiers = {
        "Logistic_Regression": LogisticRegression(),
        "Random_Forest": RandomForestClassifier(),
    "DummyClassifier": DummyClassifier(),
    "SVC" : SVC(),
    "K_Nearest_Neighbors": KNeighborsClassifier()
    }


    def score_with_metrics(models, scoring="accuracy"):
        """
        Return cross-validation scores for given models as a dataframe.

        Parameters
        ----------
        models : dict
            a dictionary with names and scikit-learn models
        scoring : list/dict/string
            scoring parameter values for cross-validation

        Returns
        ----------
            None

        """
        results_df = {}
        for (name, model) in models.items():
            clf = model
            scores = cross_validate(
                clf, X_train, y_train, return_train_score=True, scoring=scoring
            )
            df = pd.DataFrame(scores)
            results_df[name] = df.mean()
            clf.fit(X_train, y_train)
            # save the model
            dump(clf, 'results/'+name+'.joblib')
        return pd.DataFrame(results_df)



    res = score_with_metrics(classifiers)

    # saving the results table 
    try:
        res.to_csv(output_file, index = True)
    except:
        os.makedirs(os.path.dirname(output_file))
        res.to_csv(output_file, index = True)
    

if __name__ == "__main__":
    main(opt["<input_file>"], opt["<output_file>"])
