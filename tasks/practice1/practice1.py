def concatenate_strings(a: str, b: str) -> str:
    """
    Функция для сложения двух строк.
    Результат сложения запишите в переменную result.

    :param a: число
    :param b: число
    :return: результат сложения
    """

    result = a + b

    return result


def calculate_salary(total_compensation: int) -> float:
    """
    Функция расчета зарплаты, которую сотрудник получит после
    вычета налогов. Ставка налогообложения равна 13%.

    :param total_compensation: сумма зарплаты до вычета налога
    :return: сумма заплаты после вычета налога
    """

    result = total_compensation * (1 - 0.13)

    return result
