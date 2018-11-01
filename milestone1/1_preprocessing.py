# -*- coding: utf-8 -*-
import pandas as pd


path = "data/T2.csv"
column_index = 5
rows_index = 3
path_out = "data/T2_out.csv"
path_preprocessed = "data/preprocessed.csv"

def calculateAverage(path_to_csv, column_index, rows_affected, path_to_destiny):

    input_file = open(path_to_csv, 'r')
    output_file = open(path_to_destiny, 'w')
    namecols = input_file.readline()
    line = input_file.readline()

    output_file.write(namecols)

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
    file = open(path, 'r')
    index = 0
    to_delete = []
    attirbute_list = file.readline().split(',')

    for attribute in attirbute_list:
        for key in key_list:
            if key in attribute:
                to_delete.append(index)

        index += 1

    return set(to_delete)


def delete_columns(lista,df):
    lista = list(lista)
    rango = len(lista)-1
    for i in range(len(lista)):
        df = df.drop(df.columns[[lista[rango]]], axis=1)
        rango -= 1
    return df

def read_df(path):
    df = pd.read_csv(path, low_memory=False)
    return df

def to_csv(path,dataframe):
    dataframe.to_csv(path)
    
######################################################################
############################## EXECUTE   #############################
######################################################################

calculateAverage(path, column_index, rows_index, path_out)
print(len(get_indexes(path_out,['Gyroscope', 'MEDIAN', 'VAR', 'RotationVector','OrientationProbe','MIDDLE_SAMPLE','FFT'])))
lista = get_indexes(path_out,['Gyroscope', 'MEDIAN', 'VAR', 'RotationVector','OrientationProbe','MIDDLE_SAMPLE','FFT'])
print(lista)
df_pre = read_df(path_out)
df_pre_def = delete_columns(lista, df_pre)
to_csv(path_preprocessed,df_pre_def)
