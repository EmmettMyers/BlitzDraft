from pandas import read_csv
from matplotlib import pyplot
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# Load dataset
url = "data/small_stats.csv"
small_stats = [ { sick stats over here } ]
dataset = read_csv(url, names=small_stats)

# Split-out validation dataset
X = dataset.drop("Wins", axis=1)
y = dataset["Wins"]
X_train, X_validation, Y_train, Y_validation = train_test_split(X, y, test_size=0.20, random_state=1, shuffle=True)

# Train the model
model = RandomForestRegressor()
model.fit(X_train, Y_train)

# Get feature importances
importance = model.feature_importances_

# Calculate decreasing importances
decreasing_importance = 1 - importance

# Sort feature importances in descending order for increasing wins
increasing_indices = importance.argsort()[::-1]
increasing_importance = importance[increasing_indices]

# Sort feature importances in descending order for decreasing wins
decreasing_indices = decreasing_importance.argsort()[::-1]
decreasing_importance = decreasing_importance[decreasing_indices]

# Get feature names for increasing and decreasing wins
feature_names = X.columns

# Visualize feature importances for increasing wins
fig, axs = pyplot.subplots(2, 1, figsize=(8, 10))
axs[0].barh(range(len(increasing_importance)), increasing_importance, tick_label=feature_names[increasing_indices])
axs[0].set_title('Feature Importances for Increasing Wins')

# Visualize feature importances for decreasing wins
axs[1].barh(range(len(decreasing_importance)), decreasing_importance, tick_label=feature_names[decreasing_indices])
axs[1].set_title('Feature Importances for Decreasing Wins')

pyplot.tight_layout()
pyplot.show()
