import pytest
import tasks
from tasks import Task
from tasks.api import UninitializedDatabase


# an option to register custom marks, to aviod warnings
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


@pytest.mark.skip(reason="only needed to demo error output")  # TODO: skip if db is initalised
def test_uninit_db_error():
    with pytest.raises(UninitializedDatabase):
        tasks.unique_id()  # any function accessing database will do


@pytest.mark.usefixtures('tasks_db')
class TestAdd():
    """Tests related to adding tasks"""

    def test_missing_summary(self):
        """Should raise an exception if task summary is missing"""
        with pytest.raises(ValueError):
            tasks.add(Task(owner="George"))

    # this one fails, no error is raised
    @pytest.mark.skip
    def test_done_not_bool(self):
        """Should raise an exception if 'done' is not of boolean type"""
        with pytest.raises(ValueError):
            tasks.add(Task(summary='foo', done='True'))


class TestUpdate():
    """Test expected exceptions when using task.update()"""

    def test_forced_id(self):
        """Should not work if id is specified instead of auto-generated"""
        with pytest.raises(ValueError):
            tasks.add(Task(id=42))

    def test_bad_id(self):
        """Non-int ID should raise a TypeError"""
        with pytest.raises(TypeError):
            tasks.update(task_id={'dict instead of int': 42}, task=tasks.Task())

    def test_bad_task(self):
        """Non-task as a param should raise an exception"""
        with pytest.raises(TypeError):
            tasks.update(task_id=1, task='str instead of task')
