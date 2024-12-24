import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# Load your dataset (example structure)
data = pd.read_csv('project_data.csv')  # Columns: ['team_size', 'complexity', 'duration', 'past_budget', 'actual_budget']

# Features and target
X = data[['team_size', 'complexity', 'duration', 'past_budget']]
y = data['actual_budget']

# Split into train/test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
print("MSE:", mean_squared_error(y_test, y_pred))

# Predict budget for a new project
new_project = [[10, 3, 120, 50000]]  # Example input
predicted_budget = model.predict(new_project)
print("Predicted Budget:", predicted_budget[0])