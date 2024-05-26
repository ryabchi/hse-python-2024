from typing import Iterable
import random
import re
UNCULTURED_WORDS = ('kotleta', 'pirog')


def greet_user(name: str) -> str:
    greeting = f"Привет, {name}!"
    return greeting



def get_amount() -> float:
    result = round(random.uniform(100, 1000000), 2)
    return result


def is_phone_correct(phone_number: str) -> bool:
    p = re.compile(r'^\+7\d{10}$')
    result = bool(p.match(phone_number))

    return result


def is_amount_correct(current_amount: float, transfer_amount: str) -> bool:

    try:
        transfer_amount = float(transfer_amount)
    except ValueError:
        return False
    return current_amount >= transfer_amount


def moderate_text(text: str, uncultured_words: Iterable[str]) -> str:

    text = text.replace('"', '').replace("'", "")


    text = text.strip().capitalize()


    words = text.split()
    uncultured_words_lower = {word.lower() for word in uncultured_words}

    for i, word in enumerate(words):
        word_clean = word.lower().strip(",.?!")
        if word_clean in uncultured_words_lower:
            words[i] = '#' * len(word_clean) + word[len(word_clean):]

    result = ' '.join(words)

    return result



def create_request_for_loan(user_info: str) -> str:

    fam, name, patronymic, date, amount = user_info.split(',')

    request = (f"Фамилия: {fam}\n"
               f"Имя: {name}\n"
               f"Отчество: {patronymic}\n"
               f"Дата рождения: {date}\n"
               f"Запрошенная сумма: {amount}")

    return request

