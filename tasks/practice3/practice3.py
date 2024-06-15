from pathlib import Path
from typing import Dict, Any, List, Optional
import re
import csv
import os

def count_words(text: str) -> Dict[str, int]:
    """
    Функция для подсчета слов в тексте.

    При подсчете слов - все знаки препинания игнорируются.
    Словом считается непрерывная последовательность длиной больше одного
    символа, состоящая из букв в диапазоне A-Z и a-z.
    Если в последовательности присутствует цифра - это не слово.

    Hello - слово
    Hello7 - не слово

    При подсчете слов регистр букв не имеет значения.

    Результат выполнения функции словарь, в котором:
    ключ - слово в нижнем регистре
    значение - количество вхождений слов в текст

    :param text: текст, для подсчета символов
    :return: словарь, в котором:
             ключ - слово в нижнем регистре
             значение - количество вхождений слов в текст
    """

    # пиши свой код здесь
    words = re.findall(r'\b[A-Za-z]{2,}\b', text)
    word_counts = {}
    for word in words:
        word_lower = word.lower()
        if word_lower.isalpha():  # Проверяем, что слово состоит только из букв
            word_counts[word_lower] = word_counts.get(word_lower, 0) + 1
    
    return word_counts


def exp_list(numbers: List[int], exp: int) -> List[int]:
    """
    Функция, которая возводит каждый элемент списка в заданную степень

    :param numbers: список, состоящий из натуральных чисел
    :param exp: в какую степень возвести числа в списке
    :return: список натуральных чисел
    """

    # пиши свой код здесь
    powered_numbers = [num ** exp for num in numbers]
    return powered_numbers


def get_cashback(operations: List[Dict[str, Any]], special_category: List[str]) -> float:
    """
    Функция для расчета кешбека по операциям.
    За покупки в обычных категориях возвращается 1% от стоимости покупки
    За покупки в special_category начисляют 5% от стоимости покупки

    :param operations: список словарей, содержащих поля
           amount - сумма операции
           category - категория покупки
    :param special_category: список категорий повышенного кешбека
    :return: размер кешбека
    """
    total_cashback = 0
    
    for operation in operations:
        amount = operation['amount']
        category = operation['category']
        
        if category in special_category:
            # 5% кешбек для специальной категории
            cashback = amount * 0.05
        else:
            # 1% кешбек для обычных категорий
            cashback = amount * 0.01
        
        total_cashback += cashback
    
    return total_cashback


def get_path_to_file() -> Optional[Path]:
    """
    Находит корректный путь до тестового файла.

    Если запускать тесты из pycharm - начальная папка - tests
    Если запускать файлы через make tests - начальная папка - корень проекта

    :return: путь до тестового файла tasks.csv
    """
    if Path().resolve().name == 'tests':
        base_path = Path().resolve().parent
    else:
        base_path = Path().resolve()
    return base_path / 'tasks' / 'practice3' / 'tasks.csv'


def csv_reader(header: str) -> int:
    """
    Функция считывает csv файл и подсчитывает количество
    уникальных элементов в столбце.
    Столбец выбирается на основе имени заголовка,
    переданного в переменной header.

    Обратите внимание на структуру файла!
    Первая строка - строка с заголовками.
    Остальные строки - строки с данными.

    Файл для анализа: tasks.csv
    Для того чтобы файл корректно открывался в тестах:
    для получения пути до файла - используйте функцию get_path_to_file
    которая определена перед функцией.

    CSV анализируем с помощью встроенной библиотеки csv

    :param header: название заголовка
    :return: количество уникальных элементов в столбце
    """

    # пиши свой код здесь
    file_path = get_path_to_file('tasks.csv')
    unique_elements = set()

    with open(file_path, mode='r', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)
        headers = next(reader)  # Чтение первой строки как заголовков
        column_index = headers.index(header)  # Нахождение индекса столбца по заголовку

        for row in reader:
            try:
                value = row[column_index]
                unique_elements.add(value)
            except IndexError:
                pass  # Пропускаем строки, которые не соответствуют ожидаемой структуре

    return len(unique_elements)
