import sys
import operator
from utils import (
    print_cost_matrix,
    print_result,
    read_json_file_to_dict,
    record_result
)


def set_name_book(expenses):
    """
    name_book is a dict, key is the code of person, value is the name of the person
    {0: 'liuyang', 1: 'liuxinyu', 2: 'lidashuang', 3: 'qianyu'}
    We use code to represent a person during calculation.
    """
    name_amount_dict = {person_name: sum([details.get('amount') for details in expense_details.values()])
                        for person_name, expense_details in expenses.iteritems()}
    names = [k for (k, v) in sorted(name_amount_dict.items(), key=operator.itemgetter(1), reverse=True)]
    if not names:
        print "No people added"
        return None, None
    name_book = {names.index(name): name for name in names}
    cost_matrix = set_cost_matrix(len(name_book))
    return name_book, cost_matrix


def get_code_of_person(person_name, name_book):
    return [key for (key, val) in name_book.items() if val == person_name][0]


def set_cost_matrix(number):
    """
         0 1 2 3
       0   x x x  (1,2,3 should pay $x to 0)
       1 x   x x
       2 x x   x
       3 x x x
    """
    return [[0 for i in range(0, number)] for j in range(0, number)]


def record_expenses(expense, name_book, cost_matrix):
    for person_name, expense_details in expense.iteritems():
        person_code = get_code_of_person(person_name, name_book)
        if person_code is None:
            print person_name, 'is not exists, check the name in ', name_book.values()
            return
        for details in expense_details.values():
            amount = details.get('amount')
            if not amount or amount <= 0:
                continue
            payee = {get_code_of_person(name, name_book): name for name in details['shared_by']} \
                if 'shared_by' in details and details['shared_by'] else name_book
            print person_name, 'paid', amount, 'for', payee
            for code, name in payee.iteritems():
                if code != person_code:
                    cost_matrix[person_code][code] += float(amount)/(len(payee))
    return cost_matrix


def normalize_cost_matrix(matrix):
    rows = len(matrix)
    if rows < 1:
        print 'Matrix is empty'
        return
    cols = len(matrix[0])
    for i in range(0, rows):
        for j in range(i+1, cols):
            matrix[i][j] -= matrix[j][i]
            matrix[j][i] = 0
    return matrix


def minimize_cost_matrix(matrix):
    matrix = normalize_cost_matrix(matrix)
    print '\nNormalized matrix...'
    print_cost_matrix(matrix)
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(rows-1, 0, -1):
        for j in range(i, cols):
            if matrix[i][j] == 0:
                continue
            for k in range(i-1, -1, -1):
                current_cell = matrix[i][j]
                up_left = matrix[k][i]
                if up_left == 0 or current_cell == 0 or (up_left < 0 and current_cell < 0):
                    continue
                if up_left <= current_cell:
                    matrix[i][j] -= matrix[k][i]
                    matrix[k][j] += matrix[k][i]
                    matrix[k][i] = 0
                elif up_left > current_cell:
                    matrix[k][i] -= current_cell
                    matrix[k][j] += matrix[i][j]
                    matrix[i][j] = 0
    print '\nFinal matrix:'
    print_cost_matrix(matrix)
    return matrix


def main():
    args = sys.argv[1:]
    file_name = args[0]
    record = args[1] if len(args) >= 2 else False
    expense = read_json_file_to_dict(file_name)
    print 'Initialize people and expenses...'
    name_book, cost_matrix = set_name_book(expense)
    if name_book is None or cost_matrix is None:
        print 'Name book is None or cost matrix is None'
        return
    print 'Name book:', name_book
    cost_matrix = record_expenses(expense, name_book, cost_matrix)
    print '\nFirst pass cost matrix:'
    print_cost_matrix(cost_matrix)
    cost_matrix = minimize_cost_matrix(cost_matrix)
    print '\nMinimized result:'
    result = print_result(name_book, cost_matrix)
    if record == "save":
        record_result("result.txt", result)


if __name__ == '__main__':
    main()
