from math import log


def validate_number(number, least=None, largest=None):
    if not isinstance(number, int):
        raise ValueError("Incorrect number")
    if isinstance(least, int) and least >= int(number):
        raise ValueError("Incorrect number")
    elif isinstance(largest, int) and largest < int(number):
        raise ValueError("Incorrect number")
    else:
        return int(number)


def _is_prime(n):
    if n == 2 or n == 3:
        return True
    elif n % 2 == 0:
        raise ValueError("Incorrect number")
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            raise ValueError("Incorrect number")
    return True


def check_possibility(n):
    return n % 4 == 1


def find_pairs(n, one_already=False):
    result_dict = {}
    for x in range(1, int((n-1)**0.5)+1):
        for y in range(1, int((n-1)**0.5)+1):
            if x**2 + y**2 == n:
                result_dict[x] = y
                if one_already:
                    return result_dict
    return result_dict


def check_pair(n):
    my_dict = find_pairs(n)
    result_dict = {}
    for i in my_dict.items():
        if int(i[0]) >= int(i[1]):
            result_dict[i[0]] = i[1]
    return result_dict


def task_107(m, num=4):
    validate_number(m, 1)
    return int(log(m-1, num))


def task_243a(n):
    if _is_prime(validate_number(n, 1)) and check_possibility(n):
        return find_pairs(n, True)
    else:
        raise BaseException("We can`t present your number as sums of two squares")


def task_243b(n):
    if _is_prime(validate_number(n, 1)) and check_possibility(n):
        result_lst = []
        for i in check_pair(n).items():
            result_lst.append(i)
        return result_lst
    else:
        raise BaseException("We can`t present your number as sums of two squares")

