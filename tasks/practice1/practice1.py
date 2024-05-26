def concatenate_strings(a: str, b: str) -> str:
    result = a + b
    return result

def calculate_salary(total_compensation: int) -> float:
    tax = total_compensation * 0.13
    result = total_compensation - tax
    return result
