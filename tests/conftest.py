# conftest.py - pytest configuration file

import pytest
import time

@pytest.fixture
def delay_between_tests():
    # You can adjust the delay time as needed
    delay_seconds = 3
    time.sleep(delay_seconds)
