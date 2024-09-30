from functools import reduce

# Функция для фильтрации четных чисел
def is_even(n):
    return n % 2 == 0

# Функция для возведения числа в квадрат
def square(n):
    return n ** 2

# Функция для суммирования двух чисел
def add(x, y):
    return x + y

@profile
def main():
    # Исходный список чисел
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Используем filter для получения четных чисел
    even_numbers = list(filter(is_even, numbers))
    print("Четные числа:", even_numbers)

    # Используем map для возведения четных чисел в квадрат
    squared_numbers = list(map(square, even_numbers))
    print("Четные числа в квадрате:", squared_numbers)

    # Используем reduce для суммирования квадратов
    total_sum = reduce(add, squared_numbers)
    print("Сумма квадратов четных чисел:", total_sum)

    # Ожидание нажатия клавиши Enter перед закрытием
    input("Нажмите Enter, чтобы завершить программу...")

if __name__ == "__main__":
    main()
