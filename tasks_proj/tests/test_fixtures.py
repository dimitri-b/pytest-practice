import pytest


@pytest.fixture()
def mixed_tuple():
    return (42, 'foo', None, {'bar': 23})


@pytest.fixture()
def some_other_data():
    """Raise an exception from fixture, to demo what happens if a test uses it."""
    # the ERROR happens, instead of FAIL
    x = 43
    assert x == 42
    return x


@pytest.mark.skip
def test_tuple(mixed_tuple):
    # this should fail
    assert mixed_tuple[3]['bar'] == 0


@pytest.mark.skip
def test_other_data(some_other_data):
    assert some_other_data == 42
