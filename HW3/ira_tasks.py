"""Ira`s tasks for internship"""
from math import log


def validate_number(number, least=None, largest=None):
    """Function for validating number"""
    try:
        number = int(number)
    except TypeError:
        TypeError("Incorrect number")

    if isinstance(least, int) and least >= int(number):
        raise ValueError("Incorrect number")
    elif isinstance(largest, int) and largest < int(number):
        raise ValueError("Incorrect number")
    else:
        return int(number)


def _is_prime(n):
    """Function for checking is number prime"""
    if n == 2 or n == 3:
        return True
    elif n % 2 == 0:
        raise ValueError("Incorrect number")
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            raise ValueError("Incorrect number")
    return True


def check_possibility(n):
    """Function for checking possibility solving taska 243a/b"""
    return n % 4 == 1


def find_pairs(n, one_already=False):
    """Function for finding (x,y) for tasks 243a/b"""
    result_dict = {}
    for x in range(1, int((n-1)**0.5)+1):
        for y in range(1, int((n-1)**0.5)+1):
            if x**2 + y**2 == n:
                result_dict[x] = y
                if one_already:
                    return result_dict
    return result_dict


def check_pair(n):
    """Function for finding (x,y) for tasks 243a/b where x>y"""
    my_dict = find_pairs(n)
    result_dict = {}
    for i in my_dict.items():
        if int(i[0]) >= int(i[1]):
            result_dict[i[0]] = i[1]
    return result_dict


def task_107(m=4):
    """Implementation of task 107"""
    number = input("Enter number > 1: ")
    number = validate_number(number, 1)
    print(int(log(number-1, m)))
    return int(log(number-1, m))


def task_243a():
    """Implementation of task 243a"""
    number = input("Enter number > 1: ")
    number = validate_number(number, 1)
    if _is_prime(validate_number(number, 1)) and check_possibility(number):
        return find_pairs(number, True)
    else:
        raise BaseException("We can`t present your number as sums of two squares")


def task_243b():
    """Implementation of task 243b"""
    number = input("Enter number > 1: ")
    number = validate_number(number, 1)
    if _is_prime(validate_number(number, 1)) and check_possibility(number):
        result_lst = []
        for i in check_pair(number).items():
            result_lst.append(i)
        return result_lst
    else:
        raise BaseException("We can`t present your number as sums of two squares")
