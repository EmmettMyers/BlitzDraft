import numpy as np
from pandas import read_csv
from matplotlib import pyplot
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

def gradeTeam(stats, loops):
    stats = np.array(stats, dtype=np.float)
    wins = 0
    for i in range(loops):
        # Load dataset
        url = "data/small_stats.csv"
        small_stats = [ { something super fancy & cool } ]
        dataset = read_csv(url, names=small_stats)
        # Split-out validation dataset
        array = dataset.values
        X = array[:, 1:]
        y = array[:, 0]
        X_train, X_validation, Y_train, Y_validation = train_test_split(X, y, test_size=0.20, random_state=1)
        # Fit model to linear discriminant analysis
        model = LinearDiscriminantAnalysis()
        model.fit(X_train, Y_train)
        # Predicting wins based on model
        wins += (model.predict([stats]) / 16) * 17
    wins /= loops
    wins = round(wins[0])
    return wins

def gradeTeamMP(stats, loops):
    stats = np.array(stats, dtype=np.float)
    score = 0
    for i in range(loops):
        # Load dataset
        url = "data/small_stats.csv"
        small_stats = [ "Wins", 
                        "QB:Comp%", "QB:Pass Yds", "QB:Pass TD", "QB:Int",
                        "RB:Rush Yds", "RB:Rush TD", "RB:Yds/rush", "RB:Fumbles",
                        "WR1:Catch%", "WR1:Rec Yds", "WR1:Rec TD",
                        "WR2:Catch%", "WR2:Rec Yds", "WR2:Rec TD",
                        "WR3:Catch%", "WR3:Rec Yds", "WR3:Rec TD",
                        "TE:Catch%", "TE:Rec Yds", "TE:Rec TD",
                        "OL:Sacked", "OL:Sacked/g", "OL:Yds/rush",
                        "DL:Sacks", "LB:Points", "LB:Yds/play", "DB:Turnover%" ]
        dataset = read_csv(url, names=small_stats)
        # Split-out validation dataset
        array = dataset.values
        X = array[:, 1:]
        y = array[:, 0]
        X_train, X_validation, Y_train, Y_validation = train_test_split(X, y, test_size=0.20, random_state=1)
        # Fit model to linear discriminant analysis
        model = LinearDiscriminantAnalysis()
        model.fit(X_train, Y_train)
        score += model.predict([stats])
    return float(score)
