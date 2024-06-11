from pathlib import Path
from typing import Dict, Any, List, Optional
import csv

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

    text = text.lower()
    numbers = "0123456789"
    sybmols = "!@#№$;%:^&?()-_=+/|.,"
    new_text = ""
    for i in range(len(text)):
        if text[i] in sybmols:
            new_text += ' '
        else:
            new_text += text[i]
    line = new_text.split()
    d = {}
    for i in range(len(line)):
        if len(line[i]) > 1:
            flag_numbers = 0
            for j in range(len(line[i])):
                if line[i][j] in numbers:
                    flag_numbers = 1
                    break
            if flag_numbers == 0:
                if line[i] not in d:
                    d[line[i]] = 1
                else:
                    d[line[i]] += 1

    return d


def exp_list(numbers: List[int], exp: int) -> List[int]:
    """
    Функция, которая возводит каждый элемент списка в заданную степень

    :param numbers: список, состоящий из натуральных чисел
    :param exp: в какую степень возвести числа в списке
    :return: список натуральных чисел
    """

    # пиши свой код здесь
    list = []
    for i in range(len(numbers)):
        list.append(numbers[i]**exp)

    return list


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
    for i in range(len(operations)):
        if operations[i]['category'] in special_category:
            result += operations[i]['amount'] * 0.05
        else:
            result += operations[i]['amount'] * 0.01
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
    rows = []
    d = {}
    with open(get_path_to_file(), "r") as f:
        reader = csv.reader(f)
        file = list(reader)
    number = 0
    for i in range(len(file[0])):
        if file[0][i] == header:
            number = i

    for i in range(1,len(file)):
        d[file[i][number]] = 0

    return len(d)

#print(csv_reader('IssueType'))
