"""
    File to test mvp_tracker.py functions
"""
import pytest
import pandas as pd
from scraper.mvp_tracker import get_mvp_tracker

def test_get_mvp_tracker():
    mvp_df = get_mvp_tracker()
    assert 'Player' in mvp_df.columns