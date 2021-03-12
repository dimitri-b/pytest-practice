
# import pytest
import tasks
from tasks import Task


# the tasks below initialise tasks database via fixture in conftest.py,
# by referencing its name: tasks_db

def test_add_returns_valid_id(tasks_db):
    """Adding a new task should return the task ID as int"""
    # GIVEN a running task_db
    # WHEN new task is added
    # THEN it is auto-allocated an int ID
    new_task = Task('foo')
    task_id = tasks.add(new_task)
    assert isinstance(task_id, int)


# the tasks below require an initialised tasks database

# def test_add_returns_valid_id():
#     """Adding a task should return a valid task ID just added"""
#     new_task = Task('foo')
#     task_id = tasks.add(new_task)
#     assert isinstance(task_id, int)


# @pytest.mark.smoke
# def test_added_task_has_id():
#     new_task = Task('bar')
#     task_id = tasks.add(new_task)
#     task_from_db = tasks.get(task_id)
#     assert task_from_db.id == task_id


# fixture to initialise tasks database before each test
# and stop it after that test
# uses special pytest 'tmpdir' var to generate temprorary dir for database
# autouse=True sets it to run automatically before each test
# @pytest.fixture(autouse=True)
# def initialise_task_db(tmpdir):
#     tasks.start_tasks_db(str(tmpdir), 'tiny')
#     yield  # give control to the test function
#     # when test function is done - run this
#     tasks.stop_tasks_db()
