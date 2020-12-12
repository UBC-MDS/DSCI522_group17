# Authors: Pan Fan, Chun Chieh Chang, Sakshi Jain
# Date: 2020-12-04

all: docs/report.html docs/report.md

# download both wine data sets
data/raw/winequality-red.csv : src/data_download.py 
	python src/data_download.py --url=https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv --delim=';' --filepath=data/raw/ --filename=winequality-red.csv
data/raw/winequality-white.csv : src/data_download.py 
	python src/data_download.py --url=https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv --delim=';' --filepath=data/raw/ --filename=winequality-white.csv

# generate train and test dataset
data/processed/train.csv data/processed/test.csv : data/raw/winequality-red.csv data/raw/winequality-white.csv src/data_creation.py
	python src/data_creation.py  data/raw/winequality-red.csv data/raw/winequality-white.csv data/processed/train.csv data/processed/test.csv

# create data visualization including one boxplot, one density plot and one correlation plot 
results/boxplot.png results/densityplot.png results/cor.png : src/eda.py data/processed/train.csv
	python src/eda.py data/processed/train.csv results/boxplot.png results/densityplot.png results/cor.png

# transform train and test dataset 
data/processed/train_pp.csv data/processed/test_pp.csv : src/preprocess.py data/processed/train.csv data/processed/test.csv
	python src/preprocess.py data/processed/train.csv data/processed/test.csv data/processed/train_pp.csv data/processed/test_pp.csv



# fit transformed training dataset and compare the performance of different classification models
results/cv_results.csv results/bestmodel.csv : src/clf_comparison.py data/processed/train_pp.csv data/processed/test_pp.csv
	python src/clf_comparison.py data/processed/train_pp.csv data/processed/test_pp.csv results/cv_results.csv results/bestmodel.csv


# render the report

docs/report.md docs/report.html : docs/report.Rmd results/boxplot.png results/densityplot.png results/cv_results.csv results/bestmodel.csv
	Rscript -e "rmarkdown::render('docs/report.Rmd', output_format = 'all')"

clean:
	rm -rf data/raw/*.csv
	rm -rf data/processed/*.csv 
	rm -rf results/*.png 
	rm -rf data/processed/*.csv 
	rm -rf results/*.csv
	rm -rf results/*.joblib
	rm -rf docs/report.html
	rm -rf docs/report.md
	