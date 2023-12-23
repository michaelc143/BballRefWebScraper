"""
    File to test get_standings from bb_ref_scraper
"""
import pytest
import pandas as pd
from bballRefWebScraper.bb_ref_scraper import get_standings

def test_get_standings(delay_between_tests):
    """ Tests get_standings """
    standings = get_standings('2024')
    expect_cols = ['Eastern Conference','W','L','W/L%','GB','PS/G','PA/G',
                   'SRS','Western Conference','W','L','W/L%','GB','PS/G','PA/G','SRS']
    assert all(column in standings.columns for column in expect_cols)

def test_get_standings_bad_year(delay_between_tests):
    """ Tests get_standings """
    with pytest.raises(ValueError):
        standings = get_standings('2900')
