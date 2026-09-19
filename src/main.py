"""Главный модуль приложения."""

from calculator import add, subtract, multiply, divide, power, modulo


def main():
    """Точка входа в приложение."""
    print("=== Калькулятор v0.3.0 ===")  # Берём более новую версию
    print(f"2 + 3 = {add(2, 3)}")
    print(f"10 - 4 = {subtract(10, 4)}")
    print(f"5 * 6 = {multiply(5, 6)}")
    print(f"15 / 3 = {divide(15, 3)}")
    print(f"2 ^ 8 = {power(2, 8)}")
    print(f"17 % 5 = {modulo(17, 5)}")


if __name__ == "__main__":
    main()
