from typing import Set
from .employee import Employee, Manager
from .exception import NoSuchMemberError


class Team:
    """
    Класс - команда.
    У каждой команды есть менеджер, название и участники.

    Возможности:
    - добавление участников
    - удаление участника из команды
    - просмотр базовой информации об участниках
    - получение списка участников
    """

    name: str
    manager: Manager
    __members: Set[Employee]

    def __init__(self, name: str, manager: Manager):
        """
        Задача:
        Реализовать конструктор класса.
        Конструктор должен присвоить значения публичным атрибутам
        и инициализировать контейнер `__members`
        """
        if isinstance(name, str) and isinstance(manager, Manager):
            self.name = name
            self.manager = manager
            self.__members = set()
        else:
            raise ValueError


    def add_member(self, member: Employee) -> None:
        """
        Задача: реализовать метод добавления участника в команду.
        Добавить можно только работника.
        """
        if isinstance(member, Employee):
            self.__members.add(member)
        else:
            raise TypeError



    def remove_member(self, member: Employee) -> None:
        """
        Задача: реализовать метод удаления участника из команды.
        Если в команде нет такого участника поднимается исключение `NoSuchMemberError`
        """
        if isinstance(member, Employee):
            if member in self.__members:
                self.__members.remove(member)
            else:
                raise NoSuchMemberError(self.name, member)
        else:
            raise TypeError

    def get_members(self) -> Set[Employee]:
        """
        Задача: реализовать метод возвращения списка участков команды та,
        чтобы из вне нельзя было поменять список участников внутри класса
        """
        return self.__members.copy()

    def __str__(self) -> str:
        return 'team: {} manager: {} number of members: {}'.format(self.name, self.manager.name, str(len(self.__members)))

    def show(self) -> None:
        """
        DO NOT EDIT!
        Данный метод нельзя редактировать!

        Метод показывает информацию о команде в формате:
        `'team: {team_name} manager: {manager_name} number of members: {members_count)}'`

        Задача: доработать класс таким образом, чтобы метод выполнял свою функцию, не меняя содержимое
        этого метода
        """
        print(self)
