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

from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.linear_model import LogisticRegression, Ridge
from sklearn.model_selection import (
    GridSearchCV,
    RandomizedSearchCV,
    cross_validate,
    train_test_split,
)


if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")

opt = docopt(__doc__)



def main(input_file,output_file):

    # read train_df.csv
    train = pd.read_csv(input_file)
 

    #create split the train_df
    X_train, y_train = train.drop(columns=["quality_level"]), train["quality_level"]
  

    classifiers = {
        "Logistic Regression": LogisticRegression(),
        "Logistic Regression (balanced)": LogisticRegression(class_weight="balanced"),
        "Random Forest": RandomForestClassifier(),
        "Random Forest (balanced)": RandomForestClassifier(class_weight="balanced"),
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
        return pd.DataFrame(results_df)



    res = score_with_metrics(
        classifiers,
        scoring=["accuracy", "f1", "recall", "precision", "average_precision", "roc_auc"],
)


    try:
        res.to_csv(output_file, index = True)
    except:
        os.makedirs(os.path.dirname(output_file))
        res.to_csv(output_file, index = True)
    

if __name__ == "__main__":
    main(opt["<input_file>"], opt["<output_file>"])
