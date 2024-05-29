# DO NOT EDIT
import pytest

from tasks.practice4.practice4 import (
    search_phone,
)


IVAN_USER_INFO = {
    'name': 'Ivan',
    'phone': '+78005553535',
}


@pytest.mark.parametrize(
    ('content', 'name', 'phone'),
    [
        (
            {
                'name': 'Serg',
                'phone': '+78005553838',
            },
            'Serg',
            '+78005553838',
        ),
        (
            [
                {
                    'name': 'Serg',
                    'phone': '+78005553838',
                }
            ],
            'Serg',
            '+78005553838',
        ),
        (IVAN_USER_INFO, 'Ivan', '+78005553535'),
        (
            {
                'university': 'HSE',
                'student': IVAN_USER_INFO,
            },
            'Ivan',
            '+78005553535',
        ),
        (
            {
                'university': 'HSE',
                'students': [
                    {
                        'name': 'Petr',
                        'phone': '+78001001005',
                    },
                    IVAN_USER_INFO,
                ],
            },
            'Ivan',
            '+78005553535',
        ),
        (
            {
                'university': 'HSE',
                'groups': [
                    {
                        'group_name': '20pmi-1',
                        'students': [
                            {
                                'name': 'Serg',
                                'phone': '+78001001005',
                            },
                            IVAN_USER_INFO,
                        ],
                    }
                ],
            },
            'Ivan',
            '+78005553535',
        ),
        ([], 'Ivan', None),
        ({'test': {'test': None}}, 'Ivan', None),
    ],
)
def test_search_phone(content, name, phone):
    assert search_phone(content, name) == phone
