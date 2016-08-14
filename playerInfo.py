import requests

FPL_URL = "https://fantasy.premierleague.com/drf/"
USER_SUMMARY_SUBURL = "element-summary/"
LEAGUE_STANDING_SUBURL = "leagues-classic-standings/"
TEAM_ENTRY_SUBURL = "entry/"
GW_NUMBER = 1
EVENT_SUBURL = "event/" + str(GW_NUMBER) + "/picks"
USER_SUMMARY_URL = FPL_URL + USER_SUMMARY_SUBURL
LEAGUE_STANDING_URL = FPL_URL + LEAGUE_STANDING_SUBURL
ID_TEST = 1

yala_on_scasse_league_id = 336217
test_entry_id = 2677936

# player data: https://fantasy.premierleague.com/drf/bootstrap-static   (download it in a local file!)

# https://fantasy.premierleague.com/drf/leagues-classic-standings/336217
def getUserEntryIds(league_id): 
	league_url = LEAGUE_STANDING_URL + str(league_id)
	r = requests.get(league_url)
	jsonResponse = r.json()
	standings = jsonResponse["standings"]["results"]
	entries = []

	for player in standings:
		entries.append(player["entry"])

	return entries

def getplayersPickedForEntryId(entry_id):
	playerTeamUrlForSpecificGW = FPL_URL + TEAM_ENTRY_SUBURL + str(entry_id) + "/" + EVENT_SUBURL
	r = requests.get(playerTeamUrlForSpecificGW)
	jsonResponse = r.json()
	picks = jsonResponse["picks"]
	elements = []

	for pick in picks:
		elements.append(pick["element"])

	return elements

# team pick example https://fantasy.premierleague.com/drf/entry/2677936/event/1/picks with 2677936 being entry_id of the player

countOfplayersPicked = {}
entries = getUserEntryIds(yala_on_scasse_league_id)
for entry in entries:
	elements = getplayersPickedForEntryId(entry)
	for element in elements:
		if element in countOfplayersPicked:
			countOfplayersPicked[element] += 1
		else:
			countOfplayersPicked[element] = 1

print countOfplayersPicked