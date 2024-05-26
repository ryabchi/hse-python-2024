class EmployeeError(Exception):

    position: str

    def __init__(self, position: str):
        self.position = position

class NoSuchPositionError(EmployeeError):

    pass

class TeamError(Exception):
    team_name: str

    def __init__(self, team_name: str):
        self.team_name = team_name

class NoSuchMemberError(TeamError):
    member: 'Employee'

    def __init__(self, team_name: str, member: 'Employee'):
        self.member = member
        super().__init__(team_name)
