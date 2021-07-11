

import pytest
import tasks
from tasks import Task


def equivalent(t1, t2):
    """All task fields except ID are the same"""
    return (
        (t1.summary == t2.summary) and
        (t1.owner == t2.owner) and
        (t1.done == t2.done)
    )


tasks_to_try = [
    Task('foo', done=None),
    Task('bar', 'Bob', True),
    Task('bar', "Bob", True),
    Task("", done=True, owner="BoJo"),
]

# list with task labels (ID's) to use with a test
# task_ids = [f'Task({t.summary}, {t.owner}, {t.done})' for t in tasks_to_try]


def get_task_id(task):
    """Return a label to be used as task ID in tests"""
    return f'Task({task.summary}, {task.owner}, {task.done})'


@pytest.fixture(params=tasks_to_try)  # <-- params - sets up to use parameters
def a_task(request):  # <-- built-in fixture, determines this fixture's running mode
    # TODO: add more details about 'request'
    """Return one task object for each element in params, no param IDs"""
    return request.param  # <-- .param works like an iterator


# note - ids can be either a list of labels, or a function to generate one
@pytest.fixture(params=tasks_to_try, ids=get_task_id)
def a_task_with_id(request):
    """Return one task object for each element in params, with param IDs"""
    return request.param


def test_add_task(tasks_db, a_task):
    """Use 'a_task' parametrised fixture to test equivalence of multiple added tasks,
    wihout using params' IDs
    """
    task_id = tasks.add(a_task)
    task_from_db = tasks.get(task_id)
    assert equivalent(task_from_db, a_task)


def test_add_task_with_id(tasks_db, a_task_with_id):
    """Use 'a_task' parametrised fixture to test equivalence of multiple added tasks,
    using a list of prepared params' IDs
    """
    task_id = tasks.add(a_task_with_id)
    task_from_db = tasks.get(task_id)
    assert equivalent(task_from_db, a_task_with_id)
