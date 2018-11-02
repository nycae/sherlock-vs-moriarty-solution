# -*- coding: utf-8 -*-
import pandas as pd
import numpy

raw_path            = "data/T2.csv"
column_index        = 5
rows_index          = 3
path_out            = "data/T2_out.csv"
path_preprocessed   = "data/preprocessed.csv"


def calculateAverage(path_to_csv, column_index, rows_affected, path_to_destiny):

    input_file  = open(path_to_csv, 'r')
    output_file = open(path_to_destiny, 'w')

    output_file.write(input_file.readline()) # Column name
    
    # Loop begins
    
    line        = input_file.readline()
    while line:

        list_to_write = line.split(',')
        average = [0.0] * (len(list_to_write) - column_index + 1)
        rows_to_treat = []  

        rows_to_treat.append(line)

        for _ in range(1, rows_affected):
            rows_to_treat.append(input_file.readline())

        for value in average:
            
            index = column_index - 1
            non_null_values = 0
            
            for row in rows_to_treat:
                try:
                    value += float(row.split(',')[index])
                    non_null_values += 1
                except:
                    pass
            try:
                value /= non_null_values
            except ZeroDivisionError:
                value = 0
            index += 1

        line_to_write = ', '.join(map(str, list_to_write))
        line_to_write = line_to_write.replace('"Null"',"NULL") # Para quitar las columnas que son nulas
  
        output_file.write(line_to_write)

        line = input_file.readline()



def get_indexes(path, key_list):
    
    file            = open(path, 'r')
    index           = 0
    to_delete       = []
    attirbute_list  = file.readline().split(',')

    for attribute in attirbute_list:
        
        for key in key_list:
            
            if key in attribute:
                
                to_delete.append(index)

        index += 1

    return list(set(to_delete))


def delete_columns(lista, df):
    
    number_of_deletes = 0
    
    for i in lista:
        df = df.drop(df.columns[i - number_of_deletes], axis=1)
        number_of_deletes += 1
    
    return df
  
def drop_nulls(dataframe):
    dataf       = dataframe.replace(" NULL", numpy.NaN)
    dataf       = dataf.dropna()
    
    return dataf
    
def read_df(path):
    return pd.read_csv(path, low_memory=False)


def to_csv(path,dataframe):
    dataframe.to_csv(path)
#    numpy.savetxt(path, dataframe, delimiter=",", fmt='%s')

######################################################################
############################## EXECUTE ###############################
######################################################################

if __name__ == '__main__':
    
#    calculateAverage(raw_path, column_index, rows_index, path_out)
    
    # We took the Means and the covariances of al the axis except the y, because 3 dimensions are plenty
    # We discarted:
    #   MEDIAN because is highly related to the MEAN
    #   VAR, because is highly related to COVARIANCE
    #   OrientationProbe, because is highly related to X and Z Linear acceleration.
    #   Fourier's Transformation, because we don't know what the heck is that.
    #   Accelerometer, because we're not interested in taking into account acceleration with gravitational force.
    
#    lista = get_indexes(path_out, ['MEDIAN', 'AccelerometerStat','VAR', 'MIDDLE_SAMPLE', 'FFT', 'RotationVector', 'OrientationProbe'])
    lista = get_indexes(path_out, ['MEDIAN','VAR', 'AccelerometerStat','MIDDLE_SAMPLE', 'RotationVector','FFT', 'OrientationProbe', '_y_'])
    
    df_pre_null = read_df(path_out)
    df_pre_null = delete_columns(lista, df_pre_null)
    df_pre_null= drop_nulls(df_pre_null)

    to_csv(path_preprocessed, df_pre_null)

