import pytest
import datetime
import time
import random


# TODO: the fixture raises ERROR on teardown instead of failing the test,
# re-do it to make it fail instead (also ask Brian)
@pytest.fixture(autouse=True)
def check_duration(request, cache):
    """Fixture to track run times for each subsequent test, compare to previous,
    and raise an error if the time is more than x2 longer.
    """
    # make keys path-safe - no colons
    key = 'duration/' + request.node.nodeid.replace(':', '_')
    start_time = datetime.datetime.now()
    yield
    stop_time = datetime.datetime.now()
    this_duration = (stop_time - start_time).total_seconds()
    last_duration = cache.get(key, None)
    cache.set(key, this_duration)
    if last_duration is not None:
        assert this_duration <= (last_duration * 2), \
            "Test duration is more that x2 longer than previous run"


# test the fixture
@pytest.mark.parametrize('i', range(5))
def test_slow_runs(i):
    time.sleep(random.random())
