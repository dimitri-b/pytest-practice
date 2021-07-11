import pytest


# a primitive fixture example - simply return a value when referenced
@pytest.fixture()  # <-- are () optional? NOTE
def the_answer():
    return 42


# fixture is referenced in the function args
def test_the_answer(the_answer):
    assert the_answer == 42
