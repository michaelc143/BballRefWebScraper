"""
    File to test mvp_tracker.py functions
"""
import pytest
import pandas as pd
from scraper.mvp_tracker import get_mvp_tracker

def test_get_mvp_tracker():
    mvp_df = get_mvp_tracker()
    # check col names
    assert 'Player' and 'Team' and 'W' and 'L' and 'W/L%' and 'G' and 'GS' in mvp_df.columns
    assert 'MP' and 'FG' and 'FGA' and 'FG%' and '3P' and '3PA' and '3P%' in mvp_df.columns
    assert len(mvp_df) == 10
