#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

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
    print(aux)
    if not (aux.empty):
      df_to_label.loc[aux.index, 'attack'] = 1

def make_subdataset(dataset, features_to_extract):
  df_nuevo = dataset[features_to_extract]
  return df_nuevo

# Work in progress
def make_equality_inter_datasets(df_merge1, df_merge2):
  probe_1_inf      = df_merge1.iloc[0,1]
  probe_1_sup      = df_merge1.iloc[1,1]
  
  probe_2_inf      = df_merge2.iloc[0,1]
  probe_2_sup      = df_merge2.iloc[1,1]
  
  probe_interval_1 = round((probe_1_sup - probe_1_inf), -3)
  probe_interval_2 = round((probe_2_sup - probe_2_inf), -3)
  
  if (probe_interval_1 // probe_interval_2 >= 1):
    adaptative_new_registers = probe_interval_1 // probe_interval_2
    
    for index, row in df_merge1.iterrows():
      # Hacer pd.cut(UUID, adaptative_new_registers)
      pass
    
  else:
    adaptative_new_registers = probe_interval_2 // probe_interval_1
    pass

def read_df(path):
    return pd.read_csv(path, low_memory=False)

def to_csv(path,dataframe):
    dataframe.to_csv(path)
    print("File preprocessed.csv created sucessfully")

def drop_nulls(dataframe):
    dataf = dataframe.replace(" NULL", np.NaN)
    dataf = dataf.dropna()
    return dataf
    
######################################################################
############################## EXECUTE ###############################
######################################################################

if __name__ == '__main__':    
  df_T2                = read_df("data/preprocessed.csv")
  df_to_find           = df_T2[(df_T2.UUID >= 1461851815453) & ((df_T2.UUID <= 1463565596193))]    
  df_to_find['attack'] = 0
  preprocess_moriarty("data/Moriarty.csv", "data/Moriarty_fix.csv")
  
  df_Mor      = read_df("data/Moriarty_fix.csv")
  label_dataset(df_to_find, df_Mor, 60000)
  df_to_find = drop_nulls(df_to_find)

  
  
  
  
  
  
  
  
  