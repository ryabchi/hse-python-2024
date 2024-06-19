def concatenate_strings(a: str, b: str) -> str:
    """
    Функция для объединения двух строк.

    :param a: первая строка
    :param b: вторая строка
    :return: объединенная строка
    """
    result = a + b
    return result

def calculate_salary(total_compensation: int) -> float:
    """
    Функция расчета зарплаты после вычета налога.

    :param total_compensation: сумма зарплаты до вычета налога
    :return: сумма зарплаты после вычета налога
    """
    tax_rate = 0.13  # ставка налога
    tax_amount = total_compensation * tax_rate
    result = total_compensation - tax_amount
    return result
