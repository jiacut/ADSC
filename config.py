# -*- codeing = utf-8 -*-
# @Author : wyh
# @Software : PyCharm

# the config file
[section]

# the dataset filename
DATA_File = ./datasets/banknote.csv
# DATA_File = ./datasets/s2.csv
# DATA_File = ./datasets/s3.csv
# DATA_File = ./datasets/glass.csv
# DATA_File = ./datasets/letter.csv
# DATA_File = ./datasets/page-blocks.csv


# the kNN value
k = 32

# the beta value
beta = 0.9

# threshold
threshold = 0.7

# the index type
ann = kdtree
# ann = balltree
# ann = rptree

# the metric type
metric = euclidean
