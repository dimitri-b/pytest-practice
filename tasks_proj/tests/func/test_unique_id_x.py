import pytest
import tasks


# mark the tests as expected to fail
@pytest.mark.xfail
def test_unique_id_1():
    id1 = tasks.unique_id()
    id2 = tasks.unique_id()
    assert id1 != id2


# mark the tests as expected to fail, unclude condition and reason
@pytest.mark.xfail(
    tasks.__version__ < '0.2.0',
    reason='not implemented until 0.2'
)
def test_unique_id_2():
    id1 = tasks.unique_id()
    id2 = tasks.unique_id()
    assert id1 != id2


# just to demo what happens if it doesn't fail
@pytest.mark.xfail
def test_id_is_not_duck():
    id1 = tasks.unique_id()
    assert id1 != 'duck'


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
