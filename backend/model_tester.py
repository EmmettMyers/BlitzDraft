from pandas import read_csv
from matplotlib import pyplot
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

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
X_train, X_validation, Y_train, Y_validation = train_test_split(X, y, test_size=0.20, random_state=1, shuffle=True)

# Spot Check Algorithms
models = []
models.append(('LR', LogisticRegression(solver='liblinear', multi_class='ovr')))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC(gamma='auto')))

# evaluate each model in turn
results = []
names = []
for name, model in models:
	kfold = StratifiedKFold(n_splits=10, random_state=1, shuffle=True)
	cv_results = cross_val_score(model, X_train, Y_train, cv=kfold, scoring='accuracy')
	results.append(cv_results)
	names.append(name)
	print('%s: %f (%f)' % (name, cv_results.mean(), cv_results.std()))
	
# Compare Algorithms
pyplot.boxplot(results, labels=names)
pyplot.title('Algorithm Comparison')
pyplot.show()