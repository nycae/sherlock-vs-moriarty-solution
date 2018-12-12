#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import routes as r
import os

def read_dataset(path):
    return pd.read_csv(path)

def merge_datasets(path_no_attacks, path_attacks):
    os.system("echo GyroscopeStat_x_MEAN,GyroscopeStat_z_MEAN,GyroscopeStat_COV_z_x,GyroscopeStat_COV_z_y,MagneticField_x_MEAN,MagneticField_z_MEAN,MagneticField_COV_z_x,MagneticField_COV_z_y,Pressure_MEAN,LinearAcceleration_COV_z_x,LinearAcceleration_COV_z_y,LinearAcceleration_x_MEAN,LinearAcceleration_z_MEAN,attack > {}".format(r.path_merged_data))
    os.system("cat {} {} >> {} ".format(path_no_attacks,path_attacks,r.path_merged_data))  

def add_columns_names(path_old, path_new):
    os.system("echo GyroscopeStat_x_MEAN,GyroscopeStat_z_MEAN,GyroscopeStat_COV_z_x,GyroscopeStat_COV_z_y,MagneticField_x_MEAN,MagneticField_z_MEAN,MagneticField_COV_z_x,MagneticField_COV_z_y,Pressure_MEAN,LinearAcceleration_COV_z_x,LinearAcceleration_COV_z_y,LinearAcceleration_x_MEAN,LinearAcceleration_z_MEAN,attack > {}".format(path_new))
    os.system("cat {} >> {} ".format(path_old,path_new))
    
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
    df1           = read_dataset(r.path_norm_attacks)
    df1['1'] = 1
    
    df2           = read_dataset(r.path_norm_centroids)
    df2['0'] = 0
        
    to_csv(r.path_processed_attacks, df1)
    to_csv(r.path_processed_no_attacks, df2)

    merge_datasets(r.path_processed_attacks, r.path_processed_no_attacks)
    df_merged = read_dataset(r.path_merged_data)
    
    train,test = divide_datasets(df_merged)
    
    #Sin nombre de las columnas
    to_csv(r.path_train_aux,train)
    to_csv(r.path_test_aux,test)
    
    add_columns_names(r.path_train_aux, r.path_train)
    add_columns_names(r.path_test_aux, r.path_test)
    
    
    