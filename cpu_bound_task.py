"""
예제에서 자주 써먹을 cpu bound task 들
"""


def fibonacci(num):
    """
    피보나치 수열 구하기
    """
    if num < 0:
        raise ValueError

    num1, num2 = 0, 1

    for _ in range(num):
        num1, num2 = num2, num1 + num2
    return num2


def factorial(num):
    """
    factorial 구하기
    """
    if num < 0:
        raise ValueError

    res = 1

    for i in range(1, num + 1):
        res *= i
    return res
