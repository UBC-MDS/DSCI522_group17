# Wine Quality Prediction (DSCI522_group17)
Group work for DSCI522 Our group  number is 17

Date: 11/20/2020

Team members: Pan Fan, Chun Chieh Chang and Sakshi Jain

GitHub repository: https://github.com/UBC-MDS/DSCI522_group17

### Introduction

As somebody said that “Life is too short to drink bad wine.”, we decided to work on the wine dataset so that we can help in determining the quality of wine via its chemical composition.

Dataset: The data set used in this project is sourced from the UCI Machine Learning Repository and can be found [here](https://archive.ics.uci.edu/ml/datasets/Wine+Quality). Two datasets are included and one is for red wine while the other is for white wine. We will merge these two datasets together and create a new column `type of wine` to represent the wine type for each observation. In addition, we will group the quality of wine into three categories and they are "Bad", "Good", and "Excellent". In total, we have 12 predictors and one output variable.

Predictors:
1.	fixed acidity
2.	volatile acidity
3.	citric acid
4.	residual sugar
5.	chlorides
6.	free sulfur dioxide
7.	total sulfur dioxide
8.	density
9.	pH
10.	sulphates
11.	alcohol
12.	type of wine

Output variable:
1.	quality (classes : "Excellent" , "Good", "Bad")

### Objective of the Study:

We are interested in whether we can predict the quality of the wine by using physicochemical and its wine type. This is an interesting question because if we can indeed find the perfect formula to produce the perfect wine, we can start a wine company and make a lot of money off from it. Soon, we will take over the wine market and dominate the wine industry with our perfect wine!

In order to answer our research question, we will build a classification model with the features as physicochemical and the type of wine and the output as the quality of wine. In terms of exploratory data analysis, we will first split the data up into a training set and a testing set via a 0.75/0.25 split and perform the EDA on the training set. Since almost all of our predictors are continuous variables, we will first use pandas profiling to create a basic analysis on each of the predictor. Next, we will examine if the columns contain any missing values. Third, we will explore the predictors' distributions given different wine quality via seaborn using a pair plot. Finally, we will examine the distribution of wine quality to determine if there is any class imbalance issue.

In terms of model building, we are planning to use models such as K-Nearest Neighbour, Decision Tree, Support Vector Machine, Logistic Regression, and Naive Bayes to make the predictions. After we finish building our models, we will also explore which features contribute the most in the prediction process. Finally, we will select the best model and re-fit the model on the training data and evaluate it on the test data. In terms of model evaluation, we will look at model accuracy as well as the confusion matrix. These analysis will be included in the final report.

For now, you can find the result of our EDA [here](https://github.com/UBC-MDS/DSCI522_group17/tree/main/src) in a jupyter notebook.

### Dependencies

Python 3.8.3 and Python packages:

* docopt==0.6.2
* requests==2.23.0
* pandas==1.0.5
* seaborn==0.11.0
* pandocfilters==1.4.2


### Usage

To download the data, please run the following script from the root of the project.

    python src/data_download.py --url=https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv --delim=';' --filepath=data/raw/ --filename=winequality-red.csv
    python src/data_download.py --url=https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv --delim=';' --filepath=data/raw/ --filename=winequality-white.csv

### References

P. Cortez, A. Cerdeira, F. Almeida, T. Matos and J. Reis.
Modeling wine preferences by data mining from physicochemical properties. In Decision Support Systems, Elsevier, 47(4):547-553, 2009.

