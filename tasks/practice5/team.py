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

        # пиши свой код здесь
        self.name = name
        self.manager = manager
        self.__members = set()

    def add_member(self, member: Employee) -> None:
        """
        Задача: реализовать метод добавления участника в команду.
        Добавить можно только работника.
        """

        # пиши свой код здесь
        if not isinstance(member, Employee):
            raise TypeError("Only instances of Employee can be added to the team")

        self.__members.add(member)

    def remove_member(self, member: Employee) -> None:
        """
        Задача: реализовать метод удаления участника из команды.
        Если в команде нет такого участника поднимается исключение `NoSuchMemberError`
        """

        # пиши свой код здесь
        if not isinstance(member, Employee):
            raise TypeError("Only instances of Employee can be removed from the team")

        if member not in self.__members:
            raise NoSuchMemberError(self.name, member)

        self.__members.remove(member)

    def get_members(self) -> Set[Employee]:
        """
        Задача: реализовать метод возвращения списка участков команды та,
        чтобы из вне нельзя было поменять список участников внутри класса
        """

        # пиши свой код здесь
        try:
            return self.__members.copy()
        except Exception as e:
            print(f"Error getting members: {e}")

    def __str__(self):
        """
        Задача: реализовать строковое представление объекта.
        """
        return f'team: {self.name} manager: {self.manager.name} number of members: {len(self.__members)}'

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
