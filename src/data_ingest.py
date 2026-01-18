import pandas as pd
import numpy as np
from nba_api.stats.endpoints import shotchartdetail, leagueleaders
from nba_api.stats.static import players

# Scope: 2024-2025

# Find top players within certain parameters
leaders_data = leagueleaders.LeagueLeaders(
    season='2024-25'
)

leaders_df = leaders_data.get_data_frames()[0]
"""
Columns Include:
'PLAYER_ID', 'RANK', 'PLAYER', 'TEAM_ID', 
'TEAM', 'GP', 'MIN', 'FGM','FGA', 'FG_PCT', 
'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 
'FT_PCT','OREB', 'DREB', 'REB', 'AST', 'STL', 
'BLK', 'TOV', 'PTS', 'EFF'
"""

print(leaders_df.head())

"""
IDEA:
Create function in another file that takes the list i will create from above data
of the top players i want to include and returns variables for top 5 players names/ids


Player_1, Player_1, Player_1, Player_1, Player_1 = FUNCTION(LIST)
"""

# # Find player id and other info
# player_dict = players.get_players()
# lebron = [player for player in player_dict if player['full_name'] == 'LeBron James'][0]
# lebron_id = lebron['id']
# # A team ID of 0 can sometimes be used to get all shots for a player across teams
# # or you can find his current team ID. For this example, team_id=0 works.
# team_id = 0 

# # Use player info to pull shot location data
# shot_detail = shotchartdetail.ShotChartDetail(
#     player_id=lebron_id,
#     team_id=team_id,
#     context_measure_simple='FGA', # Field Goal Attempts
#     season_type_all_star='Regular Season'
# )

# # Bring in Pandas df
# shot_df = shot_detail.get_data_frames()[0]

# # Print the columns to see the data (including X, Y coordinates)
# print(shot_df.columns)
# print(shot_df[['LOC_X', 'LOC_Y', 'SHOT_MADE_FLAG', 'ACTION_TYPE']].head())
