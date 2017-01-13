import json
from datetime import datetime


def print_cost_matrix(matrix):
    rows = len(matrix)
    for i in range(0, rows):
        print matrix[i]


def print_result(name_book, matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    result = []
    for i in range(0, rows):
        for j in range(i+1, cols):
            if matrix[i][j] > 0:
                a = name_book[j] + ' should pay $' + str(matrix[i][j]) + ' to ' + name_book[i]
                print a
                result.append(a)
            elif matrix[i][j] < 0:
                b = name_book[i] + ' should pay $' + str(0-matrix[i][j]) + ' to ' + name_book[j]
                print b
                result.append(b)
    return result


def read_json_file_to_dict(file_name):
    print 'Read json file', file_name
    try:
        with open(file_name) as data_file:
            data = json.load(data_file)
            data_file.close()
        return data
    except:
        print 'Open file error', file_name


def record_result(file_name, result):
    print "---------------------"
    print 'Record result to file:' + file_name
    with open(file_name, "a") as myfile:
        myfile.write("\n")
        myfile.write(str(datetime.now())+"\n")
        i = 1
        for line in result:
            myfile.write(" " + str(i) + ": " + line+"\n")
            i += 1
        myfile.write("\n")
