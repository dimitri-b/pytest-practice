import pytest
import tasks
from tasks import Task


def test_task_defaults():
    t = Task()
    t_expected = Task(None, None, False, None)
    assert t == t_expected


def test_task_as_dict():
    """._asdict() should return a dictionary"""
    t_task = Task('just testing', 'Bob', False, 42)
    expected_dict = {
        'summary': 'just testing',
        'owner': 'Bob',
        'done': False,
        'id': 42
    }
    assert t_task._asdict() == expected_dict


def test_task_member_access():
    t = Task('foo', 'Bob', False, 42)
    assert (t.summary, t.done) == ('foo', False)


def test_replace_task_element():
    t_before = Task('foo', 'Bob', False, 42)
    t_after = t_before._replace(done=True)
    t_expected = Task('foo', 'Bob', True, 42)
    assert t_after == t_expected
