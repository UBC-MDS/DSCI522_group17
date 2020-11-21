# Wine Quality Prediction (DSCI522_group17)
Group work for DSCI522 Our group  number is 17

Date: 11/20/2020

Team members: Pan Fan, Chun Chieh Chang and Sakshi Jain

GitHub repository: https://github.com/UBC-MDS/DSCI522_group17

Introduction
As somebody said that “Life is too short to drink bad wine.”, we decided to work on the wine dataset so that we can help in determining the quality of wine. 
Dataset: The data set used in this project is sourced from the UCI Machine Learning Repository and can be found https://archive.ics.uci.edu/ml/datasets/Wine+Quality. Two datasets are included, related to red and white wine, from the north of Portugal. There are 6497 observations in the dataset with 11 physiochemical variables, as independent variables and one output quality variable measuring quality score given by bunch of wine experts. Due to privacy and logistic issues, only physicochemical (inputs) and sensory (the output) variables are available (e.g. there is no data about grape types, wine brand, wine selling price, etc.).
Input variables (based on physicochemical tests):
1.	fixed acidity (tartaric acid - $g / dm^{3}$)
2.	volatile acidity (acetic acid - g / dm^3)
3.	citric acid (g / dm^3)
4.	residual sugar (g / dm^3)
5.	chlorides (sodium chloride - g / dm^3
6.	free sulfur dioxide (mg / dm^3)
7.	total sulfur dioxide (mg / dm^3)
8.	density (g / cm^3)
9.	pH
10.	sulphates (potassium sulphate - g / dm3)
11.	alcohol (% by volume)
12.	type of wine(red or white)

Output variable (based on sensory data):
1.	quality (classes : "Excellent" , "Good", "Bad")

Objective of the study:
For this project we are trying to answer the question: can we predict the quality of the wine by using physicochemical? To answer the predictive question posed here, we plan to build a predictive classification model after merging the both data set. Before building our model we will partition the data into a training and test set (split 75%:25%) and perform exploratory data analysis to assess whether there is a strong class imbalance problem that we might need to address, as well as explore whether there are any predictors whose distribution looks very similar between the two classes, and thus we might omit from our analysis. We will analyses if any missing value treatment is needed.
Given that all measurements are continuous in nature, and the outcome we are trying to predict is one of the class among 11 classes. We are planning to explore different machine learning models such as a k-nearest neighbors classification algorithm, SVM and Decision Tree. 

After selecting our final model, we will re-fit the model on the entire training data set, and then evaluate it’s performance on the test data set. At this point we will look at overall accuracy as well as misclassification errors (from the confusion matrix) to assess prediction performance. These values will be reported as a table in the final report.

Thus far we have performed some exploratory data analysis, and the report for that can be found here.

## Report

The EDA can be found
[here](https://github.com/UBC-MDS/DSCI522_group17/blob/main/wine.ipynb).
