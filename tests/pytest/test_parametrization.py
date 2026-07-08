import pytest
from _pytest.fixtures import SubRequest


@pytest.mark.parametrize('number', [1, 3, -1])
def test_numbers(number: int):
    assert number > 0

@pytest.mark.parametrize('number, result', [(1,1), (2,4), (3,9)])
def test_square(number: int, result: int):
    assert number**2 == result



@pytest.fixture(params=['chrome', 'firefox', 'safari'])
def browser(request: SubRequest):
    return request.param

def test_open_browser(browser: str):
    print(f'open "{browser}"')

@pytest.mark.parametrize('phone_number', ['+70118356784', '70118356785', '70118356786'], ids=['user with money', 'user without money', 'user with operations on bank account'])
def test_identifiers(phone_number: str):
    ...



users = {
    "+70000000011": "User with money on bank account",
    "+70000000022": "User without money on bank account",
    "+70000000033": "User with operations on bank account"
}

@pytest.mark.parametrize('phone_number', users.keys(), ids=lambda phone_number: f'{phone_number}: {users[phone_number]}')
def test_identifiers(phone_number: str):
    ...