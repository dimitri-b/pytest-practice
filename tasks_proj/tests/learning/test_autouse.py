"""Demo of autouse fixtures"""

import pytest
import time


@pytest.fixture(autouse=True, scope='session')
def session_end_time():
    """Print time at the end of the session"""
    yield
    time_now = time.strftime("%Y-%m-%d %X", time.localtime(time.time()))
    print('----')
    print(f'Session finished at {time_now}')
    print('----')


@pytest.fixture(autouse=True, scope='function')
def function_duration():
    """Print duration at the end of the test function"""
    start = time.time()
    yield
    stop = time.time()
    delta = stop - start
    print(f"\nTest duration: {delta:.3}")


def test_1():
    """Simulate test run"""
    time.sleep(1)


def test_2():
    """Simulate test run"""
    time.sleep(1.25)
