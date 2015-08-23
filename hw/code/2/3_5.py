__author__ = 'panzer'


def make_square(rows):
    """
    Make a square with number of
    rows = 'rows'
    :param rows - integer
    """
    row_length = rows * 5
    for i in range(row_length + 1):
        for j in range(row_length + 1):
            if i % 5 == 0 and j % 5 == 0:
                print '+ ',
            elif i % 5 == 0:
                print '- ',
            elif j % 5 == 0:
                print '/ ',
            else:
                print '  ',
        print ''

make_square(4)

