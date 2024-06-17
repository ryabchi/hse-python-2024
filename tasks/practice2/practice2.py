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

    greeting = f"Божиею поспешествующею милостию {name}, император и самодержец Всероссийский, Московский, Киевский, Владимирский, Новгородский; царь Казанский, царь Астраханский, царь Польский, царь Сибирский, царь Херсонеса Таврического, царь Грузинский; государь Псковский и великий князь Смоленский, Литовский, Волынский, Подольский и Финляндский; князь Эстляндский, Лифляндский, Курляндский и Семигальский, Самогитский, Белостокский, Корельский, Тверский, Югорский, Пермский, Вятский, Болгарский и иных; государь и великий князь Новагорода низовския земли, Черниговский, Рязанский, Полотский, Ростовский, Ярославский, Белозерский, Удорский, Обдорский, Кондийский, Витебский, Мстиславский и всея северныя страны повелитель; и государь Иверския, Карталинския и Кабардинския земли и области Арменския; Черкасских и Горских князей и иных наследный государь и обладатель, государь Туркестанский; наследник Норвежский, герцог Шлезвиг-Голштейнский, Стормарнский, Дитмарсенский и Ольденбургский и прочая, и прочая, и прочая"

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

    amount = random.randint(100 * 100, 1000000 * 100)
    amount /= 100

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
    
    result = True
    result &= len(phone_number) == 12
    result &= phone_number[:2] == "+7"
    result &= phone_number[1:].isnumeric()

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

    result = current_amount >= float(transfer_amount)

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

    text = text.lower()
    uncultured_words = [plohoe_slovo.lower() for plohoe_slovo in uncultured_words]
    text = text.translate({ord(character): None for character in '\'"'})
    smeshnaya_narezka = text.split(' ')
    smeshnaya_narezka = [slovo for slovo in smeshnaya_narezka if slovo != '']
    result = ' '.join(smeshnaya_narezka)
    for plohoe_slovo in uncultured_words:
        while plohoe_slovo in result:
            result = result.replace(plohoe_slovo, len(plohoe_slovo) * '#')
    result = result.capitalize()
    
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

    porezal = user_info.split(",")
    result = "Фамилия: "             + porezal[0] +\
             "\nИмя: "               + porezal[1] +\
             "\nОтчество: "          + porezal[2] +\
             "\nДата рождения: "     + porezal[3] +\
             "\nЗапрошенная сумма: " + porezal[4]

    return result
