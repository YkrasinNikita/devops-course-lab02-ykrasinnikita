"""Главный модуль приложения."""

from calculator import add, subtract


def main():
    """Точка входа в приложение."""
    print("=== Калькулятор v0.1.0 ===")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"10 - 4 = {subtract(10, 4)}")


if __name__ == "__main__":
    main()
