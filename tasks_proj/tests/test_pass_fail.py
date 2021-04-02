import pytest

def test_this_passes():
    assert 2 * 2 == 4


@pytest.mark.skip
def test_this_fails():
    assert 2 * 2 != 4