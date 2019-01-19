from collections import namedtuple
import pytest
import time

Task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
Task.__new__.__defaults__ = (None, None, False, None)


def test_default():
    t1 = Task()
    t2 = Task(None, None, False, None)
    assert t1 == t2


@pytest.mark.mark3
def test_number_access():
    t = Task('buy_milk', 'brian')
    assert t.summary == 'buy_milk'
    assert t.owner == 'brian'
    assert (t.done, t.id) == (False, None)


@pytest.mark.mark2
def test_asdict():
    t_task = Task('do something', 'okken', True, 21)
    t_dict = t_task._asdict()
    expected = {
        'summary': 'do something',
        'owner': 'okken',
        'done': True,
        'id': 21,
    }
    assert t_dict == expected


@pytest.mark.mark2
@pytest.mark.mark1
def test_replace():
    time.sleep(0.1)
    t_before = Task('finish book', 'brian', False)
    t_after = t_before._replace(id=8, done=True)
    t_expected = Task('finish book', 'brian', True, 9)
    assert t_after == t_expected
