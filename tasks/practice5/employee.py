from typing import Dict
from .exception import NoSuchPositionError, EmployeeError

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
    name: str
    position: str
    _salary: int

    def __init__(self, name: str, position: str, salary: int):
        if position not in POSITIONS:
            raise ValueError(f"Invalid position: {position}")
        if not isinstance(salary, int) or salary < 0:
            raise ValueError("Salary must be a non-negative integer")
        self.name = name
        self.position = position
        self._salary = salary

    def get_salary(self) -> int:
        return self._salary

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Employee):
            raise TypeError(f"Cannot compare Employee with {type(other)}")
        return get_position_level(self.position) == get_position_level(other.position)

    def __str__(self):
        return f'name: {self.name} position: {self.position}'

    def __hash__(self):
        return id(self)



class Developer(Employee):
    language: str
    position: str = 'developer'

    def __init__(self, name: str, salary: int, language: str):
        super().__init__(name, self.position, salary)
        self.language = language

class Manager(Employee):
    position: str = 'manager'

    def __init__(self, name: str, salary: int):
        super().__init__(name, self.position, salary)

