#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import numpy

def preprocess_moriarty(path_to_csv, path_to_destiny):
  input_file  = open(path_to_csv, 'r')
  output_file = open(path_to_destiny, 'w')

  output_file.write(input_file.readline()) # Column name
  line        = input_file.readline()
  
  while line:
    line_to_write = line.replace('],', '];')

    output_file.write(line_to_write)
    line = input_file.readline()

def label_dataset(df_to_label, df_labels):
  for i in df_labels["UUID"]:
    aux = df_to_label[(int(i) <= df_to_label.UUID ) & (int(i) >= (df_to_label.UUID - 20000))]
    print(aux)
    if not (aux.empty or aux.attack == 1):
      df_to_label.loc[aux.index, 'attack'] = 1

def read_df(path):
    return pd.read_csv(path, low_memory=False)


def to_csv(path,dataframe):
    dataframe.to_csv(path)
    print("File preprocessed.csv created sucessfully")

def drop_nulls(dataframe):
    dataf= dataframe.replace(" NULL", numpy.NaN)
    dataf= dataf.dropna()
    return dataf
    
######################################################################
############################## EXECUTE   #############################
######################################################################

if __name__ == '__main__':    
    df_T2                = read_df("data/T2.csv")
    df_to_find           = df_T2[(df_T2.UUID >= 1461851815453) & ((df_T2.UUID <= 1463565596193))]    
    df_to_find['attack'] = 0
    preprocess_moriarty("data/Moriarty.csv", "data/Moriarty_fix.csv")
    
    df_Mor = read_df("data/Moriarty_fix.csv")
    label_dataset(df_to_find, df_Mor)
    