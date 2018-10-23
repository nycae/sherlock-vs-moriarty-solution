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
        output_file.write(line_to_write)

        line = input_file.readline()


if __name__ == '__main__':
    from sys import argv
    import argparse

    parser = argparse.ArgumentParser(description='Calculate de average of a column')
    parser.add_argument('input_file', help='Path to csv', type=str)
    parser.add_argument('-n', dest='number_of_rows', help='number of affected rows', type=int)
    parser.add_argument('-c', dest='column_index', help='index of the affected colum', type=int)
    parser.add_argument('output_file', help='Name of the result file', type=str)
    args = parser.parse_args()

    calculateAverage(args.input_file, args.column_index, args.number_of_rows, args.output_file)
