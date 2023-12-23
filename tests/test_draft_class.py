"""
    File to test draft_class.py
"""
import pytest
import pandas as pd
from src.draft_class import get_draft_class

def test_draft_class(delay_between_tests):
    """ Tests get_draft_class """
    draft_df = get_draft_class(2023)
    expected_cols = ['Pk', 'Tm', 'Player', 'College', 'Yrs', 'G', 'MP',
                     'PTS', 'TRB', 'AST', 'FG%', '3P%', 'FT%', 'MP', 
                     'PTS', 'TRB', 'AST', 'WS', 'WS/48', 'BPM', 'VORP']
    assert all(column in draft_df.columns for column in expected_cols)

def test_fail_get_draft_class(delay_between_tests):
    """ Tests that get_draft_class raises ValueError for an invalid year """
    with pytest.raises(RuntimeError):
        get_draft_class(1900)
