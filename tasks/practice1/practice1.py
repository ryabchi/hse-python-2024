def concatenate_strings(a: str, b: str) -> str:
    result = a + b
    return result


def calculate_salary(total_compensation: int) -> float:
    tax_rate = 0.13
    tax_amount = total_compensation * tax_rate
    net_salary = total_compensation - tax_amount
    return net_salary


# pytest tests/test_practice1.py
