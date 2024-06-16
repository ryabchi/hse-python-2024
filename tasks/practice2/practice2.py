import random
import re
from typing import Iterable

UNCULTURED_WORDS = ('kotleta', 'pirog')


def greet_user(name: str) -> str:
    greeting = "Hello " + name
    """
    Генерирует приветственную фразу.
    Приветствие не может состоять только из одного имени пользователя.

    :param name: имя пользователя
    :return: приветствие
    """

    # пиши код здесь
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

    # пиши код здесь
    return amount


def is_phone_correct(phone_number: str) -> bool:
    """
    Функция проверяет, что номер телефона соответствует следующему формату:
    +7xxxxxxxxxx, где x - цифра от 0 до 9

    :param phone_number: предполагаемый номер телефона
    :return: буленовское значение - bool: True - если номер корректны,
                                          False - если номер некорректный
    """
    pattern = r'\+7\d{10}'
    result = bool(re.fullmatch(pattern, phone_number))

    # пиши код здесь
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
    try:
        transfer_amount = float(transfer_amount)  # Преобразование суммы перевода в число
    except ValueError:
        return False

    if current_amount >= transfer_amount:
        return True
    else:
        return False

    # пиши код здесь


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
    text = text.strip().capitalize()

    # Отфильтровываем лишние символы: " ' (двойные и одинарные кавычки)
    filtered_text = ''.join(char for char in text if char not in ['"', "'"])

    # Заменяем запрещенные слова на знак #
    for word in uncultured_words:
        filtered_text = filtered_text.replace(word, '#' * len(word))

    return filtered_text

    return text


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
    user_data = user_info.split(',')

    last_name = user_data[0]
    first_name = user_data[1]
    middle_name = user_data[2]
    dob = user_data[3]
    loan_amount = user_data[4]

    result = f"Фамилия: {last_name}\nИмя: {first_name}\nОтчество: {middle_name}\nДата рождения: {dob}\nЗапрошенная сумма: {loan_amount}"

    return result
