from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://emmettmyers:dbCS8045@cluster0.bnt1l57.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri, server_api=ServerApi('1'))

def saveTeam(email, username, teamName, date, record, team):
    teamInfo = {
        "email": email,
        "username": username,
        "teamName": teamName,
        "date": date,
        "record": record,
        "team": team
    }
    db = client["BlitzDraft"]
    col = db["savedTeams"]
    save = col.insert_one(teamInfo)
    return "team inserted into database"

def getTeams(userEmail):
    db = client["BlitzDraft"]
    col = db["savedTeams"]
    teams_cursor = col.find({'email': userEmail})
    teams = [team for team in teams_cursor]
    for team in teams:
        team.pop('_id', None)
    return teams

def deleteTeam(userEmail, teamName):
    db = client["BlitzDraft"]
    col = db["savedTeams"]
    col.delete_one({ 'email': userEmail, 'teamName': teamName })
    return "team deleted from database"