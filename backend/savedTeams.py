from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = {MONGO_URI}
client = MongoClient(uri, server_api=ServerApi('1'))
db = client["BlitzDraft"]
col = db["savedTeams"]

def saveTeam(email, username, teamName, date, record, team):
    teamInfo = {
        "email": email,
        "username": username,
        "teamName": teamName,
        "date": date,
        "record": record,
        "team": team
    }
    save = col.insert_one(teamInfo)
    return "team inserted into database"

def getTeams(userEmail):
    teams_cursor = col.find({'email': userEmail})
    teams = [team for team in teams_cursor]
    for team in teams:
        team.pop('_id', None)
    return teams

def deleteTeam(userEmail, teamName):
    col.delete_one({ 'email': userEmail, 'teamName': teamName })
    return "team deleted from database"
