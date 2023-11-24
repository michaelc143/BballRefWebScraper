"""
    File to test get_player_stats.py functions
"""
import pytest
import pandas as pd
from scraper.get_player_stats import get_player_stats

def test_get_player_stats(delay_between_tests):
    """ Tests get_player_stats """
    player_df = get_player_stats('Stephen Curry')
    # check col names
    assert 'Season' and 'Age' and 'Tm' and 'Lg' and 'Pos' and 'G' and 'GS' in player_df.columns
    assert 'MP' and 'FG' and 'FGA' and 'FG%' and '3P' and '3PA' and '3P%' in player_df.columns
    assert '2P' and '2PA' and '2P%' and 'eFG%' and 'FT' in player_df.columns
    assert 'FTA' and 'FT%' and 'ORB' and 'DRB' in player_df.columns
    assert 'TRB' and 'AST' and 'STL' and 'BLK' and 'TOV' and 'PF' and 'PTS' in player_df.columns
    assert len(player_df) != 0

def test_get_player_stats_short_last_name(delay_between_tests):
    """ Tests get_player_stats with a player with last name > 5 letters long """
    player_df = get_player_stats('Russell Westbrook')
    # check col names
    assert 'Season' and 'Age' and 'Tm' and 'Lg' and 'Pos' and 'G' and 'GS' in player_df.columns
    assert 'MP' and 'FG' and 'FGA' and 'FG%' and '3P' and '3PA' and '3P%' in player_df.columns
    assert '2P' and '2PA' and '2P%' and 'eFG%' and 'FT' in player_df.columns
    assert 'FTA' and 'FT%' and 'ORB' and 'DRB' in player_df.columns
    assert 'TRB' and 'AST' and 'STL' and 'BLK' and 'TOV' and 'PF' and 'PTS' in player_df.columns
    assert len(player_df) != 0
