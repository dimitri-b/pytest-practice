import pytest
import tasks
from tasks import Task


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


# mark this test to skip it, reason comes up in output with -v option,
# or with -rs ( -r[chars] where chars: s-skipped, f-failed, etc.), see --help
# ---
# @pytest.mark.skip(reason="misunderstood API docs")

# mark to skip if the condition is met, e.g. it is the future version, etc.
# reason is required for skipf marks
@pytest.mark.skipif(
    tasks.__version__ < '0.2.0',
    reason="not supported until v0.2"
)
def test_unique_id_1():
    """Calling tasks.unique_id() twice should return different id's"""
    id1 = tasks.unique_id()
    id2 = tasks.unique_id()
    assert id1 != id2


def test_unique_id_2():
    ids = []
    ids.append(tasks.add(Task('one')))
    ids.append(tasks.add(Task('two')))
    ids.append(tasks.add(Task('three')))
    uid = tasks.unique_id()
    assert uid not in ids
