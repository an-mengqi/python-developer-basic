"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*args):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    result = []
    for el in args:
        result.append(el ** 2)
    return result


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_odd(number):
    if (number % 2) != 0:
        return True
    else:
        return False


def is_even(number):
    if (number % 2) == 0:
        return True
    else:
        return False


def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True


def filter_numbers(numbers, filter_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    filtered_result = None
    if filter_type is ODD:
        filtered_result = list(filter(is_odd, numbers))
    elif filter_type is EVEN:
        filtered_result = list(filter(is_even, numbers))
    elif filter_type is PRIME:
        filtered_result = list(filter(is_prime, numbers))
    return filtered_result
