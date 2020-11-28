# Wine Quality Prediction (DSCI522_group17)
Group work for DSCI522 Our group  number is 17

Date: 11/27/2020

Team members: Pan Fan, Chun Chieh Chang and Sakshi Jain

GitHub repository: https://github.com/UBC-MDS/DSCI522_group17

## Summary
In this project we will build several models to try to predict wine quality given different physicochemical properties and wine type. We built a K-Nearest Neighbor model, Logistic Regression model, Random Forest Model, and Support Vector Machine model. After we built these models, we found out that Random Forest is the best performing model and it achieved a test score that is close to 1. This may be a misleading score because we only have 3 different classes to predict compared to 10 in the original dataset and hence the model possibly found a pattern to fit the data perfectly. In addition, there was class imbalance issue such that the number of observations of 'Bad' quality wine and 'Excellent' wine are significantly less than 'Good' quality wine. Hence, further investigation is needed before we can finalize our model.

The data set used in this project is sourced from the UCI Machine Learning Repository and can be found [here](https://archive.ics.uci.edu/ml/datasets/Wine+Quality). In terms of the data, the two data sets record the physicochemical properties of the red and white variants of the Vinho Verde wine. We merged these two datasets together and created a new column `type of wine` to represent the wine type for each observation. The `quality_level` is the target we are interested in predicting and it represents the quality of the wine on a scale of 1 to 10. We will group the quality of wine into three categories and they are "Excellent" if `quality_level` is equal to or greater than 7, "Good" if `quality_level` is between 4 and 7(exclusive), and "Bad" if `quality_level` is less than or equal to 4. We also have a categorical variable `wine_type` that we will include as a feature. In total, we have 12 predictors and one output variable.




## Report

A copy of the report can be found [here]()


## Usage

To replicate the analysis, clone this GitHub repository, install the dependencies listed below, and run the following commands at the command line/terminal from the root directory of this project:

    sh runall.sh

By running this shell script, it will first download the two data sets from source. Next, it will merge the two data sets together and split the data into training and test sets. Third, it will perform simple Exploratory data analysis and save the figure in the results/ folder. It will then transform the train and test set for model building and evaluation. Next, it will fit the models using the transformed data and evaluate the models using the transformed test data. Finally, the report will be rendered and saved in the docs/ folder and in it you can find all the figures, tables, and analysis pertaining to this project.


## Dependencies

Python 3.8.3 and Python packages:

* docopt==0.6.2
* requests==2.23.0
* pandas==1.0.5
* seaborn==0.11.0
* pandocfilters==1.4.2
* scikit-learn== 0.23.2


R  4.0.2 and packages:
* tidyverse==1.3.0
* knitr==1.29

## License

Please refer to the License File [here](https://github.com/UBC-MDS/DSCI522_group17/blob/main/LICENSE)

## References

P. Cortez, A. Cerdeira, F. Almeida, T. Matos and J. Reis.
Modeling wine preferences by data mining from physicochemical properties. In Decision Support Systems, Elsevier, 47(4):547-553, 2009.

