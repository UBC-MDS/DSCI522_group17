Predicting Wine Quality Given Physicochemical and Wine Type
================
Chun Chieh Chang, Sakshi Jain, Pan Fan
2020/11/27 (Updated: 2020-12-13)

-   [Summary](#summary)
-   [Introduction](#introduction)
-   [Methods](#methods)
    -   [Data](#data)
    -   [Analysis](#analysis)
-   [Results and Discussion](#results-and-discussion)
-   [References](#references)

# Summary

In this project we built several models to try to predict wine quality
given different physicochemical properties and wine type. We built a
K-Nearest Neighbor model, Logistic Regression model, Random Forest
Model, and Support Vector Machine model. Since there exists an issue of
class imbalance in the data set, we will be using f1-score as our
validation metric. After we built these models, we found out that Random
Forest is the best performing model and it achieved a test score of
0.63. However, despite it being a good score, there is still room for
improvement. From our cross validation results, we can see that we are
overfitting with Random Forest even after hyperparameter tuning. A
solution for this problem will be to increase the number of data when
training the model, which is not possible because we have no ways to
collect additional data. Another solution for this problem will be to
use a more powerful computer to search for more hyperparameter
combinations. At the current state we can conclude that our model is
usable because it performs better than our baseline model by a large
margin and also the accuracy of prediction is over 60%.

# Introduction

Wine is a fermented fruit juice which contains alcohol as its main
ingredient. It’s complex chemical process which starts with the
selection of the fruit, its fermentation into alcohol, and the bottling
of the finished liquid. In this entire process, chemicals produced by
yeasts after consuming sugar of the fruit, play very important role in
producing different style of wine and even the quality depends on it.

Across the world, wine plays an important part of culture. It is both
liked and disliked. In some continents like Europe and America, there is
no celebration, no cheers up without wine whereas wine is disliked and
even legally banned in some parts of Asia. Wine’s popularity has
increased by development of innovative flavors and advanced distribution
systems. According to Statista, the global wine market was valued at
354.7 billion in U.S dollars in 2018 and is estimated to grow 21 percent
by 2023 ultimately valuing over 429 billion U.S dollars(Oloruntoba
2020). Hence, it’s important to know the quality of wine to determine
its price as well to target premium wine customers.

# Methods

## Data

The data set used in this project is sourced from the UCI Machine
Learning Repository(Dua and Graff 2017) and can be found
[here](https://archive.ics.uci.edu/ml/datasets/Wine+Quality). In terms
of the data, the two data sets record the physicochemical properties of
the red and white variants of the Vinho Verde wine. We merged these two
datasets together and created a new column `type of wine` to represent
the wine type for each observation. The `quality_level` is the target we
are interested in predicting and it represents the quality of the wine
on a scale of 1 to 10. We will group the quality of wine into three
categories and they are “Excellent” if `quality_level` is equal to or
greater than 7, “Good” if `quality_level` is between 4 and 7(exclusive),
and “Bad” if `quality_level` is less than or equal to 4. We also have a
categorical variable `wine_type` that we will include as a feature. In
total, we have 12 predictors and one output variable.

## Analysis

For this project, we will be using models such as Logistic Regression,
Randomized Forest, Support Vector Machine, and K-Nearest Neighbor to
help us predict wine quality.

To build our models, we will be using Python(Van Rossum and Drake 2009)
and it’s associated libraries. We will be using docopt(Keleshev 2014)and
os(Van Rossum and Drake 2009) to help us automate our script,
Pandas(team 2020) to structure our data, Seaborn(Waskom and team 2020)
and PandasProfiling(Brugman 2020) to plot the figures, and
sklearn(Pedregosa et al. 2011) to build our models. In terms of
presenting our results, we will use R (R Core Team 2020), tidyverse
package(Wickham et al. 2019), and the knitr package(Xie 2014) to present
our results. If you are interested in the codes that were used to build
our model, they can be found at
<https://github.com/UBC-MDS/DSCI522_group17/blob/main/src/>

# Results and Discussion

We will first begin by examining the distribution of each numeric
feature given the class we are trying to predict. Figure 1 plots the
density of each numeric feature given wine quality. From examining each
density plot, we observed that there are a lot of overlaps between the
density of each class. However, The feature `Density` and `Alcohol` seem
to have different mean and spread given wine quality. This is a great
sign as these two features could be good features that allow our machine
learning model to distinguish different classes effectively. Also, We
can see that most features are right skewed.

<div class="figure">

<img src="../results/densityplot.png" alt="Fig 1. Density Plot of Numeric Features Given Wine Quality" width="100%" height="100%" />
<p class="caption">
Fig 1. Density Plot of Numeric Features Given Wine Quality
</p>

</div>

Next, we examine if there is any class imbalance issue. Figure 2 plots
the count of each class in our training data. As we can see, we have
class imbalance issue where the number of observations for `Good` class
far outweighs than that of `Excellent` class, which is our target of
prediction. To overcome this problem, we decided to use f1 score as our
validation metric where the average method is set to `weighted`. We
chose weighted f1 score because it calculates the f1 score for each
class and calculates an average score given the class proportion. In
addition, when we build our models, the class weight parameter will be
set to `balanced` to account for the class imbalance.

<div class="figure">

<img src="../results/class_dist.png" alt="Fig 2. Distribution of Wine Quality" width="50%" height="50%" />
<p class="caption">
Fig 2. Distribution of Wine Quality
</p>

</div>

We used cross validation with the default cv of 5 to fit our models and
obtained the mean statistics of each model. The scoring metric we
decided to use is accuracy. The summary table is shown in Table 1 below.
From observing the table, we can see that the model Random Forest has
the best validation f1 score.

| Models                | validation\_score | train\_score |
|:----------------------|------------------:|-------------:|
| Logistic\_Regression  |         0.5219117 |    0.5257318 |
| Random\_Forest        |         0.6195363 |    1.0000000 |
| DummyClassifier       |         0.1745093 |    0.1718379 |
| SVC                   |         0.5648274 |    0.5985701 |
| K\_Nearest\_Neighbors |         0.5492148 |    0.6883396 |

Table 1. 5 Fold Cross Validation Results of Untuned Models

After our initial cross validation test, we decided to hyperparameter
tune the Random Forest Model and Logistic Regression Model. We chose
these two models because Random Forest was our best model and Logistic
Regression was the easiest model in terms of interpretability. Table 2
presents the cross validation results of the tuned Random Forest and
Logistic Regression models. From the results below, we can see that our
validation scores for both models only improved slightly compared to the
default model with no tuning.

| Models              | validation\_score | train\_score |
|:--------------------|------------------:|-------------:|
| Random Forest       |         0.6208297 |    1.0000000 |
| Logistic Regression |         0.5258040 |    0.5285105 |

Table 2. 5 Fold Cross Validation Results of Tuned Models

Finally, we fitted the tuned Random Forest model on the training set and
calculated the f1-score on the test set. The final f1 test score is
0.63. Hence, our model achieved an accuracy of 0.63 in predicting the
correct wine quality given physicochemical and wine types, which in our
opinion is a relatively good score. However, there is still room for
improvement as we can see from our cross validation that we are still
overfitting with Random Forest. To improve our model even further, we
would need more training data to train our model as well as a more
powerful computer to search through the hyperparameter space. At the
current state we can conclude that our model is usable because it
performs better than our baseline model by a large margin and also the
accuracy of prediction is over 60%.

# References

<div id="refs" class="references csl-bib-body hanging-indent">

<div id="ref-pandaprofile" class="csl-entry">

Brugman, Simon. 2020. *Docopt: Command-Line Interface Description
Language*. <https://github.com/pandas-profiling/pandas-profiling>.

</div>

<div id="ref-Dua:2019" class="csl-entry">

Dua, Dheeru, and Casey Graff. 2017. “UCI Machine Learning Repository.”
University of California, Irvine, School of Information; Computer
Sciences. <http://archive.ics.uci.edu/ml>.

</div>

<div id="ref-docopt" class="csl-entry">

Keleshev, Vladimir. 2014. *Docopt: Command-Line Interface Description
Language*. <https://github.com/docopt/docopt>.

</div>

<div id="ref-statista" class="csl-entry">

Oloruntoba, A. 2020. “Revenue of the Wine Market Worldwide by Country
2018.” *Statista*.
<https://www.statista.com/forecasts/758149/revenue-of-the-wine-market-worldwide-by-country>.

</div>

<div id="ref-sklearn" class="csl-entry">

Pedregosa, F., G. Varoquaux, A. Gramfort, V. Michel, B. Thirion, O.
Grisel, M. Blondel, et al. 2011. “Scikit-Learn: Machine Learning in
Python.” *Journal of Machine Learning Research* 12: 2825–30.

</div>

<div id="ref-R" class="csl-entry">

R Core Team. 2020. *R: A Language and Environment for Statistical
Computing*. Vienna, Austria: R Foundation for Statistical Computing.
<https://www.R-project.org/>.

</div>

<div id="ref-pandas" class="csl-entry">

team, The pandas development. 2020. *Pandas-Dev/Pandas: Pandas* (version
1.0.5). Zenodo. <https://doi.org/10.5281/zenodo.3509134>.

</div>

<div id="ref-Python" class="csl-entry">

Van Rossum, Guido, and Fred L. Drake. 2009. *Python 3 Reference Manual*.
Scotts Valley, CA: CreateSpace.

</div>

<div id="ref-seaborn" class="csl-entry">

Waskom, Michael, and the seaborn development team. 2020.
*Mwaskom/Seaborn* (version 0.11.0). Zenodo.
<https://doi.org/10.5281/zenodo.592845>.

</div>

<div id="ref-tidyverse" class="csl-entry">

Wickham, Hadley, Mara Averick, Jennifer Bryan, Winston Chang, Lucy
D’Agostino McGowan, Romain François, Garrett Grolemund, et al. 2019.
“Welcome to the <span class="nocase">tidyverse</span>.” *Journal of Open
Source Software* 4 (43): 1686. <https://doi.org/10.21105/joss.01686>.

</div>

<div id="ref-knitr" class="csl-entry">

Xie, Yihui. 2014. “Knitr: A Comprehensive Tool for Reproducible Research
in R.” In *Implementing Reproducible Computational Research*, edited by
Victoria Stodden, Friedrich Leisch, and Roger D. Peng. Chapman;
Hall/CRC. <http://www.crcpress.com/product/isbn/9781466561595>.

</div>

</div>
