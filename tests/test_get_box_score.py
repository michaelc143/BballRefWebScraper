"""
    File to test bb_ref_scraper.py function get_box_score
"""
import pytest
import pandas as pd
from bballRefWebScraper.bb_ref_scraper import get_box_scores

def test_get_box_score(delay_between_tests):
    """ Tests get_box_scores """
    box_scores_dict = get_box_scores('2023-11-20', 'MIN', 'NYK', period='GAME', stat_type='BASIC')
    df1, df2 = box_scores_dict['MIN'], box_scores_dict['NYK']
    assert len(df1) != 0 and len(df2) != 0
    expected_columns = ['Starters', 'MP', 'FG', 'FGA', 'FG%', '3P', '3PA',
                        '3P%', 'FT', 'FTA', 'FT%', 'ORB', 'DRB', 'TRB', 
                        'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS', '+/-']
    assert all(column in df1.columns for column in expected_columns)

def test_get_box_score_advanced(delay_between_tests):
    """ Tests get_box_scores """
    box_scores_dict = get_box_scores('2023-11-20', 'MIN', 'NYK', period='GAME',
                                     stat_type='ADVANCED')
    df1, df2 = box_scores_dict['MIN'], box_scores_dict['NYK']
    assert len(df1) != 0 and len(df2) != 0

def test_get_box_score_fake_category(delay_between_tests):
    """ Tests get_box_scores """
    with pytest.raises(ValueError):
        box_scores_dict = get_box_scores('2023-11-20',
                                         'MIN', 'NYK', period='GAME', stat_type='FAKE')
