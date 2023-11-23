"""
    File to show example usage of functions
"""
from scraper.bb_ref_scraper import get_box_scores, get_draft_class, get_standings
from scraper.mvp_tracker import get_mvp_tracker, get_mvp_percent

# draft_df = get_draft_class(2023)
# print(draft_df)

box_score = get_box_scores('2023-11-20', 'MIN', 'NYK', period='GAME', stat_type='BASIC')
print(box_score)

# standings = get_standings(2024)
# print(standings)

# mvp_df = get_mvp_tracker()
# print(mvp_df)

# mvp = get_mvp_percent("Nikola Jokic")
# print(mvp)
