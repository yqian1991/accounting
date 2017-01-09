import json


def print_cost_matrix(matrix):
    rows = len(matrix)
    for i in range(0, rows):
        print matrix[i]


def print_result(name_book, matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(0, rows):
        for j in range(i+1, cols):
            if matrix[i][j] > 0:
                print name_book[j], 'should pay', '$'+str(matrix[i][j]), 'to', name_book[i]
            elif matrix[i][j] < 0:
                print name_book[i], 'should pay', '$'+str(0-matrix[i][j]), 'to', name_book[j]


def read_json_file_to_dict(file_name):
    print 'Read json file', file_name
    try:
        with open(file_name) as data_file:
            data = json.load(data_file)
            data_file.close()
        return data
    except:
        print 'Open file error', file_name