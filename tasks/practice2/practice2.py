from typing import Iterable

UNCULTURED_WORDS = ('kotleta', 'pirog')


def greet_user(name: str) -> str:
    """
    Генерирует приветственную фразу.
    Приветствие не может состоять только из одного имени пользователя.

    :param name: имя пользователя
    :return: приветствие
    """

    greeting = f"Привет, {name}! Рад тебя видеть."
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

    random = __import__('random')
    amount = random.uniform(100, 1000000)
    amount = round(amount, 2)
    return amount


def is_phone_correct(phone_number: str) -> bool:
    """
    Функция проверяет, что номер телефона соответствует следующему формату:
    +7xxxxxxxxxx, где x - цифра от 0 до 9

    :param phone_number: предполагаемый номер телефона
    :return: буленовское значение - bool: True - если номер корректны,
                                          False - если номер некорректный
    """

    result = False
    if phone_number.startswith('+7') and len(phone_number) == 12:
        if phone_number[2:].isdigit():
            result = True
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

    transfer_amount_float = float(transfer_amount)
    result = current_amount >= transfer_amount_float
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
    from typing import Iterable
    text = ' '.join(text.split())
    text = text.lower().capitalize()
    dangers = ["\"", "\'"]
    for symbol in dangers:
        text = text.replace(symbol, '')
    for word in uncultured_words:
        text = text.replace(word, '#' * len(word))
    result = text
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

    user = user_info.split(',')
    result = f"Фамилия: {user[0]}\n" \
             f"Имя: {user[1]}\n" \
             f"Отчество: {user[2]}\n" \
             f"Дата рождения: {user[3]}\n" \
             f"Запрошенная сумма: {user[4]}"
    return result
