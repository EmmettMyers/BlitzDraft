import csv

teams = ["ARI", "ATL", "BAL", "BUF", "CAR", "CHI", "CIN", "CLE", "DAL", "DEN",
         "DET", "GNB", "HOU", "IND", "JAX", "KAN", "LVR", "LAC", "LAR", "MIA",
         "MIN", "NWE", "NOR", "NYG", "NYJ", "PHI", "PIT", "SFO", "SEA", "TAM",
         "TEN", "WAS"]
full_teams = ["Arizona Cardinals", "Atlanta Falcons", "Baltimore Ravens", "Buffalo Bills", 
              "Carolina Panthers", "Chicago Bears", "Cincinnati Bengals", "Cleveland Browns", 
              "Dallas Cowboys", "Denver Broncos", "Detroit Lions", "Green Bay Packers", "Houston Texans", 
              "Indianapolis Colts", "Jacksonville Jaguars", "Kansas City Chiefs", "Las Vegas Raiders", 
              "Los Angeles Chargers", "Los Angeles Rams", "Miami Dolphins", "Minnesota Vikings", 
              "New England Patriots", "New Orleans Saints", "New York Giants", "New York Jets", 
              "Philadelphia Eagles", "Pittsburgh Steelers", "San Francisco 49ers", "Seattle Seahawks", 
              "Tampa Bay Buccaneers", "Tennessee Titans", "Washington Commanders"]

def getPlayersByTeam(full_team):
    team = teams[full_teams.index(full_team)]
    images = []
    with open("data/player_images_2022.csv", 'r') as file:
        imageReader = csv.reader(file)
        for row in imageReader:
            images.append(row)
    with open("data/small_stats_2022.csv", 'r') as file:
        statReader = csv.reader(file)
        statRows = list(statReader)
        for i in range(32):
            if statRows[i][0] == team:
                qb = statRows[i][1:7]
                qb.append(images[i][0])
                rb = statRows[i][7:12]
                rb.append(images[i][1])
                wr1 = statRows[i][12:16]
                wr1.append(images[i][2])
                wr2 = statRows[i][16:20]
                wr2.append(images[i][3])
                wr3 = statRows[i][20:24]
                wr3.append(images[i][4])
                te = statRows[i][24:28]
                te.append(images[i][5])
                ol = statRows[i][28:32]
                d = statRows[i][32:37]
                return {"team": full_team,
                        "qb" : qb, 
                        "rb" : rb, 
                        "wr1" : wr1, 
                        "wr2" : wr2, 
                        "wr3" : wr3, 
                        "te" : te, 
                        "ol" : ol, 
                        "def" : d }
    return None