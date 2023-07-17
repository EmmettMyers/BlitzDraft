from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://emmettmyers:dbCS8045@cluster0.bnt1l57.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri, server_api=ServerApi('1'))

def statDraftPick(email, name, pos, team, pick):
    pickInfo = {
        "email": email,
        "name": name,
        "position": pos,
        "team": team,
        "pickNumber": pick 
    }
    db = client["BlitzDraft"]
    col = db["pickStats"]
    save = col.insert_one(pickInfo)
    return "draft pick inserted into database"

def statRank(email, rank):
    rankInfo = {
        "email": email,
        "rank": rank
    }
    db = client["BlitzDraft"]
    col = db["rankStats"]
    save = col.insert_one(rankInfo)
    return "draft rank inserted into database"

def statRecord(email, wins):
    recordInfo = {
        "email": email,
        "wins": wins
    }
    db = client["BlitzDraft"]
    col = db["recordStats"]
    save = col.insert_one(recordInfo)
    return "draft record inserted into database"