import pytest
import tasks

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
