import pytest
import tasks
from tasks import Task


@pytest.fixture(autouse=True)
def initialise_task_db(tmpdir):
    tasks.start_tasks_db(str(tmpdir), 'tiny')
    yield
    tasks.stop_tasks_db()


def equivalent(t1, t2):
    """All task fields except ID are the same"""
    return (
        (t1.summary == t2.summary) and
        (t1.owner == t2.owner) and
        (t1.done == t2.done)
    )


def test_add_1():
    """Added task can be retrieved from db by its ID"""
    task = Task('foo', 'Tony', False)
    task_id = tasks.add(task)
    task_from_db = tasks.get(task_id)
    assert equivalent(task, task_from_db)


# parametrised test - runs multiple times with supplied params
# pytest will list each run as a separate test
@pytest.mark.parametrize(
    argnames='task',  # <-- parameter name which will have different values
    argvalues=[
        Task('foo', done=True),
        Task('bar', 'Bob'),
        Task('baz', 'John', True),
        Task('A few words', 'Bill Gates', False),
    ]
)
def test_add_2(task):
    """Added task can be retrieved from db by its ID"""
    task_id = tasks.add(task)
    task_from_db = tasks.get(task_id)
    assert equivalent(task, task_from_db)


# variation on parametrised test - same as above, but variable values
# will be shown in test results (if they can be shown as strings)
# NOTE:
# 1 - param names are a comma-delimited list
# 2 - param tuples must match the specs of the names, in this case - 3 in each
@pytest.mark.parametrize(
    'summary, owner, done',
    [
        ('foo', None, None),
        ('bar', 'Bob', True),
        ('baz', 'Steve', None),
        ('long description, really', None, False),
    ]
)
def test_add_3(summary, owner, done):
    task = Task(summary, owner, done)
    task_id = tasks.add(task)
    task_from_db = tasks.get(task_id)
    assert equivalent(task, task_from_db)


# another variation - use prepared objects as parameters
# the output doesn't show used values, just "task0, task1, etc."
tasks_to_try = [
    Task('foo', done=None),
    Task('bar', 'Bob', True),
    Task('bar', "Bob", True),
    Task("", done=True, owner="BoJo"),
]


@pytest.mark.parametrize('task', tasks_to_try)
def test_add_4(task):
    task_id = tasks.add(task)
    task_from_db = tasks.get(task_id)
    assert equivalent(task, task_from_db)


# improvement on the above - use prepared objects and optional ids collection
# to show the values used, ids are the repro strings showing values
task_ids = [f'Task({t.summary}, {t.owner}, {t.done})' for t in tasks_to_try]


@pytest.mark.parametrize('task', tasks_to_try, ids=task_ids)
def test_add_5(task):
    task_id = tasks.add(task)
    task_from_db = tasks.get(task_id)
    assert equivalent(task, task_from_db)


# it is also possible to supply custom ids as labels for different params
@pytest.mark.parametrize('task', [
        pytest.param(Task('foo'), id='created with summary only'),
        pytest.param(Task('bar', 'Jimmy'), id='summary + owner'),
        pytest.param(Task('baz', 'Bob', True), id='all three')
    ]
)
def test_add_6(task):
    task_id = tasks.add(task)
    task_from_db = tasks.get(task_id)
    assert equivalent(task, task_from_db)


# parametrising a test class
@pytest.mark.parametrize('task', tasks_to_try, ids=task_ids)
class TestAdd():
    def test_equivalent(self, task):
        task_id = tasks.add(task)
        task_from_db = tasks.get(task_id)
        assert equivalent(task, task_from_db)

    def test_valid_id(self, task):
        task_id = tasks.add(task)
        task_from_db = tasks.get(task_id)
        assert task_id == task_from_db.id
