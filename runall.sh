# Pan Fan
# 2020-11-27
#
# Driver script/analysis pipeline for wine quality analysis
#
# Usage:
# bash runall.sh

# generate train and test dataset (2 inputs , 2 outputs)

python src/dt_cr.py  data/raw/winequality-red.csv data/raw/winequality-white.csv data/processed/train.csv data/processed/test.csv

# create data visualization including one boxplot, one density plot and one correlation plot (1 inputs , 3 outputs)

python src/eda_figs.py data/processed/train.csv src/figures/boxplot.png src/figures/densityplot.png src/figures/cor.png

# transform train and test dataset (2 inputs , 2 outputs)

python src/pre.py data/processed/train.csv data/processed/test.csv data/processed/train_pp.csv data/processed/test_pp.csv

# fit transformed training dataset and compare the performance of different classification models (1 inputs , 1 outputs)

python src/clf_comp.py data/processed/train_pp.csv results/training_res.csv

