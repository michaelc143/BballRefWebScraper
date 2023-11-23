"""
    File to test mvp_tracker.py functions
"""
import pytest
import pandas as pd
from scraper.mvp_tracker import get_mvp_tracker

def test_get_mvp_tracker():
    mvp_df = get_mvp_tracker()
    assert 'Player' in mvp_df.columns
    assert 'Team' in mvp_df.columns
    assert 'W' in mvp_df.columns
    assert 'L' in mvp_df.columns
    assert 'W/L%' in mvp_df.columns
    assert 'G' in mvp_df.columns
    assert 'GS' in mvp_df.columns
    assert 'MP' in mvp_df.columns
    assert 'FG' in mvp_df.columns
    assert 'FGA' in mvp_df.columns
    assert 'FG%' in mvp_df.columns
    assert '3P' in mvp_df.columns
    assert '3PA' in mvp_df.columns
    assert '3P%' in mvp_df.columns
