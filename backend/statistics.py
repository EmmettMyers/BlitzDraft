from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from collections import Counter

uri = "mongodb+srv://emmettmyers:dbCS8045@cluster0.bnt1l57.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri, server_api=ServerApi('1'))
db = client["BlitzDraft"]

def countOccurrences(arr):
    occurrences = [0] * 18 
    for num in arr:
        if 0 <= num <= 17:
            occurrences[num] += 1
    return occurrences

def getStats(email):
    totalStats = {
        "avgRec": 0,
        "highRec": 0,
        "lowRec": 17,
        "avgRank": 0,
        "allRecords": [],
        "allRanks": [],
        "highPlayers": [],
        "highTeams": [],
        "lowTeams": [],
        "posADP": []
    }
    # getting record stats
    records = db["recordStats"]
    userRecords = 0
    for record in records.find():
        if record['email'] == email:
            userRecords += 1
            wins = record['wins']
            if wins > totalStats['highRec']:
                totalStats['highRec'] = wins
            elif wins < totalStats['lowRec']:
                totalStats['lowRec'] = wins
            totalStats['avgRec'] += wins
            totalStats['allRecords'].append(wins)
    totalStats['allRecords'] = countOccurrences(totalStats['allRecords'])
    totalStats['avgRec'] = round(totalStats['avgRec']/userRecords)
    # getting rank stats
    ranks = db["rankStats"]
    userRanks = 0
    for rank in ranks.find():
        if rank['email'] == email:
            userRanks += 1
            gameRank = rank['rank']
            totalStats['avgRank'] += gameRank
            totalStats['allRanks'].append(gameRank)
    totalStats['avgRank'] = round(totalStats['avgRank']/userRanks)
    # getting pick stats
    players = {}
    teams = {}
    posADP = {key: 0 for key in ['QB', 'RB', 'WR1', 'WR2', 'WR3', 'TE', 'OL', 'DEF']}
    totalPicks = 0
    picks = db["pickStats"]
    for pick in picks.find():
        if pick['email'] == email:
            totalPicks += 1
            playerName = pick['name']
            playerTeam = pick['team']
            if playerName in players:
                players[playerName][1] += 1
            else:
                players[playerName] = [playerTeam, 1]
            team = pick['team']
            if team in teams:
                teams[team] += 1
            else:
                teams[team] = 1
            pos = pick['position']
            numPick = pick['pickNumber']
            posADP[pos] += numPick
    sorted_players = sorted(players.items(), key=lambda item: item[1][1], reverse=True)
    totalStats['highPlayers'] = sorted_players[:5]
    team_counter = Counter(teams)
    top_2_teams = team_counter.most_common(2)
    bottom_2_teams = team_counter.most_common()[:-3:-1]
    totalStats['highTeams'] = [team for team, occurrences in top_2_teams]
    totalStats['lowTeams'] = [team for team, occurrences in bottom_2_teams]
    for pos in posADP:
        posADP[pos] = posADP[pos] / (totalPicks / (totalPicks / userRecords))
    totalStats['posADP'] = list(posADP.values())
    return totalStats

print(getStats('emmettleemyers@gmail.com'))

def statDraftPick(email, name, pos, team, pick):
    pickInfo = {
        "email": email,
        "name": name,
        "position": pos,
        "team": team,
        "pickNumber": pick 
    }
    col = db["pickStats"]
    save = col.insert_one(pickInfo)
    return "draft pick inserted into database"

def statRank(email, rank):
    rankInfo = {
        "email": email,
        "rank": rank
    }
    col = db["rankStats"]
    save = col.insert_one(rankInfo)
    return "draft rank inserted into database"

def statRecord(email, wins):
    recordInfo = {
        "email": email,
        "wins": wins
    }
    col = db["recordStats"]
    save = col.insert_one(recordInfo)
    return "draft record inserted into database"