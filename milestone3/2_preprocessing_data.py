#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import numpy
import routes as r
from sklearn import preprocessing

def read_dataset(path_no_attacks):
    return pd.read_csv(path_no_attacks)

def clean_first_line_dataset(path_in,path_out):
    input_file  = open(path_in, 'r')
    output_file = open(path_out, 'w')
    
    input_file.readline()
    line = input_file.readline()
    while line:
        output_file.write(line)  
        line=input_file.readline()
    output_file.close()
    
def clean_dataset_and_normalize(data):
    data.drop(df_attacks.columns[[0]], axis=1, inplace=True)
  
    exclude         = ['UserID', 'UUID', 'Version', 'TimeStemp', 'attack']
    df_ex           = data.loc[:, data.columns.difference(exclude)]

    min_max_scaler  = preprocessing.MinMaxScaler()
    df_norm         = min_max_scaler.fit_transform(df_ex)
     
    return df_norm
 
def to_csv(path,dataframe):
    numpy.savetxt(path, dataframe, delimiter=",")

if __name__ == '__main__':
    
    df_no_attacks = read_dataset(r.path_raw_no_attacks)
    df_attacks    = read_dataset(r.path_raw_attacks)
        
    df_clean_norm_no_attacks = clean_dataset_and_normalize(df_no_attacks)
    df_clean_norm_attacks    = clean_dataset_and_normalize(df_attacks)
    
    to_csv(r.path_norm_no_attacks, df_clean_norm_no_attacks)
    to_csv(r.path_norm_attacks, df_clean_norm_attacks)
    
    
    
    
