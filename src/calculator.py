"""Простой калькулятор для демонстрации GitFlow."""


def add(a, b):
    """Сложение двух чисел."""
    return a + b


def subtract(a, b):
    """Вычитание двух чисел."""
    return a - b


# TODO: добавить функции multiply и divide


def power(a, b):
    """Возведение в степень."""
    return a ** b


def modulo(a, b):
    """Остаток от деления."""
    if b == 0:
        raise ValueError("Cannot modulo by zero")
    return a % b
