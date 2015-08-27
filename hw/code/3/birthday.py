from __future__ import division, print_function
import random

__author__ = 'panzer'


def has_duplicates(lst):
    """
    Computes if a list has duplicate elements
    :param lst: List to check in
    :return: True if it contains duplicate, else false
    """
    if lst is None or not len(lst):
        return False
    sorted_list = sorted(lst)
    for i in range(len(sorted_list)-1):
        if sorted_list[i] == sorted_list[i+1]:
            return True
    return False


def random_list(size):
    """
    Creates a random integer list of a given size
    :param size: Size of the list to be created
    :return: Integer list of a given size
    """
    lst = []
    for _ in range(size):
        lst.append(random.randint(1, 365))
    return lst


def estimate_same_day(size, repeats=100):
    """
    Estimate probability of a list having
    :param size:
    :param repeats:
    :return:
    """
    dup_count = 0
    for _ in range(repeats):
        birthdays = random_list(size)
        if has_duplicates(birthdays):
            dup_count += 1
    return dup_count/repeats

if __name__ == '__main__':
    s = 23
    r = 10000
    print("Size of list =  {}".format(s))
    print("Times repeated  = {}".format(r))
    print("Probability of list containing same day = {}".format(round(estimate_same_day(s, r), 4)))
