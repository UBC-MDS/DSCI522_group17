# Authors: Pan Fan, Chun Chieh Chang, Sakshi Jain
# Date: 2020-11-27
#
# Driver script/analysis pipeline for wine quality analysis
#
# Usage:
# bash runall.sh



# download both wine data sets
python src/data_download.py --url=https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv --delim=';' --filepath=data/raw/ --filename=winequality-red.csv
python src/data_download.py --url=https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv --delim=';' --filepath=data/raw/ --filename=winequality-white.csv

# generate train and test dataset (2 inputs , 2 outputs)

python src/data_creation.py data/raw/winequality-red.csv data/raw/winequality-white.csv data/processed/train.csv data/processed/test.csv

# create data visualization including one boxplot, one density plot and one correlation plot (1 inputs , 3 outputs)

python src/eda.py data/processed/train.csv results/boxplot.png results/densityplot.png results/cor.png

# transform train and test dataset (2 inputs , 2 outputs)

python src/preprocess.py data/processed/train.csv data/processed/test.csv data/processed/train_pp.csv data/processed/test_pp.csv

# fit transformed training dataset and compare the performance of different classification models and run model predition to get results (2 inputs , 2 outputs)

python src/clf_comparison.py data/processed/train_pp.csv data/processed/test_pp.csv results/cs_results.csv results/Bestmodel.csv


# render the report into an html and an md file

Rscript -e "rmarkdown::render('docs/report.Rmd', output_format = 'all')"




