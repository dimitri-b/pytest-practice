""" DO NOT IMPORT THIS MODULE """

# this module contains shared fixtures for use by all tests in this dir and its subdirs

# Reminder of Task constructor interface
# # Task(summary=None, owner=None, done=False, id=None) ​ ​ ​
# # summary is required ​ ​ ​
# # owner and done are optional ​ ​ ​
# # id is set by database

import pytest
import tasks
from tasks import Task

import redundant_math


# tasks db to last for the whole testing session
# uses tmpdir_factory instead of tmpdir, because factory is of session scope
@pytest.fixture(scope='session')
def tasks_db_session(tmpdir_factory):
    """Initialise tasks db for the session, disconnect after"""
    temp_dir = tmpdir_factory.mktemp('temp')
    tasks.start_tasks_db(str(temp_dir), 'tiny')
    yield
    tasks.stop_tasks_db


# the fixture with this name is used in many test,
# we can easily change it's scope without braking any tests that depend on it
# here it has 'session' scope via use of tasks_db_session fixture
@pytest.fixture()
def tasks_db(tasks_db_session):
    """Initialise and empty the db for the session"""
    tasks.delete_all()


# tasks db to last per one function that calls it (default scope)
# @pytest.fixture()
# def tasks_db(tmpdir):
#     # set up db
#     tasks.start_tasks_db(str(tmpdir), "tiny")
#     # give control to tests
#     yield
#     # teardown after tests
#     tasks.stop_tasks_db()


@pytest.fixture()
def tasks_just_a_few():
    """Several tasks with unique owner and summaries"""
    return (
        Task("foo", "Alice", False),
        Task("bar", "Bob", True),
        Task("baz", "Charlie", False),
    )


@pytest.fixture()
def tasks_multiple_per_owner():
    """Return a tuple of tasks, with multiple tasks per owner"""
    return (
        Task("foo", "Alice", False),
        Task("bar", "Alice", True),
        Task("baz", "Alice", False),
        # --
        Task("foo", "Bob", False),
        Task("bar", "Bob", True),
        Task("baz", "Bob", False),
        # --
        Task("foo", "Charlie", False),
        Task("bar", "Charlie", True),
        Task("baz", "Charlie", False),
    )


# this fixture uses other fixtures,
# note how it takes tasks_db param to trigger db init
@pytest.fixture()
def db_with_3_tasks(tasks_db, tasks_just_a_few):
    """Initialise tasks db with 3 tasks"""
    for t in tasks_just_a_few:
        tasks.add(t)


@pytest.fixture()
def db_with_multi_tasks(tasks_db, tasks_multiple_per_owner):
    """Initialise tasks db with multiple tasks per owner"""
    for t in tasks_multiple_per_owner:
        tasks.add(t)


@pytest.fixture(autouse=True)
def add_redundant_math_abbr(doctest_namespace):
    """For --doctest-modules tests to parse doctest examples properly,
    put abbreviated module name, as it appears in the module's
    example import statement, into namespace
    """
    doctest_namespace['rm'] = redundant_math


# ---- plugin prototyping ----
# using pytest hook functions to intercept pytest calls and modify behaviour

# adds new command line option: --nice
def pytest_addoption(parser):
    """Add CLI option to show politically correct outcomes"""
    group = parser.getgroup('nice')
    group.addoption(
        "--nice",
        action='store_true',
        help='less offensive language for error messages'
    )


# pytest hook function, uses new --nice option to modify test results status message
def pytest_report_header(config):
    """Using hook to override default status message"""
    if config.getoption('nice'):
        return 'Thank you for testing'


# pytest hook function, uses new --nice option to modify test failure flags: 
# F -> WN, FAILED -> WORK NEEDED
def pytest_report_teststatus(report, config):
    """Use hook to change Fail (F) symbol in status"""
    if report.when == 'call':
        if report.failed and config.getoption('nice'):
            return (report.outcome, 'WN', 'WORK NEEDED')
