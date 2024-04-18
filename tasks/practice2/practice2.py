from typing import Iterable

UNCULTURED_WORDS = ('kotleta', 'pirog')


def greet_user(name: str) -> str:
    """
    Генерирует приветственную фразу.
    Приветствие не может состоять только из одного имени пользователя.

    :param name: имя пользователя
    :return: приветствие
    """

    greeting = "Guten Tag, " + str.format(name)  # пиши код здесь
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

    import random
    amount = float(random.randint(100, 1000000))  # пиши код здесь
    return amount


def is_phone_correct(phone_number: str) -> bool:
    """
    Функция проверяет, что номер телефона соответствует следующему формату:
    +7xxxxxxxxxx, где x - цифра от 0 до 9

    :param phone_number: предполагаемый номер телефона
    :return: буленовское значение - bool: True - если номер корректны,
                                          False - если номер некорректный
    """

    if phone_number[0:1] == "+" and phone_number[1:].isdigit() and phone_number[1:2] == "7" and len(
            phone_number[1:]) == 11:
        result = True
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

    if current_amount >= float(transfer_amount):  # пиши код здесь
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

    censorship_length = ""  # пиши код здесь
    for uncultured_word in uncultured_words:
        if uncultured_word in text:
            for i in range(len(uncultured_word)):
                censorship_length = censorship_length + "#"
            text = text.replace(uncultured_word, censorship_length)
            censorship_length = ""
    text = text.casefold()
    text = text.split()
    text[0] = text[0].title()
    text = ' '.join(text)
    print(text)
    for word in text:
        for dangerous_symbol in word:
            text = text.replace("'", "")
    for word in text:
        for dangerous_symbol in word:
            text = text.replace('"', '')
    text = ' '.join(text.split())
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

    intermediate_result = user_info.split(",")  # пиши код здесь
    result = (("Фамилия: " + intermediate_result[0] + "\n" + "Имя: " + intermediate_result[1] + "\n" + "Отчество: " +
               intermediate_result[2]) + "\n" + "Дата рождения: " + intermediate_result[
                  3] + "\n" + "Запрошенная сумма: "
              + intermediate_result[4])
    return result

