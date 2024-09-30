from functools import reduce
from memory_profiler import profile

# Функция для фильтрации четных чисел и возведения в квадрат
def process_numbers(numbers):
    for n in numbers:
        if n % 2 == 0:  # Проверяем, является ли число четным
            yield n ** 2  # Возвращаем квадрат четного числа

@profile
def main():
    # Исходный список чисел
    numbers = range(1, 11)  # Используем range для генерации чисел от 1 до 10

    # Генератор на основе обработки чисел
    squared_even_numbers = process_numbers(numbers)

    # Суммируем квадратные значения без создания списка
    total_sum = sum(squared_even_numbers)

    print("Сумма квадратов четных чисел:", total_sum)

    # Ожидание нажатия клавиши Enter перед закрытием
    input("Нажмите Enter, чтобы завершить программу...")

if __name__ == "__main__":
    main()
