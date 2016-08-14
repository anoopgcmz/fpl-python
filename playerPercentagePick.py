import json
import csv

def getAllPlayersDetailedJson():
	with open('allPlayersInfo.json') as json_data:
		d = json.load(json_data)
		return d

def writeToFile(countOfplayersPicked):
	with open('PercentagePicked.csv','w') as out:
		csv_out = csv.writer(out)
		csv_out.writerow(['name','num'])
		for row in countOfplayersPicked:
			csv_out.writerow(row)

playerNameToPercentPicked = {}

allPlayers = getAllPlayersDetailedJson()
for element in allPlayers["elements"]:
	playerNameToPercentPicked[element["web_name"].encode('ascii','ignore')] = float(element["selected_by_percent"])

srotedPlayersPicked = sorted(playerNameToPercentPicked.items(), key=lambda x: x[1], reverse=True)
writeToFile(srotedPlayersPicked )