import pandas as pd
from sklearn.ensemble import IsolationForest

# Load dataset metadata
data = pd.read_csv('dataset_metadata.csv')  # Columns: ['dataset_id', 'completeness', 'consistency', 'accuracy']

# Train anomaly detection model
model = IsolationForest(contamination=0.1, random_state=42)
data['anomaly'] = model.fit_predict(data[['completeness', 'consistency', 'accuracy']])

# Identify datasets needing attention
anomalies = data[data['anomaly'] == -1]
print("Datasets Needing Attention:\n", anomalies)
