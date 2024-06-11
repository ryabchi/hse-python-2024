from typing import Iterable
import random

UNCULTURED_WORDS = ('kotleta', 'pirog')


def greet_user(name: str) -> str:
    """
    Генерирует приветственную фразу.
    Приветствие не может состоять только из одного имени пользователя.

    :param name: имя пользователя
    :return: приветствие
    """

    # пиши код здесь
    greeting = "Hello, " + name + "!"
    return greeting


def get_amount() -> float:
    """
    Генерируем случайную сумму на счете.

    Сумма:
    - в диапазоне от 100 до 1000000
    - float
    - не больше 2-х знаков после запятой

    :return: случайную сумму на счете
    """

    # пиши код здесь
    amount = random.randint(100, 1000000) + random.randint(10, 100) / 100
    return amount


def is_phone_correct(phone_number: str) -> bool:
    """
    Функция проверяет, что номер телефона соответствует следующему формату:
    +7xxxxxxxxxx, где x - цифра от 0 до 9

    :param phone_number: предполагаемый номер телефона
    :return: буленовское значение - bool: True - если номер корректны,
                                          False - если номер некорректный
    """

    # пиши код здесь
    result = False
    if len(phone_number) == 12 and phone_number[0] == '+' and phone_number[1] == '7':
        result = True
        numbers = "0123456789"
        for i in range(1, 12):
            if phone_number[i] not in numbers:
                result = False
                break
    return result


def is_amount_correct(current_amount: float, transfer_amount: str) -> bool:
    """
    Проверяет возможность осуществления перевода.
    Перевод возможен если выполняется условие:
    - текущий счет (current_amount) больше или равен сумме перевода (transfer_amount)

    :param current_amount: текущий счет
    :param transfer_amount: сумма перевода
    :return: буленовское значение - bool: True - если перевод возможен,
                                          False - если денег недостаточно
    """

    # пиши код здесь
    result = False
    if current_amount >= float(transfer_amount):
        result = True
    return result


def moderate_text(text: str, uncultured_words: Iterable[str]) -> str:
    """
    Модерирует текст по следующим правилам.

    Требования к тексту:
    - Первая буква заглавная, остальные буквы только в нижнем регистре
    - отсутствую лишние пробелы
    - фильтруются 'опасные' символы: " ' (двойные и одинарные кавычки)
    - слова, перечисленные в переменной uncultured_words заменяются на аналогичное количество знаков #

    :param text: исходный текст
    :param uncultured_words: список запрещенных слов
    :return: текст, соответсвующий правилам
    """

    # пиши код здесь
    result = ""
    i = 0
    word = ""
    while i < len(text):
        if text[i] == '"' or text[i] == "'":
            result += ""
        else:
            result += text[i]
        i += 1
    result = result.replace(UNCULTURED_WORDS[0], "#######")
    result = result.replace(UNCULTURED_WORDS[1], "#####")
    line = result.split()
    result = ""
    for i in range(0, len(line)):
        result += line[i] + " "
    result = result.lower()
    if result[0].isalpha():
        result = result[0].upper() + result[1:]
    result = result[:-1]
    return result


def create_request_for_loan(user_info: str) -> str:
    """
    Генерирует заявку на кредит на основе входящей строки.
    Формат входящий строки:

    Иванов,Петр,Сергеевич,01.01.1991,10000

    Что должны вернуть на ее основе:

    Фамилия: Иванов
    Имя: Петр
    Отчество: Сергеевич
    Дата рождения: 01.01.1991
    Запрошенная сумма: 10000

    :param user_info: строка с информацией о клиенте
    :return: текст кредитной заявки
    """

    # пиши код здесь
    user_info = user_info.replace('.', ',')
    user_info = user_info.replace(',', ' ')
    words = user_info.split(' ')
    result = "Фамилия: " + words[0] + "\n" + "Имя: " + words[1] + "\n" + "Отчество: " + words[
        2] + "\n" + "Дата рождения: " + words[3] + "." + words[4] + "." + words[5] + "\n" + "Запрошенная сумма: " + \
             words[6]
    return result


