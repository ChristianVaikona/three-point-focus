from nba_api.stats.static import players
player_dict = players.get_players()
from nba_api.stats.static import teams
teams = teams.get_teams()
from nba_api.stats.static import teams
teams = teams.get_teams()
from nba_api.stats.endpoints import shotchartdetail, leaguedashplayershotlocations



shot_detail = shotchartdetail.ShotChartDetail(player_id=0, 
              team_id=0, context_measure_simple = 'FGA',     
              season_type_all_star='Playoffs')
shot_df = shot_detail.get_data_frames()[0]

print(shot_df.head())