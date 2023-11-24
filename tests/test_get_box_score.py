"""
    File to test bb_ref_scraper.py function get_box_score
"""
import pytest
import pandas as pd
from scraper.bb_ref_scraper import get_box_scores

def test_get_box_score(delay_between_tests):
    box_scores_dict = get_box_scores('2023-11-20', 'MIN', 'NYK', period='GAME', stat_type='BASIC')
    df1, df2 = box_scores_dict['MIN'], box_scores_dict['NYK']
    assert len(df1) != 0 and len(df2) != 0
    expected_columns = ['Starters', 'MP', 'FG', 'FGA', 'FG%', '3P', '3PA',
                        '3P%', 'FT', 'FTA', 'FT%', 'ORB', 'DRB', 'TRB', 
                        'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS', '+/-']
    assert all(column in df1.columns for column in expected_columns)
