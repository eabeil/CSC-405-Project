from pathlib import Path
from tempfile import TemporaryDirectory

import pandas as pd


# Constants
SEASON_FILES = {
    "2010/11": "E0 (29).csv",
    "2011/12": "E0 (28).csv",
    "2012/13": "E0 (27).csv",
    "2013/14": "E0 (26).csv",
    "2014/15": "E0 (25).csv",
    "2015/16": "E0 (19).csv",
    "2016/17": "E0 (20).csv",
    "2017/18": "E0 (21).csv",
    "2018/19": "E0 (22).csv",
    "2019/20": "E0 (23).csv",
    "2020/21": "E0 (24).csv",
}

# fixed column names for the fixture data
FIXTURE_COLUMNS = {
    "Date": "match_date",
    "HomeTeam": "home_team",
    "AwayTeam": "away_team",
    "FTHG": "home_goals",
    "FTAG": "away_goals",
    "FTR": "result",
}

SCORE_COLUMNS = ["home_goals", "away_goals"]
