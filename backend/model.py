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
        small_stats = [ { also something very cool & fancy } ]
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
