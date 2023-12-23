"""
    File to test mvp_tracker.py functions
"""
import pytest
import pandas as pd
from bballRefWebScraper.mvp_tracker import get_mvp_tracker, get_mvp_percent

def test_get_mvp_tracker(delay_between_tests):
    """ Tests get_mvp_tracker """
    mvp_df = get_mvp_tracker()
    # check col names
    assert 'Player' and 'Team' and 'W' and 'L' and 'W/L%' and 'G' and 'GS' in mvp_df.columns
    assert 'MP' and 'FG' and 'FGA' and 'FG%' and '3P' and '3PA' and '3P%' in mvp_df.columns
    assert len(mvp_df) == 10

def test_get_mvp_percent(delay_between_tests):
    """ Tests get_mvp_percent """
    percent = get_mvp_percent('Nikola Jokic')
    assert type(percent) == str

def test_get_mvp_percent_non_mvp(delay_between_tests):
    """ Tests get_mvp_percent for non-mvp player """
    with pytest.raises(RuntimeError):
        get_mvp_percent('Naz Reid')
