import pytest


def test_this_passes():  # sourcery skip: simplify-numeric-comparison
    assert 2 * 2 == 4


@pytest.mark.xfail
def test_this_fails():  # sourcery skip: simplify-numeric-comparison
    assert 2 * 2 != 4
