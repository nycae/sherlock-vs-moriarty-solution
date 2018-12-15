#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import os

path_attacks_normalized     =           "data/data_attack_normalized.csv"
path_centroids_no_attacks   =           "data/data_no_attack_centroids.csv"
path_mergered               =           "data/data_merged.csv"
path_train                  =           "model/data_train.csv"
path_test                   =           "model/data_test.csv"
path_divided                =           "data/data_divided.csv"
'''
In order to improve our model, we try to develop a random forest.

1) Merge attacks and no attacks
2) Parameterize random forest


'''
def read_dataset(path):
    return pd.read_csv(path)

def merge_datasets():
    # os.system("echo GyroscopeStat_x_MEAN,GyroscopeStat_z_MEAN,GyroscopeStat_COV_z_x,GyroscopeStat_COV_z_y,MagneticField_x_MEAN,MagneticField_z_MEAN,MagneticField_COV_z_x,MagneticField_COV_z_y,Pressure_MEAN,LinearAcceleration_COV_z_x,LinearAcceleration_COV_z_y,LinearAcceleration_x_MEAN,LinearAcceleration_z_MEAN,attack > {}".format(path_mergered))
    os.system("cat {} {} >> {} ".format(path_centroids_no_attacks,path_attacks_normalized,path_mergered))
    df = read_dataset(path_mergered)
    return df
    
def divide_datasets(df_merged):
    # Mezclamos y requetemezclamos
    df_divide = df_merged.sample(frac=1)
    # 1/3 for test  2/3 for train
    p = 0.67
    df_train = df_divide[:int((len(df_divide))*p)]
    df_test = df_divide[int((len(df_divide))*p):]
    
    return df_train,df_test,df_divide

def to_csv(path,dataframe):
    np.savetxt(path, dataframe, delimiter=",")
    
if __name__ == '__main__':

    
    df_merged = merge_datasets()
    #df_merged = df_merged.replace(0, 1)
    #df_merged = df_merged.replace(np.nan, 0)
    
    
    train,test,divided = divide_datasets(df_merged)
    
    to_csv(path_train,train)
    to_csv(path_test,test)
    to_csv(path_divided,divided)