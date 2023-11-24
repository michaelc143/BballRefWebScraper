"""
    File to test mvp_tracker.py functions
"""
import pytest
import pandas as pd
from scraper.per_game_leaders import get_per_game_leaders_szn

def test_get_per_game_leaders_pts(delay_between_tests):
    df = get_per_game_leaders_szn('pts')
    ex_headers = ['Rank', 'Player', 'PPG', 'Season']
    assert all(column in df.columns for column in ex_headers)

def test_get_per_game_leaders_ast(delay_between_tests):
    df = get_per_game_leaders_szn('ast')
    ex_headers = ['Rank', 'Player', 'APG', 'Season']
    assert all(column in df.columns for column in ex_headers)
    
def test_get_per_game_leaders_reb(delay_between_tests):
    df = get_per_game_leaders_szn('trb')
    ex_headers = ['Rank', 'Player', 'RPG', 'Season']
    assert all(column in df.columns for column in ex_headers)
    
def test_get_per_game_leaders_stl(delay_between_tests):
    df = get_per_game_leaders_szn('stl')
    ex_headers = ['Rank', 'Player', 'SPG', 'Season']
    assert all(column in df.columns for column in ex_headers)

def test_get_per_game_leaders_blk(delay_between_tests):
    df = get_per_game_leaders_szn('blk')
    ex_headers = ['Rank', 'Player', 'BPG', 'Season']
    assert all(column in df.columns for column in ex_headers)