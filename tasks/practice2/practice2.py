from typing import Iterable

UNCULTURED_WORDS = ('kotleta', 'pirog')


def greet_user(name: str) -> str:
    greeting = f"Привет, {name}! Как дела?"
    return greeting



import random

def get_amount() -> float:
    amount = round(random.uniform(100, 1000000), 2)
    return amount



def is_phone_correct(phone_number: str) -> bool:
    return phone_number.startswith("+7") and len(phone_number) == 12 and phone_number[1:].isdigit()



def is_amount_correct(current_amount: float, transfer_amount: str) -> bool:
    return current_amount >= float(transfer_amount)


def moderate_text(text: str, uncultured_words: Iterable[str]) -> str:
    # Удаление лишних пробелов и фильтрация опасных символов
    text = " ".join(text.split())
    text = text.replace('"', '').replace("'", "")

    # Замена некультурных слов на #
    for word in uncultured_words:
        text = text.replace(word, '#' * len(word))

    # Преобразование первой буквы в заглавную, а остальных в нижний регистр
    text = text.capitalize()

    return text


def create_request_for_loan(user_info: str) -> str:
    parts = user_info.split(",")
    last_name = parts[0]
    first_name = parts[1]
    middle_name = parts[2]
    birth_date = parts[3]
    requested_amount = parts[4]

    request = f"Фамилия: {last_name}\nИмя: {first_name}\nОтчество: {middle_name}\nДата рождения: {birth_date}\nЗапрошенная сумма: {requested_amount}"
    return request

