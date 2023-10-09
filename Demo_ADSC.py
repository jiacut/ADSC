# -*- codeing = utf-8 -*-
# @Author : wyh
# @Software : PyCharm
import datetime
import Dataprocessing
import numpy as np
from sklearn import metrics
from ADSC import ADSC

if __name__ == '__main__':
    # read data file
    config_dict = Dataprocessing.read_config()

    # parameter
    DATA_File = config_dict['DATA_File']

    k = config_dict['k']
    threshold= config_dict['threshold']
    beta = config_dict['beta']
    ann = config_dict['ann']
    metric = config_dict['metric']

    # read the dataset and label
    data, label_true = Dataprocessing.get_data(DATA_File)
    print(data.shape)
    # original_data, label_true = Dataprocessing.get_data(DATA_File)
    # data = Dataprocessing.maxminnorm(original_data)

    starttime = datetime.datetime.now()

    model = ADSC(k, threshold, beta, ann=ann, metric=metric)
    model.fit(data)
    label_pred = model.labels_

    endtime = datetime.datetime.now()
    print('total time=', endtime - starttime)

    ARI = metrics.adjusted_rand_score(label_true, label_pred)
    AMI = metrics.adjusted_mutual_info_score(label_true, label_pred)
    NMI = metrics.normalized_mutual_info_score(label_true, label_pred)

    print("Adj. Rand Index Score=", ARI)
    print("Adj. Mutual Info Score=", AMI)
    print("Norm Mutual Info Score=", NMI)

    center_id = model.choosen_original_id

    #Dataprocessing.id_diagram(center_id, model.DS_index, model.cc_set, 1. / model.knn_radius, model.delta)
    #Dataprocessing.plot_quickdsc(data, center_id, model.DS_index, model.cc_set)
    #Dataprocessing.show_cluster(data, label_pred, center_id)
