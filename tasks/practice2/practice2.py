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
    greeting = f"Приветсвую, {name}"
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
    amount = random.uniform(100, 1_000_000)
    return round(amount, 2)


def is_phone_correct(phone_number: str) -> bool:
    """
    Функция проверяет, что номер телефона соответствует следующему формату:
    +7xxxxxxxxxx, где x - цифра от 0 до 9

    :param phone_number: предполагаемый номер телефона
    :return: буленовское значение - bool: True - если номер корректны,
                                          False - если номер некорректный
    """
    return True if re.match("[+]7[0-9]{10}", phone_number) else False


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
    return current_amount >= float(transfer_amount)


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
    words_in_text = text.strip().split(" ")
    filtered_text = []
    for i in range(0, len(words_in_text)):
        current_word = words_in_text[i]

        if current_word.isspace():
            continue

        step1 = filter_first_word(current_word) if i == 0 else current_word.lower()
        step2 = remove_quotes(step1)
        step3 = replace_uncultured_words(step2, uncultured_words)
        filtered_text.append(step3)

    return " ".join(filtered_text)


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
    user_info_split = user_info.split(",")
    result = (
            f"Фамилия: {user_info_split[0]}\n" +
            f"Имя: {user_info_split[1]}\n" +
            f"Отчество: {user_info_split[2]}\n" +
            f"Дата рождения: {user_info_split[3]}\n" +
            f"Запрошенная сумма: {user_info_split[4]}"
    )
    # пиши код здесь
    return result


def filter_first_word(word: str) -> str:
    capitalized_first_letter = word[0].capitalize()
    other_letters = word[1:].lower()
    return capitalized_first_letter + other_letters


def remove_quotes(word: str) -> str:
    return "".join(filter(lambda x: x != '\'' and x != '\"', word))


def replace_uncultured_words(word: str, uncultured_words: Iterable[str]) -> str:
    existed_uncultured_words = list(filter(lambda x: x in word, uncultured_words))
    replaced_word = word
    for uncultured_word in existed_uncultured_words:
        replaced_word = replaced_word.replace(uncultured_word, '#' * len(uncultured_word))
    return replaced_word
