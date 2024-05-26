from typing import Dict, Set

class NoSuchPositionError(Exception):
    def __init__(self, position: str):
        self.position = position

POSITIONS: Dict[str, int] = {
    'CEO': 0,
    'manager': 1,
    'developer': 2,
    'tester': 3,
}

def get_position_level(position_name: str) -> int:

    try:
        return POSITIONS[position_name]
    except KeyError as exp:
        raise NoSuchPositionError(position_name) from exp

class Employee:

    def __init__(self, name: str, position: str, salary: int):
        if not isinstance(salary, int):
            raise ValueError()
        self.name = name
        self.position = position
        self._salary = salary

    def get_salary(self) -> int:

        return self._salary

    def __eq__(self, other: object) -> bool:

        if not isinstance(other, Employee):
            raise TypeError()
        try:
            return get_position_level(self.position) == get_position_level(other.position)
        except NoSuchPositionError as exp:
            raise ValueError()

    def __str__(self):

        return f'name: {self.name} position: {self.position}'

    def __hash__(self):
        return id(self)

class Developer(Employee):

    def __init__(self, name: str, salary: int, language: str):
        super().__init__(name, 'developer', salary)
        self.language = language

class Manager(Employee):

    def __init__(self, name: str, salary: int):
        super().__init__(name, 'manager', salary)