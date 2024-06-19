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
        self.name = name
        if not isinstance(name, str):
            raise ValueError('name must be a string')
        self.position = position
        if not isinstance(position, str):
            raise ValueError('position must be a string')
        self._salary = salary
        if not isinstance(salary, int):
            raise ValueError('salary must be int')
        # пиши свой код здесь

    def get_salary(self) -> int:
        """
        Метод возвращает зарплату сотрудника.
        """
        return self._salary
        # пиши свой код здесь

    def __eq__(self, other: object) -> bool:
        """
        Задача: реализовать метод сравнение двух сотрудников, чтобы все тесты проходили.

        Сравнение происходит по уровню позиции см. `get_position_level`.
        Если что-то идет не так - бросаются исключения. Смотрим что происходит в тестах.
        """
        if not isinstance(other, Employee):
            raise TypeError("Cannot compare Employee with non-Employee object")
        try:
            return get_position_level(self.position) == get_position_level(other.position)
        except NoSuchPositionError:
            raise ValueError("Cannot compare Employee objects with undefined positions")
        # пиши свой код здесь

    def __str__(self):
        """
        Задача: реализовать строковое представление объекта.
        Пример вывода: 'name: Ivan position manager'
        """
        return f'name: {self.name} position: {self.position}'
        # пиши свой код здесь

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
        super().__init__(name, self.position, salary)
        self.language = language
        # пиши свой код здесь


class Manager(Employee):
    """
    Сотрудник - менеджер
    """

    position: str = 'manager'

    def __init__(self, name: str, salary: int):
        """
        Задача: реализовать конструктор класса, используя конструктор родителя
        """
        super().__init__(name, self.position, salary)
        # пиши свой код здесь
