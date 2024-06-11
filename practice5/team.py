from typing import Set
from .employee import Employee, Manager
from .exception import NoSuchMemberError

class Team:
    name: str
    manager: Manager
    __members: Set[Employee]

    def __init__(self, name: str, manager: Manager):
        self.name = name
        self.manager = manager
        self.__members = set()

    def add_member(self, member: Employee) -> None:
        if not isinstance(member, Employee):
            raise TypeError("Member must be an instance of Employee")
        self.__members.add(member)

    def remove_member(self, member: Employee) -> None:
        if not isinstance(member, Employee):
            raise TypeError("Member must be an instance of Employee")
        if member not in self.__members:
            raise NoSuchMemberError(self.name, member)
        self.__members.remove(member)

    def get_members(self) -> Set[Employee]:
        return self.__members.copy()

    def __str__(self):
        return f'team: {self.name} manager: {self.manager.name} number of members: {len(self.__members)}'

    def show(self) -> None:
        print(self)
