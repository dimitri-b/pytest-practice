"""Fixture scopes demo"""

# a socpe can be specified for fixtures, in which case the fixture will
# run once per scope
# default is 'function'
# fixtures in a scope can only depend on other fixtures in the same or higher scope,
# e.g. function can use module scope, but module cannot use function, etc.

import pytest


@pytest.fixture(scope='function')
def fixture_scope_func():
    pass


@pytest.fixture(scope='class')
def fixture_scope_class():
    pass


@pytest.fixture(scope='module')
def fixture_scope_module():
    pass


@pytest.fixture(scope='session')
def fixture_scope_session():
    pass


def test_1(fixture_scope_func, fixture_scope_module, fixture_scope_session):
    """Dummy function to trigger diferent fixtures"""
    pass


def test_2(fixture_scope_func, fixture_scope_module, fixture_scope_session):
    """Another dummy functino to trigger the same fixtures again"""
    pass


@pytest.mark.usefixtures('fixture_scope_class')  # <-- note: str, not object
class TestFixtrueScopes():
    def test_in_class_1(self):
        pass

    def test_in_class_2(self):
        pass
