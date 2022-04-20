from math import log


def enter_number_task_1():
    while True:
        m = int(input("Enter number > 1: "))
        if m <= 1:
            print("Your number need to be more than 1. Enter again: ")
        else:
            return m


def enter_number_task_2_3():
    while True:
        n = int(input("Enter prime number: "))
        if not _is_prime(n):
            print("Your number isn`t prime. Enter again: ")
        else:
            return n


def _is_prime(n):
    if n == 2 or n == 3:
        return True
    elif n % 2 == 0 or n < 2:
        return False
    else:
        for i in range(3, int(n**0.5)+1, 2):
            if n % i == 0:
                return False
        return True


def check_possibility(n):
    return n % 4 == 1


def find_pair(n):
    result_dict = {}
    for x in range(1, int((n-1)**0.5)+1):
        for y in range(1, int((n-1)**0.5)+1):
            if x**2 + y**2 == n:
                result_dict[x] = y
    return result_dict


def check_pair(n):
    my_dict = find_pair(n)
    result_dict = {}
    for i in my_dict.items():
        if int(i[0]) >= int(i[1]):
            result_dict[i[0]] = i[1]
    return result_dict


def task1(m, num = 4):
    return int(log(m-1, num))


def task2(n):
    if check_possibility(n):
        print("Here there are possible pairs present as (x, y)")
        result_lst = []
        for i in find_pair(n).items():
            result_lst.append(i)
        return result_lst
    else:
        return "We can`t present your number as sums of two squares"


def task3(n):
    if check_possibility(n):
        print("Here there are possible pairs present as (x, y)")
        result_lst = []
        for i in check_pair(n).items():
            result_lst.append(i)
        return result_lst
    else:
        return "We can`t present your number as sums of two squares"


if __name__ == "__main__":
    print(f"{'-'*15}Task1{'-'*15}")
    m = enter_number_task_1()
    print(task1(m))
    print(f"{'-' * 15}Task2{'-' * 15}")
    n = enter_number_task_2_3()
    print(task2(n))
    print(f"{'-' * 15}Task3{'-' * 15}")
    print(task3(n))
