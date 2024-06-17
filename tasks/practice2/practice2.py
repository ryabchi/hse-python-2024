import re
from typing import Iterable
import random

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
    return amount


def is_phone_correct(phone_number: str) -> bool:
    """
    Функция проверяет, что номер телефона соответствует следующему формату:
    +7xxxxxxxxxx, где x - цифра от 0 до 9

    :param phone_number: предполагаемый номер телефона
    :return: буленовское значение - bool: True - если номер корректны,
                                          False - если номер некорректный
    """

    pattern = r'\+7\d{10}'  # Паттерн для поиска номера в формате +7xxxxxxxxxx
    match = re.fullmatch(pattern, phone_number)
    return bool(match)


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
    return current_amount >= float(transfer_amount)


def moderate_text(text: str, uncultured_words: Iterable[str]) -> str:
    text = text.lower()
    text = ' '.join(text.split())

    text = text.replace('pirog', '#####').replace("kotleta", '#######')
    text = text.replace('"', '').replace("'", '')

    text = text.capitalize()

    return text


def create_request_for_loan(user_info: str) -> str:
    info_list = user_info.split(',')

    if len(info_list) != 5:
        return "Некорректный формат информации о клиенте"

    last_name = info_list[0]
    first_name = info_list[1]
    middle_name = info_list[2]
    dob = info_list[3]
    loan_amount = info_list[4]

    request_text = f"Фамилия: {last_name}\nИмя: {first_name}\nОтчество: {middle_name}\nДата рождения: {dob}\nЗапрошенная сумма: {loan_amount}"

    return request_text
