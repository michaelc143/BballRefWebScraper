# BasketballReference WebScraping Package Documentation

## Installation

Install the package using pip:

```bash
pip install bballRefWebScraper
```

## Functions

### get_player_stats(player: str) -> pd.DataFrame

Get career stats for an NBA player.

#### Args

* player (str): player whos stats are returned

### Usage

```python
import bballRefWebScraper as bball
# Example: Get career stats for LeBron James
lebron_stats = bball.get_player_stats('LeBron James')
print(lebron_stats)
```

### get_box_scores(date: str) -> pd.DataFrame

Retrieve box scores for all games played on a given date.

### Args

* date (str): Date in format YYYY-MM-DD (e.g., '2023-12-25')

### Usage

```python
import bballRefWebScraper as bball
# Example: Get box scores for games played on Christmas Day
christmas_box_scores = bball.get_box_scores('2023-12-25')
print(christmas_box_scores)
```

### get_standings(year: int) -> pd.DataFrame

Get the standings for a conference in a given year

### Args

* year (int): the year you want data from

### Usage

```python
import bballRefWebScraper as bball
# Example: Get standings for 2023-2024 year
standings = bball.get_standings(2024)
print(standings)
```

### get_draft_class(year: int) -> pd.DataFrame

Retrieves draft class information for a given year.

### Args

* year (int): The year of the draft class to fetch.

### Usage

```python
import bballRefWebScraper as bball
# Example: Get draft class for 2023
draft_2023 = bball.get_draft_class(2023)
print(draft_2023)
```

### get_mvp_tracker() -> pd.DataFrame

Fetches the current NBA MVP tracker data from Basketball-Reference.

### Returns

* df (pd.DataFrame): A DataFrame containing MVP tracker information, including player rankings, names, teams, and MVP scores.

### Usage

```python
import bballRefWebScraper as bball
# Example: Get current MVP tracker
mvp_tracker = bball.get_mvp_tracker()
print(mvp_tracker)
```

### get_mvp_percent(player_name: str) -> str

Retrieves a player's current MVP probability according to Basketball-Reference.

### Args

* player_name (str): The name of the player to check.

### Returns

* probability (str): A string representing the player's MVP probability (e.g., "35.2%").

### Usage

```python
import bballRefWebScraper as bball
# Example: Get Nikola Jokic's MVP probability
giannis_mvp_prob = get_mvp_percent('Nikola Jokic')
print(giannis_mvp_prob)
```

### get_per_game_leaders_szn(stat: str) -> pd.DataFrame

Fetches the top per-game leaders for a given statistic in a single season.

### Args

* stat (str): The statistic to filter by (e.g., "Pts", "Ast", "Trb", "Stl", "Blk").

### Returns

* df (pd.DataFrame): A DataFrame containing top per-game leaders for the specified stat.

### Usage

```python
import bballRefWebScraper as bball
# Example: Get top scorers per game
scoring_leaders = bball.get_per_game_leaders_szn('Pts')
print(scoring_leaders)
```

### get_schedule(team: str, year: str) -> pd.DataFrame

Retrieves the schedule for a specific team and year.

### Args

* team (str): The name of the team to get the schedule for.
* year (str): The year of the schedule to fetch (e.g., "2023").

### Returns

* df (pd.DataFrame): A DataFrame containing the team's schedule, including dates, opponents, and results.

### Usage

```python
import bballRefWebScraper as bball
# Example: Get The Minnesota Timberwolves' schedule for 2023-2024
warriors_schedule = bball.get_schedule("Min", 2024)
print(warriors_schedule)
```
