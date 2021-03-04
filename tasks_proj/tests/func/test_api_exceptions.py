import pytest
import tasks
from tasks import Task

# an option to register custom marks, to aviod wornings
# def pytest_configure(config):
#     config.addinivalue_line(
#         "markers", "env(name): mark test to run only on named environment"
#     )


# pytest.raises(expected_error_class) - something within this context
# should raise an expected error, or the test will fail
def test_add_wrong_type():
    """Calling tasks.add() with wrong type should raise TypeError"""
    with pytest.raises(TypeError):
        tasks.add(task='just a string, not a task object')


def test_wrong_element_type_error_msg():
    """Raised exception message must match this content"""
    with pytest.raises(ValueError) as err_info:
        tasks.start_tasks_db('some/dummy/path', 'mysql')
    err_msg = err_info.value.args[0]
    assert err_msg == "db_type must be a 'tiny' or 'mongo'"


# marked test can be selectively run with: pytest -m mark_name_here
# also works with: pytest -m "mark_1 and mark_2", also 'or', 'not', etc.
@pytest.mark.smoke
@pytest.mark.get
def test_get_task():
    """Should raise an error when getting a task
    by providing wrong type for ID
    """
    with pytest.raises(TypeError):
        tasks.get(id='123')


@pytest.mark.smoke
def test_task_listing():
    """Should raise an error when trying to list tasks
    by supplying a wrong param type
    """
    with pytest.raises(TypeError):
        tasks.list_tasks(owner=123)


# the tasks below require an initialised tasks database

def test_add_returns_valid_id():
    """Adding a task should return a valid task ID just added"""
    new_task = Task('foo')
    task_id = tasks.add(new_task)
    assert isinstance(task_id, int)


def test_added_task_has_id():
    new_task = Task('bar')
    task_id = tasks.add(new_task)
    task_from_db = tasks.get(task_id)
    assert task_from_db.id == task_id


# fixture to initialise tasks database before each test
# and stop it after that test
# uses special pytest 'tmpdir' var to generate temprorary dir for database
# autouse=True sets it to run automatically before each test
@pytest.fixture(autouse=True)
def initialise_task_db(tmpdir):
    tasks.start_tasks_db(str(tmpdir), 'tiny')
    yield  # give control to the test function
    # when test function is done - run this
    tasks.stop_tasks_db()
