# Authors: Pan Fan, Chun Chieh Chang, Sakshi Jain
# Date: 2020-12-04

all: data/raw/winequality-red.csv data/raw/winequality-white.csv data/processed/train.csv data/processed/test.csv

# download both wine data sets
data/raw/winequality-red.csv : src/data_download.py 
	python src/data_download.py --url=https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv --delim=';' --filepath=data/raw/ --filename=winequality-red.csv
data/raw/winequality-white.csv : src/data_download.py 
	python src/data_download.py --url=https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv --delim=';' --filepath=data/raw/ --filename=winequality-white.csv

# generate train and test dataset
data/processed/train.csv data/processed/test.csv : data/raw/winequality-red.csv data/raw/winequality-white.csv src/dt_cr.py
	python src/dt_cr.py  data/raw/winequality-red.csv data/raw/winequality-white.csv data/processed/train.csv data/processed/test.csv

clean:
	rm -rf data/raw/winequality-red.csv
	rm -rf data/raw/winequality-white.csv
	rm -rf data/processed/train.csv 
	rm -rf data/processed/test.csv