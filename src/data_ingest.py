import pandas as pd
import numpy as np
from nba_api.stats.endpoints import shotchartdetail, leagueleaders

leaders = leagueleaders.LeagueLeaders(
    season='2024-25',
    season_type_all_star='Regular Season',
    stat_category_abbreviation='FG3_PCT'  # sort by 3P%
)
df_leaders = leaders.get_data_frames()[0]

print(df_leaders.head(10))

shots = shotchartdetail.ShotChartDetail(
    team_id=0,  # 0 = all teams for that player
    player_id=203552,
    season_nullable='2024-25',
    season_type_all_star='Regular Season',
    context_measure_simple='FGA'  # get all attempts
)

df_shots = shots.get_data_frames()[0]  # Shot_Chart_Detail table

print(df_shots.head(10))