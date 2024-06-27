class NoSuchPositionError(Exception):
    def __init__(self, position: str):
        super().__init__(f"No such position: {position}")

class NoSuchMemberError(Exception):
    def __init__(self, member):
        super().__init__(f"No such member: {member}")
