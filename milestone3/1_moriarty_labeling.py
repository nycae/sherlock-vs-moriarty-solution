#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import routes as r

def preprocess_moriarty(path_to_csv, path_to_destiny):
  input_file  = open(path_to_csv, 'r')
  output_file = open(path_to_destiny, 'w')

  output_file.write(input_file.readline()) # Column name
  line        = input_file.readline()
  
  while line:
    line_to_write = line.replace('],', '];')

    output_file.write(line_to_write)
    line = input_file.readline()

def label_dataset(df_to_label, df_labels, probe_time):
  
  for i in df_labels["UUID"]:
    aux = df_to_label[(int(i) <= df_to_label.UUID ) & (int(i) >= (df_to_label.UUID - probe_time))]
    if not (aux.empty):
      df_to_label.loc[aux.index, 'attack'] = 1

def make_subdataset(dataset, features_to_extract):
  df_nuevo = dataset[features_to_extract]
  return df_nuevo

def read_df(path):
    return pd.read_csv(path, low_memory=False)

def to_csv(path,dataframe):
    dataframe.to_csv(path)
    print("File created sucessfully at: {}".format(path))

def drop_nulls(dataframe):
    dataf = dataframe.replace(" NULL", np.NaN)
    dataf = dataf.dropna()
    return dataf
    
######################################################################
############################## EXECUTE ###############################
######################################################################

if __name__ == '__main__':    
  # 1 Preparing dataset
  df_no_labeled         = read_df(r.path_raw_data)
  df_labeled            = df_no_labeled[(df_no_labeled.UUID >= 1461851815453) & ((df_no_labeled.UUID <= 1463565596193))]    
  df_labeled['attack'] = 0
  
  # 2 Treating moriarty
  preprocess_moriarty(r.moriarty_to_fix, r.moriarty_fix)
  df_Mor      = read_df(r.moriarty_fix)
  
  # 3 Labeling
  label_dataset(df_labeled, df_Mor, 60000)
  df_labeled = drop_nulls(df_labeled)
  
  # 4 Dividing the data
  df_attacks = df_labeled[(df_labeled.attack == 1)]
  df_no_attacks = df_labeled[(df_labeled.attack == 0)]
   
  # 5 Saving the new labeled datasets
  to_csv(r.path_raw_attacks , df_attacks)
  to_csv(r.path_raw_no_attacks, df_no_attacks)

  
  
  
  
  
  
  
  
  