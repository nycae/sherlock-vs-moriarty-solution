#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import numpy

path_no_attacks         =           "data/data_no_attack.csv"
path_no_attacks_cleaned =           "data/data_no_attack_cleaned.csv"
path_inter              =           "data/data_no_attack_inter.csv"
path_plot               =           "plots/"

def read_dataset(path_no_attacks):
    return pd.read_csv(path_no_attacks)

def clean_first_line_dataset(path_inter):
    input_file  = open(path_inter, 'r')
    output_file = open(path_no_attacks_cleaned, 'w')
    
    input_file.readline()
    line = input_file.readline()
    while line:
        output_file.write(line)
        
        line=input_file.readline()
    output_file.close()
    

def clean_dataset(file):
     exclude         = ['UserID', 'UUID', 'Version', 'TimeStemp']
     df_ex           = file.loc[:, file.columns.difference(exclude)]
     df_ex           = df_ex.drop([0], axis=0)
     return df_ex
 
def to_csv(path,dataframe):
    numpy.savetxt(path, dataframe, delimiter=",")

if __name__ == '__main__':
    df=read_dataset(path_no_attacks)
    df_ex = clean_dataset(df)
    to_csv(path_inter,df_ex)
    
    clean_first_line_dataset(path_inter)
    df_c = read_dataset(path_inter)
    
    
