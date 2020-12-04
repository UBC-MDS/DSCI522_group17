# Authors: Pan Fan, Chun Chieh Chang, Sakshi Jain
# Date: 2020-12-04

all: data/raw/winequality-red.csv data/raw/winequality-white.csv data/processed/train.csv data/processed/test.csv results/boxplot.png results/densityplot.png results/cor.png data/processed/train_pp.csv data/processed/test_pp.csv results/cs_results.csv results/Bestmodel.csv docs/report.html docs/report.md

# download both wine data sets
data/raw/winequality-red.csv : src/data_download.py 
	python src/data_download.py --url=https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv --delim=';' --filepath=data/raw/ --filename=winequality-red.csv
data/raw/winequality-white.csv : src/data_download.py 
	python src/data_download.py --url=https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv --delim=';' --filepath=data/raw/ --filename=winequality-white.csv

# generate train and test dataset
data/processed/train.csv data/processed/test.csv : data/raw/winequality-red.csv data/raw/winequality-white.csv src/dt_cr.py
	python src/dt_cr.py  data/raw/winequality-red.csv data/raw/winequality-white.csv data/processed/train.csv data/processed/test.csv

# create data visualization including one boxplot, one density plot and one correlation plot 
results/boxplot.png results/densityplot.png results/cor.png : data/processed/train.csv src/eda_figs.py
	python src/eda_figs.py data/processed/train.csv results/boxplot.png results/densityplot.png results/cor.png

# transform train and test dataset 
data/processed/train_pp.csv data/processed/test_pp.csv : data/processed/train.csv data/processed/test.csv src/pre.py
	python src/pre.py data/processed/train.csv data/processed/test.csv data/processed/train_pp.csv data/processed/test_pp.csv



# fit transformed training dataset and compare the performance of different classification models
results/cs_results.csv results/Bestmodel.csv : data/processed/train_pp.csv data/processed/test_pp.csv src/clf_comp.py
	python src/clf_comp.py data/processed/train_pp.csv data/processed/test_pp.csv results/cs_results.csv results/Bestmodel.csv


# render the report
docs/report.html docs/report.md : docs/report.Rmd
	Rscript -e "rmarkdown::render('docs/report.Rmd')"


clean:
	rm -rf data/raw/winequality-red.csv
	rm -rf data/raw/winequality-white.csv
	rm -rf data/processed/train.csv 
	rm -rf data/processed/test.csv
	rm -rf results/boxplot.png 
	rm -rf results/densityplot.png 
	rm -rf results/cor.png
	rm -rf data/processed/train_pp.csv 
	rm -rf data/processed/test_pp.csv
	rm -rf results/cs_results.csv 
	rm -rf results/Bestmodel.csv
	rm -rf docs/report.html
	rm -rf docs/report.md
	