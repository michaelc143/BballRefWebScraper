""" Configuration file for pytest """
import time
import pytest

@pytest.fixture
def delay_between_tests():
    """ Adds delay between tests to not get rate limited """
    delay_seconds = 2
    time.sleep(delay_seconds)
