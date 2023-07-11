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

        # Predicting good vs bad team wins
        """
        good_team = [67.1,5250,41,12, # Mahomes
                    1538,13,4.4,6, # Henry
                    72.8,1553,11, # Adams
                    70.0,1710,7, # Hill
                    70.1,1429,11, # Diggs
                    69.9,1361,9, # Andrews
                    25,6.2,4.0, # Saints OL
                    44,277,5.0,15.3] # 49ers D
        bad_team = [60.4,2242,17,11, # Fields
                    891,3,4.9,1, # Mostert
                    58.7,829,2, # Sutton
                    51.9,687,2, # Peoples-Jones
                    69.8,804,6, # Meyers
                    66.1,406,4, # Ertz
                    55,14.7,4.0, # Bears OL
                    39,420,5.7,11.9] # Texans D
        """

        wins += (model.predict([stats]) / 16) * 17

    wins /= loops
    wins = round(wins[0])
    return wins