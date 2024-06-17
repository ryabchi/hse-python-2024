from typing import Any, Optional


def search_phone(content: Any, name: str) -> Optional[str]:
    """
    Функция поиска номера телефона пользователя в структуре данных.

    Алгоритм работы следующий:
    1) принимаем на вход структуру content, состоящую из словарей,
    списков и строковых ключей в списке
    2) внутри структуры может быть запись следующего формата:
    {
        'name': 'user_name',
        'phone': 'user_phone',
    }

    3) необходимо пройтись по всей структуре
    4) если встречаем словарь, в котором ключ name совпадает с
    аргументом функции name - берем из этого словаря поле phone
    и возвращаем этот телефон из функции
    5) если поле name с таким значением не найдено - возвращаем из
    функции None

    Может пригодиться:

    1) Чтобы проверить, является ли объект списком используйте функцию:
    isinstance(some_object, list)
    если some_object список - результат будет True
    если some_object не список - False

    2) Чтобы проверить, является ли объект словарем используйте функцию:
    isinstance(some_object, dict)


    :param content: словарь или список, внутрь которого вложены объекты. Внутри
                      может скрываться номер телефона пользователя
    :param name: имя пользователя, у которого будем искать номер телефона
    :return: номер телефона пользователя или None
    """
    flag = True
    # пиши свой код здесь
    if isinstance(content, list):
        for element in content:
            if isinstance(element, list):
                return search_phone(element, name)
            elif isinstance(element, dict):
                if "name" in element.keys():
                    if element["name"] == name:
                        return element["phone"]
                        flag = False
                else:
                    return search_phone(element, name)
        if flag:
            return None
    elif isinstance(content, dict):
        if "name" in content.keys():
                    if content["name"] == name:
                        return content["phone"]
                    else:
                        return None
        else:
            for element in content.values():
                if isinstance(element, list):
                    return search_phone(element, name)
                elif isinstance(element, dict):
                    if "name" in element.keys():
                        if element["name"] == name:
                            return element["phone"]
                        else:
                            return None
                    else:
                        return search_phone(element, name)