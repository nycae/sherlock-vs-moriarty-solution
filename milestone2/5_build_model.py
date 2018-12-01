#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import os

path_attacks_normalized     =           "data/data_attack_cleaned.csv"
path_centroids_no_attacks   =           "data/data_no_attack_centroids.csv"
path_mergered               =           "data/data_merged.csv"
path_train                  =           "model/data_train.csv"
path_test                   =           "model/data_test.csv"

'''
In order to improve our model, we try to develop a random forest.

1) Mezclar ataques y no ataques (Hecho)
2) Parametrizar random forest
3) Hacer vainas

'''
def read_dataset(path):
    return pd.read_csv(path)

def merge_datasets(df_centroids, df_attacks_normalized):
    os.system("cat {} {} > {} ".format(path_centroids_no_attacks,path_attacks_normalized,path_mergered))
    df = read_dataset(path_mergered)
    return df
    
def divide_datasets(df_merged):
    # Mezclamos y requetemezclamos
    df_divide = df_merged.sample(frac=1)
    # 1/3 for test  2/3 for train
    p = 0.67
    df_train = df_divide[:int((len(df_divide))*p)]
    df_test = df_divide[int((len(df_divide))*p):]
    
    return df_train,df_test

def to_csv(path,dataframe):
    np.savetxt(path, dataframe, delimiter=",")
    
if __name__ == '__main__':
    df1       = read_dataset(path_attacks_normalized)
    df2       = read_dataset(path_centroids_no_attacks)
    
    df_merged = merge_datasets(df1,df2)
    train,test = divide_datasets(df_merged)
    
    to_csv(path_train,train)
    to_csv(path_test,test)
    