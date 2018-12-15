#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sklearn import preprocessing
import numpy
import pandas as pd


path_no_attacks_cleaned    =          "data/data_no_attack_cleaned.csv"
path_no_attacks_normalized =          "data/data_no_attack_normalized.csv"
path_attacks_cleaned       =          "data/data_attack_cleaned.csv"
path_attacks_normalized    =          "data/data_attack_normalized.csv"


def to_csv(path,dataframe):
    numpy.savetxt(path, dataframe, delimiter=",")
    
def read_df(path):
   return pd.read_csv(path, low_memory=False)

def normalize_filtered_data(df):
    min_max_scaler  = preprocessing.MinMaxScaler()
    df_norm         = min_max_scaler.fit_transform(df)
    return df_norm

if __name__ == '__main__':
    
    
    df_no_attacks = read_df(path_no_attacks_cleaned) 
    df_attacks    = read_df(path_attacks_cleaned)

    df_norm_no_attacks = normalize_filtered_data(df_no_attacks)
    df_norm_attacks    = normalize_filtered_data(df_attacks)
    
    to_csv(path_no_attacks_normalized,df_norm_no_attacks)
    to_csv(path_attacks_normalized,df_norm_attacks)
   
