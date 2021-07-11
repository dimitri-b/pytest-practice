import pytest
import tasks
from tasks import Task


@pytest.fixture(autouse=True)
def initialise_task_db(tmpdir):
    tasks.start_tasks_db(str(tmpdir), 'tiny')
    yield
    tasks.stop_tasks_db()


def test_delete_all():
    tasks.delete_all()
    assert tasks.count() == 0


def test_task_count():
    tasks.delete_all()
    tasks.add(Task('task1'))
    tasks.add(Task('task2'))
    tasks.add(Task('task3'))
    assert tasks.count() == 3
