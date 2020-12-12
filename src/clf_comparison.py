# Author: Pan Fan, Chun Chieh Chang, Sakshi Jain
# Date: 2020/11/27
"""Compare the performance of different classifier and train the best model given cross_validate results .

Usage: src/clf_comparison.py <input_file> <input_file1> <output_file> <output_file1>

Options:
<input_file>     Path (including filename and file extension) to transformed train file
<input_file1>    Path (including filename and file extension) to transformed test file
<output_file>   Path (including filename and file extension) to cross validate result file
<output_file1>   Path (including filename and file extension) to store untuned model predictions
"""
#import packages
from docopt import docopt
import pandas as pd
import sys
import os
import numpy as np
from sklearn.dummy import DummyClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import (
    cross_validate,
    GridSearchCV,
    RandomizedSearchCV
)
from joblib import dump, load
from sklearn.metrics import f1_score, make_scorer
if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")

opt = docopt(__doc__)



def main(input_file, input_file1, output_file, output_file1):
    

    # read train_df.csv
    train = pd.read_csv(input_file)
    test = pd.read_csv(input_file1)
 

    # create split the train_df
    X_train, y_train = train.drop(columns=["quality_level"]), train["quality_level"]
    X_test, y_test = test.drop(columns=["quality_level"]), test["quality_level"]
  
    # check if target folder exists
    try:
        os.makedirs(os.path.dirname(output_file))
    except FileExistsError:
        pass
    # define classifiers
    classifiers = {
        "Logistic_Regression": LogisticRegression(random_state = 123, class_weight = 'balanced'),
        "Random_Forest": RandomForestClassifier(random_state = 123, class_weight = 'balanced'),
    "DummyClassifier": DummyClassifier(random_state = 123),
    "SVC" : SVC(random_state = 123, class_weight = 'balanced'),
    "K_Nearest_Neighbors": KNeighborsClassifier()
    }
    f1 = make_scorer(f1_score, average = 'weighted', labels = ['Excellent'])

    def score_with_metrics(models, scoring=f1):
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
    res = res.transpose()
    best_model = res.idxmax()['test_score']
    best_clf = classifiers[best_model]
    best_clf.fit(X_train, y_train)
    pred = best_clf.predict(X_test)
    test_scores = f1_score(y_test, pred, average = 'weighted', labels = ['Excellent'])
    best_score = pd.DataFrame({'Model': [best_model], 'Test_Score':[test_scores]})
    res.to_csv(output_file, index = True)
    best_score.to_csv(output_file1, index = False)
    
    # perform hyperparameter tuning on two of the best models
    param_RF = {'n_estimators':[int(i) for i in np.linspace(start = 100, stop = 1000, num = 10).tolist()],
           'max_depth':[int(i) for i in np.linspace(start = 10, stop = 1000, num = 100).tolist()]}
    param_log = {
    "C": [0.0001, 0.001, 0.01, 0.1, 1.0, 10, 100, 1000]}
    
    rf_search = RandomizedSearchCV(classifiers['Random_Forest'],
                                       param_RF, cv = 5,
                                       n_jobs = -1,
                                       scoring = f1,
                                       n_iter = 20, random_state = 123)
    
    log_search = GridSearchCV(classifiers['Logistic_Regression'],
                                       param_log, cv = 5,
                                       n_jobs = -1,
                                       scoring = f1
                                       )
    rf_search.fit(X_train, y_train)
    log_search.fit(X_train, y_train)
    rf_best = rf_search.best_estimator_
    log_best = log_search.best_estimator_
    tuned_results = {}
    rf_score = cross_validate(rf_best, X_train, y_train, return_train_score=True, scoring=f1)
    log_score = cross_validate(log_best, X_train, y_train, return_train_score=True, scoring=f1)
    tuned_results['Random Forest'] = pd.DataFrame(rf_score).mean()
    tuned_results['Logistic Regression'] = pd.DataFrame(log_score).mean()
    tuned_results = pd.DataFrame(tuned_results).transpose()
    tuned_results.to_csv('results/tuned_cv_results.csv', index = True)
    rf_best.fit(X_train, y_train)
    dump(rf_best, 'results/Bestrfmodel.joblib')
    pred = rf_best.predict(X_test)
    best_f1 = f1_score(y_test, pred, average = 'weighted', labels = ['Excellent'])
    best_tuned_model_test = pd.DataFrame({'Model': ['Random Forest'], 'Test_Score':[best_f1]})
    best_tuned_model_test.to_csv('results/best_tuned_model.csv', index = False)
    
    
    
    

    
    

if __name__ == "__main__":
    main(opt["<input_file>"], opt["<input_file1>"], opt["<output_file>"], opt["<output_file1>"])
