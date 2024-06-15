from typing import Iterable
import random
import re

UNCULTURED_WORDS = ('kotleta', 'pirog')


def greet_user(name: str) -> str:
    """
    Генерирует приветственную фразу.
    Приветствие не может состоять только из одного имени пользователя.

    :param name: имя пользователя
    :return: приветствие
    """

    greeting = 'Hello, ' + name
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

    amount = round(random.uniform(100, 1000000), 2)
    return amount


def is_phone_correct(phone_number: str) -> bool:
    """
    Функция проверяет, что номер телефона соответствует следующему формату:
    +7xxxxxxxxxx, где x - цифра от 0 до 9

    :param phone_number: предполагаемый номер телефона
    :return: буленовское значение - bool: True - если номер корректны,
                                          False - если номер некорректный
    """
    if len(phone_number) == 12:
        if phone_number[0] + phone_number[1] == '+7':
            flag_of_correct_phone = 0
            for i in range(2, len(phone_number)):
                if not (phone_number[i].isdigit()):
                    flag_of_correct_phone = 1
            if flag_of_correct_phone == 0:
                result = True
            else:
                result = False
        else:
            result = False
    else:
        result = False
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

    transfer_amount = float(transfer_amount)
    if current_amount >= transfer_amount:
        result = True
    else:
        result = False
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
    result = re.sub(" +", " ", text)
    result = re.sub("'", "", result)
    result = re.sub('"', "", result)

    for i in uncultured_words:
        result = re.sub(i, "#" * len(i), result)

    if result[0] == ' ':
        for i in range(len(result)):
            if i != ' ':
                result = result[i + 1:]
                break

    if result[len(result) - 1] == ' ':
        for i in range(len(result) - 1, -1, -1):
            if i != ' ':
                result = result[:i]
                break

    result = result[0].upper() + result[1:].lower()

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

    inf = user_info.split(',')
    result = "Фамилия: " + inf[0] + "\n" + "Имя: " + inf[1] + "\n" + "Отчество: " + inf[2] + "\n" + "Дата рождения: " + \
             inf[3] + "\n" + "Запрошенная сумма: " + inf[4]
    return result
