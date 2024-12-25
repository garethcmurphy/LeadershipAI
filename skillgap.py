import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load team skills data
data = pd.read_csv('team_skills.csv')  # Columns: ['member', 'skill_1', 'skill_2', 'skill_3', ...]

# Clustering
X = data.iloc[:, 1:]  # Skills columns
kmeans = KMeans(n_clusters=3, random_state=42)
data['cluster'] = kmeans.fit_predict(X)

# Visualize clusters
plt.scatter(X.iloc[:, 0], X.iloc[:, 1], c=data['cluster'], cmap='viridis')
plt.xlabel('Skill 1')
plt.ylabel('Skill 2')
plt.title('Skill Clusters')
plt.show()

# Identify skill gaps by cluster
for cluster in range(3):
    cluster_data = data[data['cluster'] == cluster]
    print(f"Cluster {cluster} Average Skills:\n", cluster_data.iloc[:, 1:].mean())
