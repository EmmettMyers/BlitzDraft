import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd

row_names = ["Wins", 
             "QB:Comp%", "QB:Pass Yds", "QB:Pass TD", "QB:Int", "QB:First Down", "QB:Adj Yds/att", "Pass Yds/comp", "QB:Pass Yds/g", "QB:Sacked", "QB:Sacked/g", "GWD",
             "RB:Rush Yds", "RB:Rush TD", "RB:First Down", "RB:Yds/rush", "RB:Fumbles",
             "WR1:Catch%", "WR1:Rec Yds", "WR1:Rec TD", "WR1:First Downs", "WR1:Yds/rec", "WR1:Yds/tgt", "WR1:Fumbles",
             "WR2:Catch%", "WR2:Rec Yds", "WR2:Rec TD", "WR2:First Downs", "WR2:Yds/rec", "WR2:Yds/tgt", "WR2:Fumbles",
             "WR3:Catch%", "WR3:Rec Yds", "WR3:Rec TD", "WR3:First Downs", "WR3:Yds/rec", "WR3:Yds/tgt", "WR3:Fumbles",
             "TE:Catch%", "TE:Rec Yds", "TE:Rec TD", "TE:First Downs", "TE:Yds/rec", "TE:Yds/tgt", "TE:Fumbles",
             "OL:Sacked", "OL:Sacked/g", "OL:Yds/rush",
             "DL:Blitzes", "DL:Blitz%", "DL:Hurries", "DL:Hurry%", "DL:Knockdowns", "DL:Knockdown%", "DL:Sacks", "DL:Pressures", "DL:Pressure%",
             "LB:Total Yds", "LB:Points", "LB:Yds/play", "LB:FF", "LB:Pass Yds/att", "LB:Rush Yds", "LB:Rush TD", "LB:Yds/rush", "LB:Penalties", "LB:Penalty Yds",
             "DB:Pass Comp", "DB:Pass Yds", "DB:Pass TD", "DB:Int", "DB:Pass Net Yds/att", "DB:Pass FD", "DB:Turnovers", "DB:Penalties", "DB:Penalty Yards", "DB:Turnover%", "DB:Total Yds", "DB:Points"]

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

# stats indexes: wins, qb, rb, wr1, wr2, wr3, te, ol, dl, lb, db
stats = {}

def resetTeams():
    global teams
    teams = ["ARI", "ATL", "BAL", "BUF", "CAR", "CHI", "CIN", "CLE", "DAL", "DEN",
            "DET", "GNB", "HOU", "IND", "JAX", "KAN", "LVR", "LAC", "LAR", "MIA",
            "MIN", "NWE", "NOR", "NYG", "NYJ", "PHI", "PIT", "SFO", "SEA", "TAM",
            "TEN", "WAS"]
    global full_teams
    full_teams = ["Arizona Cardinals", "Atlanta Falcons", "Baltimore Ravens", "Buffalo Bills", 
                "Carolina Panthers", "Chicago Bears", "Cincinnati Bengals", "Cleveland Browns", 
                "Dallas Cowboys", "Denver Broncos", "Detroit Lions", "Green Bay Packers", "Houston Texans", 
                "Indianapolis Colts", "Jacksonville Jaguars", "Kansas City Chiefs", "Las Vegas Raiders", 
                "Los Angeles Chargers", "Los Angeles Rams", "Miami Dolphins", "Minnesota Vikings", 
                "New England Patriots", "New Orleans Saints", "New York Giants", "New York Jets", 
                "Philadelphia Eagles", "Pittsburgh Steelers", "San Francisco 49ers", "Seattle Seahawks", 
                "Tampa Bay Buccaneers", "Tennessee Titans", "Washington Commanders"]

def setTeamWins(year):
    url = f"https://www.pro-football-reference.com/years/{year}/passing.htm"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table", id="passing")
    body = table.find("tbody")
    rows = body.find_all("tr")
    for row in rows:
        if (row.find('td', attrs={"data-stat": "qb_rec"})):
            team = row.find('td', attrs={"data-stat": "team"}).text
            if (team in teams and stats[team][0] == None):
                wins = row.find('td', attrs={"data-stat": "qb_rec"}).text
                if (len(wins) > 0):
                    stats[team][0] = int(wins[:wins.index("-")])
                else:
                    stats[team][0] = int(0)

def setQBStats(year):
    url = f"https://www.pro-football-reference.com/years/{year}/passing.htm"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table", id="passing")
    body = table.find("tbody")
    rows = body.find_all("tr")
    for row in rows:
        if (row.find('td', attrs={"data-stat": "qb_rec"})):
            team = row.find('td', attrs={"data-stat": "team"}).text
            pass_yds = int(row.find('td', attrs={"data-stat": "pass_yds"}).text)
            if (team in teams and (stats[team][1] == None or pass_yds > stats[team][1][1])):
                qb = []
                qb.append(float(row.find('td', attrs={"data-stat": "pass_cmp_perc"}).text))
                qb.append(int(row.find('td', attrs={"data-stat": "pass_yds"}).text))
                qb.append(int(row.find('td', attrs={"data-stat": "pass_td"}).text))
                qb.append(int(row.find('td', attrs={"data-stat": "pass_int"}).text))
                if (year > 1994):
                    qb.append(int(row.find('td', attrs={"data-stat": "pass_first_down"}).text))
                else:
                    qb.append(int(0))
                qb.append(float(row.find('td', attrs={"data-stat": "pass_adj_yds_per_att"}).text))
                qb.append(float(row.find('td', attrs={"data-stat": "pass_yds_per_cmp"}).text))
                qb.append(float(row.find('td', attrs={"data-stat": "pass_yds_per_g"}).text))
                qb.append(int(row.find('td', attrs={"data-stat": "pass_sacked"}).text))
                qb.append(float(row.find('td', attrs={"data-stat": "pass_sacked_perc"}).text))
                gwd = row.find('td', attrs={"data-stat": "gwd"}).text
                if (len(gwd) > 0):
                    qb.append(int(row.find('td', attrs={"data-stat": "gwd"}).text))
                else:
                    qb.append(int(0))
                stats[team][1] = qb

def setRBStats(year):
    url = f"https://www.pro-football-reference.com/years/{year}/rushing.htm"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table", id="rushing")
    body = table.find("tbody")
    rows = body.find_all("tr")
    for row in rows:
        if (row.find('td', attrs={"data-stat": "rush_yds"})):
            team = row.find('td', attrs={"data-stat": "team"}).text
            rush_yds = int(row.find('td', attrs={"data-stat": "rush_yds"}).text)
            if (team in teams and (stats[team][2] == None or rush_yds > stats[team][2][0])):
                rb = []
                rb.append(int(row.find('td', attrs={"data-stat": "rush_yds"}).text))
                rb.append(int(row.find('td', attrs={"data-stat": "rush_td"}).text))
                if (year > 1993):
                    rb.append(int(row.find('td', attrs={"data-stat": "rush_first_down"}).text))
                else:
                    rb.append(int(0))
                rb.append(float(row.find('td', attrs={"data-stat": "rush_yds_per_att"}).text))
                rb.append(int(row.find('td', attrs={"data-stat": "fumbles"}).text))
                stats[team][2] = rb

def setWRStats(year, rank):
    url = f"https://www.pro-football-reference.com/years/{year}/receiving.htm"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table", id="receiving")
    body = table.find("tbody")
    rows = body.find_all("tr")
    for row in rows:
        if (row.find('td', attrs={"data-stat": "rec_yds"})):
            pos = row.find('td', attrs={"data-stat": "pos"}).text
            team = row.find('td', attrs={"data-stat": "team"}).text
            rec_yards = int(row.find('td', attrs={"data-stat": "rec_yds"}).text)
            if (pos == "WR" and team in teams and (stats[team][2+rank] == None or rec_yards > stats[team][2+rank][1])
            and (stats[team][3] == None or stats[team][3][1] != rec_yards) 
            and (stats[team][4] == None or stats[team][4][1] != rec_yards) 
            and (stats[team][5] == None or stats[team][5][1] != rec_yards) ):
                wr = []
                catchperc = row.find('td', attrs={"data-stat": "catch_pct"}).text
                catchperc = float(catchperc[:catchperc.index("%")])
                wr.append(catchperc)
                wr.append(int(row.find('td', attrs={"data-stat": "rec_yds"}).text))
                wr.append(int(row.find('td', attrs={"data-stat": "rec_td"}).text))
                if (year > 1993):
                    wr.append(int(row.find('td', attrs={"data-stat": "rec_first_down"}).text))
                else:
                    wr.append(int(0))
                wr.append(float(row.find('td', attrs={"data-stat": "rec_yds_per_rec"}).text))
                wr.append(float(row.find('td', attrs={"data-stat": "rec_yds_per_tgt"}).text))
                wr.append(int(row.find('td', attrs={"data-stat": "fumbles"}).text))
                wr.append(row.find('td', attrs={"data-stat": "player"}).text)
                stats[team][2+rank] = wr

def setTEStats(year):
    url = f"https://www.pro-football-reference.com/years/{year}/receiving.htm"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table", id="receiving")
    body = table.find("tbody")
    rows = body.find_all("tr")
    for row in rows:
        if (row.find('td', attrs={"data-stat": "rec_yds"})):
            pos = row.find('td', attrs={"data-stat": "pos"}).text
            team = row.find('td', attrs={"data-stat": "team"}).text
            rec_yards = int(row.find('td', attrs={"data-stat": "rec_yds"}).text)
            if (pos == "TE" and team in teams and (stats[team][6] == None or rec_yards > stats[team][6][1])):
                te = []
                catchperc = row.find('td', attrs={"data-stat": "catch_pct"}).text
                catchperc = float(catchperc[:catchperc.index("%")])
                te.append(catchperc)
                te.append(int(row.find('td', attrs={"data-stat": "rec_yds"}).text))
                te.append(int(row.find('td', attrs={"data-stat": "rec_td"}).text))
                if (year > 1993):
                    te.append(int(row.find('td', attrs={"data-stat": "rec_first_down"}).text))
                else:
                    te.append(int(0))
                te.append(float(row.find('td', attrs={"data-stat": "rec_yds_per_rec"}).text))
                te.append(float(row.find('td', attrs={"data-stat": "rec_yds_per_tgt"}).text))
                te.append(int(row.find('td', attrs={"data-stat": "fumbles"}).text))
                te.append(row.find('td', attrs={"data-stat": "player"}).text)
                stats[team][6] = te

def setOLStats():
    for team in teams:
        print(team)
        ol = []
        ol.append(stats[team][1][8])
        ol.append(stats[team][1][9])
        ol.append(stats[team][2][3])
        stats[team][7] = ol

def setDLStats(year):
    url = f"https://www.pro-football-reference.com/years/{year}/opp.htm"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table", id="advanced_defense")
    body = table.find("tbody")
    rows = body.find_all("tr")
    for row in rows:
        if (row.find('td', attrs={"data-stat": "g"})):
            index = full_teams.index(row.find('a').text)
            team = teams[index]
            dl = []
            dl.append(int(row.find('td', attrs={"data-stat": "blitzes"}).text))
            blitzperc = row.find('td', attrs={"data-stat": "blitz_pct"}).text
            dl.append(float(blitzperc[:blitzperc.index("%")]))
            dl.append(int(row.find('td', attrs={"data-stat": "qb_hurry"}).text))
            hurryperc = row.find('td', attrs={"data-stat": "qb_hurry_pct"}).text
            dl.append(float(hurryperc[:hurryperc.index("%")]))
            dl.append(float(row.find('td', attrs={"data-stat": "qb_knockdown"}).text))
            knockperc = row.find('td', attrs={"data-stat": "qb_knockdown_pct"}).text
            dl.append(float(knockperc[:knockperc.index("%")]))
            dl.append(int(row.find('td', attrs={"data-stat": "sacks"}).text))
            dl.append(int(row.find('td', attrs={"data-stat": "pressures"}).text))
            pressureperc = row.find('td', attrs={"data-stat": "pressures_pct"}).text
            dl.append(float(pressureperc[:pressureperc.index("%")]))
            stats[team][8] = dl

def setLBStats(year):
    url = f"https://www.pro-football-reference.com/years/{year}/opp.htm"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table", id="team_stats")
    body = table.find("tbody")
    rows = body.find_all("tr")
    for row in rows:
        if (row.find('td', attrs={"data-stat": "g"})):
            index = full_teams.index(row.find('a').text)
            team = teams[index]
            lb = []
            lb.append(int(row.find('td', attrs={"data-stat": "total_yards"}).text))
            lb.append(int(row.find('td', attrs={"data-stat": "points"}).text))
            lb.append(float(row.find('td', attrs={"data-stat": "yds_per_play_offense"}).text))
            lb.append(int(row.find('td', attrs={"data-stat": "fumbles_lost"}).text))
            lb.append(float(row.find('td', attrs={"data-stat": "pass_net_yds_per_att"}).text))
            lb.append(int(row.find('td', attrs={"data-stat": "rush_yds"}).text))
            lb.append(int(row.find('td', attrs={"data-stat": "rush_td"}).text))
            lb.append(float(row.find('td', attrs={"data-stat": "rush_yds_per_att"}).text))
            lb.append(int(row.find('td', attrs={"data-stat": "penalties"}).text))
            lb.append(int(row.find('td', attrs={"data-stat": "penalties_yds"}).text))
            stats[team][9] = lb

def setDBStats(year):
    url = f"https://www.pro-football-reference.com/years/{year}/opp.htm"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table", id="team_stats")
    body = table.find("tbody")
    rows = body.find_all("tr")
    for row in rows:
        if (row.find('td', attrs={"data-stat": "g"})):
            index = full_teams.index(row.find('a').text)
            team = teams[index]
            db = []
            db.append(int(row.find('td', attrs={"data-stat": "pass_cmp"}).text))
            db.append(int(row.find('td', attrs={"data-stat": "pass_yds"}).text))
            db.append(int(row.find('td', attrs={"data-stat": "pass_td"}).text))
            db.append(int(row.find('td', attrs={"data-stat": "pass_int"}).text))
            db.append(float(row.find('td', attrs={"data-stat": "pass_net_yds_per_att"}).text))
            db.append(int(row.find('td', attrs={"data-stat": "pass_fd"}).text))
            db.append(int(row.find('td', attrs={"data-stat": "turnovers"}).text))
            db.append(int(row.find('td', attrs={"data-stat": "penalties"}).text))
            db.append(int(row.find('td', attrs={"data-stat": "penalties_yds"}).text))
            db.append(float(row.find('td', attrs={"data-stat": "turnover_pct"}).text))
            db.append(int(row.find('td', attrs={"data-stat": "total_yards"}).text))
            db.append(int(row.find('td', attrs={"data-stat": "points"}).text))
            stats[team][10] = db

def setDStats(year):
    url = f"https://www.pro-football-reference.com/years/{year}/fantasy-points-against-QB.htm"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table", id="fantasy_def")
    body = table.find("tbody")
    rows = body.find_all("tr")
    for row in rows:
        if (row.find('td', attrs={"data-stat": "g"})):
            scks = []
            index = full_teams.index(row.find('a').text)
            team = teams[index]
            scks.append(int(row.find('td', attrs={"data-stat": "pass_sacked"}).text))
            stats[team][8] = scks
    url = f"https://www.pro-football-reference.com/years/{year}/opp.htm"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table", id="team_stats")
    body = table.find("tbody")
    rows = body.find_all("tr")
    for row in rows:
        if (row.find('td', attrs={"data-stat": "g"})):   
            other = []
            index = full_teams.index(row.find('a').text)
            team = teams[index]
            other.append(int(row.find('td', attrs={"data-stat": "turnovers"}).text))
            other.append(int(row.find('td', attrs={"data-stat": "total_yards"}).text))
            other.append(int(row.find('td', attrs={"data-stat": "points"}).text))
            stats[team][9] = other

def setStatBaseForYear(year):
    if (year < 2022):
        full_teams[31] = "Washington Football Team"
    if (year < 2020):
        full_teams[31] = "Washington Redskins"
        full_teams[16] = "Oakland Raiders"
        teams[16] = "OAK"
    if (year < 2017):
        full_teams[17] = "San Diego Chargers"
        teams[17] = "SDG"
    if (year < 2016):
        full_teams[18] = "St. Louis Rams"
        teams[18] = "STL"
    if (year < 2002):
        full_teams.pop(12)
        teams.pop(12)
    if (year < 1999):
        full_teams[29] = "Tennessee Oilers"
        full_teams.pop(7)
        teams.pop(7)
    if (year < 1997):
        full_teams[28] = "Houston Oilers"
        teams[28] = "HOU"
    if (year < 1996):
        full_teams[2] = "Cleveland Browns"
        teams[2] = "CLE"
    if (year < 1995):
        full_teams.pop(4)
        teams.pop(4)
        full_teams.pop(11)
        teams.pop(11)
        full_teams[12] = "Los Angeles Raiders"
        teams[12] = "RAI"
        full_teams[14] = "Los Angeles Rams"
        teams[14] = "RAM"
    if (year < 1994):
        full_teams[0] = "Phoenix Cardinals"
        teams[0] = "PHO"

    for team in teams:
        stats[team] = [None] * 11

def createYearStatsArray():
    year_stats = []
    for team in teams:
        combined_array = [stats[team][0]]
        for element in stats[team][1:]:
            if isinstance(element, (list, tuple)):
                combined_array.extend(element)
            else:
                combined_array.append(element)
        year_stats.append(combined_array)
    return year_stats

def getYearStats(year):
    setStatBaseForYear(year)
    setTeamWins(year)
    setQBStats(year)
    setRBStats(year)
    setWRStats(year, 1)
    setWRStats(year, 2)
    setWRStats(year, 3)
    setTEStats(year)
    setOLStats()
    #setDLStats(year)
    #setLBStats(year)
    #setDBStats(year)
    setDStats(year)
    return createYearStatsArray()

def writeCSVStats(year):
    with open('data/stat_swapper.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(row_names)
        year_stats = getYearStats(year)
        writer.writerows(year_stats)

def writeToSmallCSVSwapper():
    csv_file = 'stat_swapper.csv'
    small_stats = [ "Wins", 
                    "QB:Comp%", "QB:Pass Yds", "QB:Pass TD", "QB:Int",
                    "RB:Rush Yds", "RB:Rush TD", "RB:Yds/rush", "RB:Fumbles",
                    "WR1:Catch%", "WR1:Rec Yds", "WR1:Rec TD",
                    "WR2:Catch%", "WR2:Rec Yds", "WR2:Rec TD",
                    "WR3:Catch%", "WR3:Rec Yds", "WR3:Rec TD",
                    "TE:Catch%", "TE:Rec Yds", "TE:Rec TD",
                    "OL:Sacked", "OL:Sacked/g", "OL:Yds/rush",
                    "DL:Blitzes", "DL:Blitz%", "DL:Hurries", "DL:Hurry%" ]
    df = pd.read_csv(csv_file)
    selected_columns_df = df[small_stats]
    selected_columns_df.to_csv('data/small_stat_swapper.csv', index=False)

def setSmallStatNames():
    for team in teams:
        stats[team] = [None] * 11
    # Read the input CSV file
    with open("data/small_stats_2022.csv", 'r') as input_file:
        reader = csv.reader(input_file)
        rows = list(reader)
    for i in range(32):
        rows[i].insert(32, teams[i])
    # Write the updated data to the output CSV file
    with open("data/small_stat_swapper.csv", 'w', newline='') as output_file:
        writer = csv.writer(output_file)
        writer.writerows(rows)

def setTeamWinPercentages(firstYear, lastYear):
    allWinPercs = []
    index = 0
    for year in range(firstYear, lastYear + 1):
        resetTeams()
        setStatBaseForYear(year)
        url = f"https://www.pro-football-reference.com/years/{year}/"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        table = soup.find("table", id="AFC")
        body = table.find("tbody")
        rows = body.find_all("tr")
        for row in rows:
            if (row.find('th', attrs={"data-stat": "team"})):
                full_team = row.find('th', attrs={"data-stat": "team"}).text
                team = teams[full_teams.index[full_team]]
                if (team in teams and stats[team][0] == None):
                    stats[team][0] = float(row.find('td', attrs={"data-stat": "win_loss_perc"}).text)
        table = soup.find("table", id="NFC")
        body = table.find("tbody")
        rows = body.find_all("tr")
        for row in rows:
            if (row.find('th', attrs={"data-stat": "team"})):
                full_team = row.find('th', attrs={"data-stat": "team"}).text
                team = teams[full_teams.index[full_team]]
                if (team in teams and stats[team][0] == None):
                    stats[team][0] = float(row.find('td', attrs={"data-stat": "win_loss_perc"}).text)

    with open('data/small_stats.csv', 'r') as input_file, open('data/small_stats_swapper.csv', 'w', newline='') as output_file:
        reader = csv.reader(input_file)
        writer = csv.writer(output_file)
        for row in reader:
            row[0] = allWinPercs[index]
            index = index + 1
            writer.writerow(row)

#setTeamWinPercentages(1994, 2022)

# we have 29 years of stats, 1994-2022

#writeCSVStats(1993)
# small stats
    # wins
    # qb: yds, tds, ints, comp%
    # rb: yds, tds, yds/rush, fumbles
    # wr/te: yds, tds, catch%
    # def: sacks, points, yards/play, turnovers
#writeToSmallCSVSwapper()

print("Data scraped and transferred.")