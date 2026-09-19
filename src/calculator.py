"""Простой калькулятор для демонстрации GitFlow."""


def add(a, b):
    """Сложение двух чисел."""
    return a + b


def subtract(a, b):
    """Вычитание двух чисел."""
    return a - b


def multiply(a, b):
    """Умножение двух чисел."""
    return a * b


def divide(a, b):
    """Деление двух чисел."""
    if b == 0 or b == 0.0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(a, b):
    """Возведение в степень."""
    return a ** b


def modulo(a, b):
    """Остаток от деления."""
    if b == 0:
        raise ValueError("Cannot modulo by zero")
    return a % b
