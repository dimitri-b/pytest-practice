"""DO NOT IMPORT THIS MODULE"""

# this module contains shared fixtures for use by all tests in this dir and its subdirs

import pytest
import tasks
# from tasks import Task


@pytest.fixture()
def tasks_db(tmpdir):
    # set up db
    tasks.start_tasks_db(str(tmpdir), 'tiny')
    # give control to tests
    yield
    # teardown after tests
    tasks.stop_tasks_db()
