from pathlib import Path
from typing import Dict, Any, List, Optional
import csv
import string

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
    word_count = {}
    string.punctuation
    for p in string.punctuation:
        if p in text:
            text = text.replace(p, '')
    text_low = text.lower()

    words = text_low.split()
    for word in words:
        if any(char.isdigit() for char in word) == False:
            word_count[word] = word_count.get(word, 0) + 1
    return word_count
    # word_count = {}
    # word = ""
    # for char in text:
    #     if char.isalpha():
    #         word += char.lower()
    #     else:
    #         if word:
    #             word_count[word] = word_count.get(word, 0) + 1
    #             word = ""
    # if word:
    #     word_count[word] = word_count.get(word, 0) + 1
    # return word_count


def exp_list(numbers: List[int], exp: int) -> List[int]:
    """
    Функция, которая возводит каждый элемент списка в заданную степень

    :param numbers: список, состоящий из натуральных чисел
    :param exp: в какую степень возвести числа в списке
    :return: список натуральных чисел
    """

    for i in range(len(numbers)):
        numbers[i] = numbers[i] ** exp

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

    result = 0
    for operation in operations:
        amount = operation.get('amount', 0)
        category = operation.get('category', '')
        if category in special_category:
            result += amount * 0.05
        else:
            result += amount * 0.01
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

    def get_path_to_file(filename: str) -> str:
        return str(Path(__file__).parent / filename)

    with open(get_path_to_file('tasks.csv'), 'r', newline='') as file:
        csv_reader = csv.reader(file)

        headers = next(csv_reader)

        try:
            header_index = headers.index(header)
        except ValueError:
            raise ValueError(f'Header "{header}" not found')

        unique_elements = set()
        
        for row in csv_reader:
            unique_elements.add(row[header_index])

        return len(unique_elements)


