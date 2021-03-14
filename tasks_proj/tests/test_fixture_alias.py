"""Fixtures can have shorter aliases"""

import pytest


@pytest.fixture(name='the_answer')
def the_answer_to_life_and_universe_and_evertything():
    """Return the answer to life, universe, and everything"""
    return 42


def test_answer(the_answer):
    """Test the answer to life, universe, etc."""
    assert the_answer == 42
