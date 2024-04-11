# DO NOT EDIT
import pytest

from tasks.practice2.practice2 import (
    greet_user,
    get_amount,
    is_phone_correct,
    is_amount_correct,
    moderate_text,
    create_request_for_loan,
    UNCULTURED_WORDS,
)


def test_greet_user():
    name = 'Ivan'
    result = greet_user(name)
    assert name in result
    assert len(result) > len(name)


def test_get_amount():
    for _ in range(100):
        result = get_amount()
        assert isinstance(result, float)
        assert 100 <= result <= 1000000
        assert len(str(result).split('.')[1]) <= 2


def test_is_phone_correct():
    assert is_phone_correct('+78005553535')


@pytest.mark.parametrize(
    'phone', [
        '88005553535',
        '8800555353545',
        '+88005553535',
        '+780055535ab',
    ]
)
def test_is_phone_correct_fail(phone):
    assert not is_phone_correct(phone)


@pytest.mark.parametrize(
    ('current_amount', 'transfer_amount'), [
        (500.0, '500.0'),
        (500.55, '500.0'),
        (1000.0, '500.0')
    ]
)
def test_is_amount_correct(current_amount, transfer_amount):
    assert is_amount_correct(current_amount, transfer_amount)


@pytest.mark.parametrize(
    ('current_amount', 'transfer_amount'), [
        (500.0, '1000.0'),
        (0, '1000.0')
    ]
)
def test_is_amount_correct_fail(current_amount, transfer_amount):
    assert not is_amount_correct(current_amount, transfer_amount)


@pytest.mark.parametrize(
    ('input_text', 'processed_text'),
    [
        ('  per restaurant  ', 'Per restaurant'),
        ('Per RESTAURANT', 'Per restaurant'),
        ('Per" rest\'aurant  ', 'Per restaurant'),
        ('Per restaurant kotleta!', 'Per restaurant #######!'),
        ('Per restaurant pirog!', 'Per restaurant #####!'),
        ('Per restaurant pirog and kotleta!', 'Per restaurant ##### and #######!'),
    ],
)
def test_moderate_text(input_text, processed_text):
    assert moderate_text(input_text, UNCULTURED_WORDS) == processed_text


@pytest.mark.parametrize(
    ('input_text', 'loan_request'), [
        ('Иванов,Петр,Сергеевич,01.01.1991,10000',
         'Фамилия: Иванов\nИмя: Петр\nОтчество: Сергеевич\nДата рождения: 01.01.1991\nЗапрошенная сумма: 10000'),
        ('Doe,John,Sergeevich,12.12.2000,345',
         'Фамилия: Doe\nИмя: John\nОтчество: Sergeevich\nДата рождения: 12.12.2000\nЗапрошенная сумма: 345'),
    ]
)
def test_create_request_for_loan(input_text, loan_request):
    assert create_request_for_loan(input_text) == loan_request
