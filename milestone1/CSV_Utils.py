#!/usr/bin/python3

def calculateAverage(path_to_csv, column_index, rows_affected, path_to_destiny):

    input_file = open(path_to_csv, 'r')
    output_file = open(path_to_destiny, 'w')
    input_file.readline() #ignore the first line
    line = input_file.readline()

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
        line_to_write = line_to_write.replace('"Null"',"NULL") # This replace is to eliminate this annoying nulls


        output_file.write(line_to_write)

        line = input_file.readline()


def normalize_filtered_data(path):

    import pandas as pd
    from sklearn import preprocessing
    from sklearn.decomposition import PCA
    import numpy as np

    file = pd.read_csv(path, low_memory=False)

    exclude = ['UserID', 'UUID', 'Version', 'TimeStemp', "RotationVector_cosThetaOver2_MEAN", "RotationVector_cosThetaOver2_MEDIAN", "RotationVector_cosThetaOver2_MIDDLE_SAMPLE"]
    df_ex = file.loc[:, file.columns.difference(exclude)]
    df_ex = df_ex.replace(" NULL", np.NaN)
    
    df_ex = df_ex.dropna()
    
    min_max_scaler = preprocessing.MinMaxScaler()
    df_norm = min_max_scaler.fit_transform(df_ex)
        
    return df_norm

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

if __name__ == '__main__':
    from sys import argv
    import argparse

    print(len(get_indexes('T2.csv', ['Gyroscope', 'MEDIAN', 'VAR', 'RotationVector', 'FFT'])))

    parser = argparse.ArgumentParser(description='Calculate de average of a column')
    parser.add_argument('input_file', help='Path to csv', type=str)
    parser.add_argument('-n', dest='number_of_rows', help='number of affected rows', type=int)
    parser.add_argument('-c', dest='column_index', help='index of the affected colum', type=int)
    parser.add_argument('output_file', help='Name of the result file', type=str)
    args = parser.parse_args()

    calculateAverage(args.input_file, args.column_index, args.number_of_rows, args.output_file)
