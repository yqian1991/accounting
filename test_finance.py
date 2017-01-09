from finance import set_name_book, get_code_of_person


def test_set_name_book():
    print 'Run unit tests...'
    print 'Test when file is empty'
    expense = {}
    name_book, cost_matrix = set_name_book(expense)
    print '   -', name_book is None
    print '   -', cost_matrix is None
    print 'Test set name book and cost matrix'
    expense = {
        "liuyang": {
            "1": {
                "amount": 10
            }

        },
        "lidashuang": {
            "1": {
                "amount": 20
            }
        }
    }
    name_book, cost_matrix = set_name_book(expense)
    print '   -', len(cost_matrix) == len(expense)
    print '   -', len(cost_matrix[0]) == len(expense)
    print 'Test get_code_of_person...'
    ret = get_code_of_person(u'liuyang', name_book)
    print '   -', name_book[ret] == u'liuyang'


if __name__ == '__main__':
    test_set_name_book()
