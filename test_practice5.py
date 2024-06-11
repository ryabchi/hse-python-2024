import pytest
from tasks.practice5.employee import (
    Employee,
    Developer,
    Manager,
    get_position_level,
    NoSuchPositionError,
)
from tasks.practice5.team import Team
from tasks.practice5.exception import NoSuchMemberError


def test_employee_get_position_level_success():
    assert get_position_level('CEO') == 0


def test_employee_get_position_level_fail():
    with pytest.raises(NoSuchPositionError):
        get_position_level('_')


@pytest.mark.parametrize(
    ('name', 'position', 'salary'),
    [
        ('name', 'developer', 40),
        ('Alex', 'CEO', 100000),
    ],
)
def test_init_employee(name, position, salary):
    employee = Employee(name, position, salary)

    assert employee.name == name
    assert employee.position == position
    assert employee._salary == salary


def test_init_employee_fail():
    with pytest.raises(ValueError):
        Employee('name', 'position', 'salary')


def test_employee_get_salary():
    salary = 100

    employee = Employee('name', 'developer', salary)

    assert employee.get_salary() == salary


@pytest.mark.parametrize(
    ('name', 'position', 'result'),
    [
        ('Ivan', 'manager', 'name: Ivan position: manager'),
        ('Dmitry', 'CEO', 'name: Dmitry position: CEO'),
    ],
)
def test_employee_str(name, position, result):
    employee = Employee(name, position, 100)

    assert str(employee) == result


@pytest.mark.parametrize(
    ('position1', 'position2'),
    [
        ('manager', 'manager'),
        ('tester', 'tester'),
        ('CEO', 'CEO'),
    ],
)
def test_employee_eq_success(position1, position2):
    assert Employee('name1', position1, 40) == Employee('name2', position2, 50)


@pytest.mark.parametrize(
    ('position1', 'position2'),
    [
        ('CEO', 'manager'),
        ('CEO', 'tester'),
        ('CEO', 'developer'),
        ('developer', 'tester'),
        ('tester', 'manager'),
    ],
)
def test_employee_not_eq_success(position1, position2):
    assert Employee('name1', position1, 40) != Employee('name2', position2, 50)


def test_employee_eq_fail():
    employee_1 = Employee('name1', 'developer', 10)
    employee_2 = Employee('name2', 'tester', 30)

    with pytest.raises(TypeError):
        assert employee_1 == 1

    with pytest.raises(ValueError):
        employee_invalid = Employee('name3', 'invalid_position', 10)



@pytest.mark.parametrize(
    ('name', 'salary', 'language'),
    [
        ('Ivan', 1000, 'python'),
        ('Tim', 77, 'java'),
    ],
)
def test_init_developer(name, salary, language):
    employee = Developer(name, salary, language)

    assert employee.name == name
    assert employee.position == 'developer'
    assert employee._salary == salary
    assert employee.language == language


def test_init_manager():
    name = 'name'
    position = 'manager'
    salary = 10

    employee = Manager(name, salary)

    assert employee.name == name
    assert employee.position == position
    assert employee._salary == salary


def test_init_team():
    team_name = 'team_name'
    manager: Manager = Manager('name', 20)
    team: Team = Team(name=team_name, manager=manager)

    assert team.name == team_name
    assert team.manager is manager
    assert team._Team__members == set()


@pytest.fixture()
def team():
    return Team('name', Manager('name', 10))


@pytest.fixture()
def developer():
    return Developer('name', 10, 'python')


def test_team_add_member_success(team, developer):
    team.add_member(developer)

    assert developer in team._Team__members


@pytest.mark.parametrize('member', [1, 'Ivan'])
def test_team_add_member_fail(team, member):
    with pytest.raises(TypeError):
        team.add_member(member)


def test_team_remove_member_success(team, developer):
    team.add_member(developer)

    team.remove_member(developer)

    assert developer not in team._Team__members


def test_team_remove_member_fail(team, developer):
    with pytest.raises(NoSuchMemberError):
        team.remove_member(developer)

    team.add_member(developer)
    team.remove_member(developer)

    with pytest.raises(NoSuchMemberError):
        team.remove_member(developer)


def test_get_members(team, developer):
    members_1 = team.get_members()

    team.add_member(developer)

    members_2 = team.get_members()

    assert members_1 == set()
    assert members_2 == set([developer])
    assert members_1 != members_2


def test_team_show(team):
    assert (
        team.__str__() == f'team: {team.name} manager: {team.manager.name} '
        f'number of members: {len(team.get_members())}'
    )
