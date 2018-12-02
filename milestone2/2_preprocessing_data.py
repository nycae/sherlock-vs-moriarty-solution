#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import numpy

path_attacks            =           "data/data_attack.csv"
path_no_attacks         =           "data/data_no_attack.csv"
path_no_attacks_cleaned =           "data/data_no_attack_cleaned.csv"
path_attacks_cleaned    =           "data/data_attack_cleaned.csv"
path_inter_no_attack    =           "data/data_no_attack_inter.csv"
path_inter_attack       =           "data/data_attack_inter.csv"


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
    

def clean_dataset(file):
     exclude         = ['UserID', 'UUID', 'Version', 'TimeStemp']
     df_ex           = file.loc[:, file.columns.difference(exclude)]
     return df_ex
 
def to_csv(path,dataframe):
    numpy.savetxt(path, dataframe, delimiter=",")

if __name__ == '__main__':
    
    df_no_attacks = read_dataset(path_no_attacks)
    df_attacks    = read_dataset(path_attacks)
    
    df_clean_no_attacks = clean_dataset(df_no_attacks)
    df_clean_attacks    = clean_dataset(df_attacks)
    
    to_csv(path_inter_no_attack ,df_clean_no_attacks)
    to_csv(path_inter_attack,df_clean_attacks)
    
    clean_first_line_dataset(path_inter_no_attack,path_no_attacks_cleaned)
    clean_first_line_dataset(path_inter_attack,path_attacks_cleaned)
    
    
    
    
