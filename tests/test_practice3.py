# DO NOT EDIT
import pytest

from tasks.practice3.practice3 import (
    count_words,
    exp_list,
    get_cashback,
    csv_reader,
)


@pytest.mark.parametrize(
    ('text', 'result'),
    [
        (
            'In the face of ambiguity, refuse the temptation to guess. '
            'NotWord7 7NotWord! 777',
            {
                'in': 1,
                'the': 2,
                'face': 1,
                'of': 1,
                'ambiguity': 1,
                'refuse': 1,
                'temptation': 1,
                'to': 1,
                'guess': 1,
            },
        ),
        ('', {}),
        ('123 - word', {'word': 1}),
        ('word word!', {'word': 2}),
        ('word Word...', {'word': 2}),
        ('NotWord123 Word 111', {'word': 1}),
    ],
)
def test_count_words(text, result):
    assert count_words(text) == result


@pytest.mark.parametrize(
    ('numbers', 'exp', 'result'),
    [([1, 2, 3], 2, [1, 4, 9]), ([9, 11], 5, [59049, 161051])],
)
def test_exp_list(numbers, exp, result):
    assert exp_list(numbers, exp) == result


@pytest.mark.parametrize(
    ('operations', 'special_category', 'result'),
    [
        ([{'amount': 5, 'category': 'home'}], [], 0.05),
        ([{'amount': 5, 'category': 'home'}], ['home'], 0.25),
        ([{'amount': 10, 'category': 'auto'}], ['auto'], 0.5),
        (
            [
                {'amount': 100, 'category': 'auto'},
                {'amount': 77, 'category': 'flowers'},
            ],
            ['auto'],
            5.77,
        ),
    ],
)
def test_get_cashback(operations, special_category, result):
    assert get_cashback(operations, special_category) == result


@pytest.mark.parametrize(
    ('header', 'result'),
    [
        ('IssueType', 3),
        ('Summary', 5),
        ('Project Key', 2),
    ],
)
def test_csv_reader(header, result):
    assert csv_reader(header) == result
