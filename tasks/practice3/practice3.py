from pathlib import Path
from typing import Dict, Any, List, Optional
import csv

import tasks


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

    punctuation_symbols = (".", "?", ",", "!", ":", ";", "-", "—")
    counter = 0
    for i in text:
        if i in punctuation_symbols:
            text = text.replace(i, "")
    text = text.lower().split()
    processed_text = ""
    dictionary = dict()
    for word in range(len(text)):
        counter = 0
        if any(character.isdigit() for character in text[word]):
            counter = 0
        else:
            counter = counter + 1
            if text[word] in processed_text:
                counter = counter + 1
            else:
                processed_text = processed_text + " " + text[word]
        if counter > 0:
            dictionary[text[word]] = counter
    dictionary = sorted(dictionary.items())
    dictionary = dict(dictionary)
    print(dictionary)
    return dictionary


def exp_list(numbers: List[int], exp: int) -> List[int]:
    """
    Функция, которая возводит каждый элемент списка в заданную степень

    :param numbers: список, состоящий из натуральных чисел
    :param exp: в какую степень возвести числа в списке
    :return: список натуральных чисел
    """

    for i in range(len(numbers)):  # пиши свой код здесь
        numbers[i] = int(numbers[i]) ** int(exp)
    return numbers


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

    cashback = 0
    cat = [i['category'] for i in operations]
    am = [i['amount'] for i in operations]
    for i in range(len(cat)):
        if cat[i] in special_category:
            cashback = cashback + 0.05 * float(am[i])
        else:
            cashback = cashback + 0.01 * float(am[i])
    return cashback


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

    file_path = get_path_to_file()
    unique_elements = set()
    with open(file_path, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        header_row = next(reader)
        column_index = header_row.index(header)
        for row in reader:
            unique_elements.add(row[column_index])
    return len(unique_elements)

