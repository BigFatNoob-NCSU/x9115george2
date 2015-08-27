__author__ = 'panzer'


def right_justify(s):
    if len(s) < 70 :
        prefix_length = 70 - len(s)
    else :
        prefix_length = 0
    output = " " * prefix_length + s
    print output

right_justify('allen')
