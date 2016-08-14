import requests

FPL_URL = "https://fantasy.premierleague.com/drf/"
PLAYER_SUMMARY_SUBURL = "element-summary/"
LEAGUE_STANDING_SUBURL = "leagues-classic-standings/"
PLAYER_SUMMARY_URL = FPL_URL + PLAYER_SUMMARY_SUBURL
LEAGUE_STANDING_URL = FPL_URL + LEAGUE_STANDING_SUBURL
ID_TEST = 1


yala_on_scasse_league_id = 336217

# team pick example https://fantasy.premierleague.com/drf/entry/2677936/event/1/picks with 2677936 being entry_id of the player
# player data: https://fantasy.premierleague.com/drf/bootstrap-static   (download it in a local file!)

r = requests.get(LEAGUE_STANDING_URL + str(yala_on_scasse_league_id))
jsonResponse = r.json()
print jsonResponse