__author__ = 'panzer'


def do_twice(f, arg):
    f(arg)
    f(arg)


def print_twice(s):
    print s
    print s


def do_four(f, arg):
    do_twice(f, arg)
    do_twice(f, arg)

do_twice(print_twice, 'spam')

do_four(print_twice, 'spam')
