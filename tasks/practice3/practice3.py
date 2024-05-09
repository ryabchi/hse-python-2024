import csv
import re
from pathlib import Path
from typing import Dict, Any, List, Optional


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
    splited_text = text.split(' ')
    res = {}
    for word in splited_text:
        if len(word) > 1:
            flag = True
            for i in range(len(word)):
                if word[i].isdigit():
                    flag = False
                    break
            if flag:
                start, end = 0, 0
                while start < len(word) and not word[start].isalpha():
                    start += 1
                if start == len(word):
                    continue
                end = start
                while end < len(word) and word[end].isalpha():
                    end += 1
                if end == len(word):
                    res[word[start:end].lower()] = res.get(word[start:end].lower(), 0) + 1
                    continue
                is_alpha = False
                for i in range(end, len(word)):
                    if word[i].isalpha():
                        is_alpha = True
                        break
                if is_alpha:
                    continue
                res[word[start:end].lower()] = res.get(word[start:end].lower(), 0) + 1
    return res


def exp_list(numbers: List[int], exp: int) -> List[int]:
    """
    Функция, которая возводит каждый элемент списка в заданную степень

    :param numbers: список, состоящий из натуральных чисел
    :param exp: в какую степень возвести числа в списке
    :return: список натуральных чисел
    """

    # пиши свой код здесь
    res = [i ** exp for i in numbers]
    return res


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

    # пиши свой код здесь
    result = 0
    for op in operations:
        if op['category'] in special_category:
            result += op['amount'] * 0.05
        else:
            result += op['amount'] * 0.01

    return result


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
    path_to_file = get_path_to_file()
    total_unique = set()
    with open(path_to_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            total_unique.add(row[header])
    return len(total_unique)
