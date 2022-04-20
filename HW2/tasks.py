def task_88(_number: int):
    """
    Task 88 в)
    :param: _number
    :return: Integer with swapped first and last digits of a number
    """

    _number = str(_number)
    return int(_number) if len(_number) == 1 else int(_number[-1] + _number[1:-1] + _number[0])


def task_88g(_number: int):
    """
    Task 88 г)
    :param _number:
    :return:
    """

    _number = str(_number)
    return int("1" + _number + "1")


def task_332(_number):
    """
    Find numbers which match expression:
    n = x**2 + y**2 + z**2 + t**2
    :param _number:
    :return:
    """

    _sqr = int(_number ** 0.5) + 1

    for x in range(_sqr):
        for y in range(_sqr):
            for z in range(_sqr):
                for t in range(_sqr):
                    if x*x + y*y + z*z + t*t == _number:
                        print(f"x={x}|y={y}|z={z}|t={t}")
                        return x, y, z, t