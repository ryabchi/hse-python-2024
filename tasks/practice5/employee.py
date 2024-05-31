from typing import Dict

from .exception import NoSuchPositionError

POSITIONS: Dict[str, int] = {
    'CEO': 0,
    'manager': 1,
    'developer': 2,
    'tester': 3,
}


def get_position_level(position_name: str) -> int:
    """
    Функция возвращает уровень позиции по ее названию.
    Если должности нет в базе поднимается исключение `NoSuchPositionError(position_name)`
    """
    try:
        return POSITIONS[position_name]
    except KeyError as exp:
        raise NoSuchPositionError(position_name) from exp


class Employee:
    """
    Класс - сотрудник

    Возможности:
    1. Реализована возможность сравнения двух сотрудников в зависимости от занимаемой должности - метод __eq__
    2. Возможность получить зарплату через метод get_salary
    """
    name: str
    position: str
    _salary: int

    def __init__(self, name: str, position: str, salary: int):
        """
        Задача: реализовать конструктор класса, чтобы все тесты проходили
        """

        # пиши свой код здесь
        if not (isinstance(name, str)) or not (isinstance(position, str)) or not (isinstance(salary, int)):
            raise ValueError
        self.name = name
        self.position = position
        self._salary = salary

    def get_salary(self) -> int:
        """
        Метод возвращает зарплату сотрудника.
        """

        # пиши свой код здесь
        return self._salary

    def __eq__(self, other: object) -> bool:
        """
        Задача: реализовать метод сравнение двух сотрудников, чтобы все тесты проходили.

        Сравнение происходит по уровню позиции см. `get_position_level`.
        Если что-то идет не так - бросаются исключения. Смотрим что происходит в тестах.
        """

        # пиши свой код здесь
        if isinstance(other, Employee):
            try:
                return get_position_level(self.position) == get_position_level(other.position)
            except NoSuchPositionError:
                raise ValueError

        raise TypeError

    def __str__(self):
        """
        Задача: реализовать строковое представление объекта.
        Пример вывода: 'name: Ivan position manager'
        """

        # пиши свой код здесь
        return f"name: {self.name} position: {self.position}"

    def __hash__(self):
        return id(self)


class Developer(Employee):
    """
    Сотрудник - разработчик
    """

    language: str
    position: str = 'developer'

    def __init__(self, name: str, salary: int, language: str):
        """
        Задача: реализовать конструктор класса, используя конструктор родителя
        """

        # пиши свой код здесь
        self.language = language
        self.name = name
        self._salary = salary


class Manager(Employee):
    """
    Сотрудник - менеджер
    """

    position: str = 'manager'

    def __init__(self, name: str, salary: int):
        """
        Задача: реализовать конструктор класса, используя конструктор родителя
        """

        # пиши свой код здесь
        self.name = name
        self._salary = salary