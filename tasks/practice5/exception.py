class EmployeeError(Exception):
    """
    Исключение связанное с должностью
    """
    position: str

    def __init__(self, position: str):
        self.position = position

    def __str__(self):
        raise f"EmployeeError: {self.position}"


class NoSuchPositionError(EmployeeError):
    """ 
    Исключение поднимается, когда нет позиции в бд
    """
    def __str__(self):
        return f"NoSuchPositionError: {self.position} position does not exist"


class TeamError(Exception):
    """
    Исключение связанное с командой
    """
    team_name: str

    def __init__(self, team_name: str):
        self.team_name = team_name

    def __str__(self):
        return f"TeamError in team: {self.team_name}"


class NoSuchMemberError(TeamError):
    """
    Исключение поднимается, когда нет сотрудника в команде
    """
    member: 'Employee'

    def __init__(self, team_name: str, member: 'Employee'):
        self.member = member
        super().__init__(team_name)

    def __str__(self):
        return f"NoSuchMemberError: Member {self.member.name} does not exist in team {self.team_name}"
