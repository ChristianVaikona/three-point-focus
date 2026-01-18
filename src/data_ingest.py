import pandas as pd
import numpy as np
from nba_api.stats.endpoints import shotchartdetail, leagueleaders
from nba_api.stats.static import players

# 1. Find the player and team IDs (Example for LeBron James)
player_dict = players.get_players()
lebron = [player for player in player_dict if player['full_name'] == 'LeBron James'][0]
lebron_id = lebron['id']
# A team ID of 0 can sometimes be used to get all shots for a player across teams
# or you can find his current team ID. For this example, team_id=0 works.
team_id = 0 

# 2. Call the API endpoint
shot_detail = shotchartdetail.ShotChartDetail(
    player_id=lebron_id,
    team_id=team_id,
    context_measure_simple='FGA', # Field Goal Attempts
    season_type_all_star='Regular Season'
)

# 3. Convert to a DataFrame
# The result is a dictionary-like object; get the first data frame.
shot_df = shot_detail.get_data_frames()[0]

# Print the columns to see the data (including X, Y coordinates)
print(shot_df.columns)
print(shot_df[['LOC_X', 'LOC_Y', 'SHOT_MADE_FLAG', 'ACTION_TYPE']].head())
