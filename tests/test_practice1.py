# DO NOT EDIT
import pytest

from tasks.practice1.practice1 import concatenate_strings, calculate_salary


def test_concatenate_strings_success():
    assert concatenate_strings('Hello ', 'World!') == 'Hello World!'


@pytest.mark.parametrize(
    ('total_compensation', 'result'), [
        (100, 87),
        (0, 0),
        (99, 86.13),
    ]
)
def test_calculate_salary(total_compensation, result):
    assert calculate_salary(total_compensation) == result
