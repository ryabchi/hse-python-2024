class EmployeeError(Exception):
    """
    Исключение связанное с должностью
    """
    position: str

    def __init__(self, position: str):
        self.position = position


class NoSuchPositionError(EmployeeError):
    """ 
    Исключение поднимается, когда нет позиции в бд
    """
    pass


class TeamError(Exception):
    """
    Исключение связанное с командой
    """
    team_name: str

    def __init__(self, team_name: str):
        self.team_name = team_name


class NoSuchMemberError(TeamError):
    """
    Исключение поднимается, когда нет сотрудника в команде
    """
    member: 'Employee'

    def __init__(self, team_name: str, member: 'Employee'):
        self.member = member

        super().__init__(team_name)
