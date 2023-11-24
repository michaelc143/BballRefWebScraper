"""
    File to test schedule.py functions
"""
import pytest
import pandas as pd
from scraper.schedule import get_schedule

def test_get_schedule(delay_between_tests):
    schedule = get_schedule("Min", 2024)
    expect_cols = ['G', 'Date', 'Start (ET)', '\xa0', 'Box Score', '@', 'Opponent',
                   'W/L', 'OT?', 'Tm', 'Opp', 'W', 'L', 'Streak', 'Notes']
    assert all(column in schedule.columns for column in expect_cols)
