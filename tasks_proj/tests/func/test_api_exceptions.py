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
