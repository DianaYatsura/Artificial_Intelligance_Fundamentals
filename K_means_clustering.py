import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def load_dataset(file_path):
    """
    Load a dataset from a CSV file.

    This function reads a CSV file located at the specified 'file_path' and returns
    the dataset as a pandas DataFrame.

    Args:
        file_path (str): The path to the CSV file to be loaded.

    Returns:
        pandas.DataFrame: The loaded dataset as a DataFrame.

    """
    dataset = pd.read_csv(file_path)

    return dataset

def preprocess_data(dataset, selected_features):
    """
    Scales selected features from the given dataset.

    This function applies standard scaling to the specified features in the dataset to normalize their values.

    Args:
      dataset (pandas.DataFrame): The dataset from which features are selected.
      selected_features (list): List of column names from the dataset to be scaled.

    Returns:
      numpy.ndarray: Scaled values of the selected features.
    """
    X = dataset[selected_features].values
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    return X_scaled

def apply_kmeans_clustering(X_scaled, num_clusters):
    """
    Apply K-means clustering to scaled data.

    This function applies the K-means clustering algorithm to the scaled feature matrix
    'X_scaled' using the specified number of clusters 'num_clusters'. It returns the
    cluster assignments for each data point and the cluster centers.

    Args:
        X_scaled (array-like): Scaled feature matrix for clustering.
        num_clusters (int): Number of clusters to form.

    Returns:
        tuple: A tuple containing:
            - clusters (array-like): Cluster assignments for each data point.
            - cluster_centers (array-like): Coordinates of cluster centers.

    """

    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    kmeans.fit(X_scaled)
    clusters = kmeans.labels_

    return clusters, kmeans.cluster_centers_

def visualize_clusters(X_scaled, clusters, cluster_centers, feature_names=None):
    """
    Apply K-means clustering to scaled data.

    This function applies the K-means clustering algorithm to the scaled feature matrix
    'X_scaled' using the specified number of clusters 'num_clusters'. It returns the
    cluster assignments for each data point and the cluster centers.

    Args:
        X_scaled (array-like): Scaled feature matrix for clustering.
        num_clusters (int): Number of clusters to form.

    Returns:
        tuple: A tuple containing:
            - clusters (array-like): Cluster assignments for each data point.
            - cluster_centers (array-like): Coordinates of cluster centers.

    """
    plt.figure(figsize=(8, 6))

    plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=clusters, cmap='plasma', s=40)

    plt.scatter(cluster_centers[:, 0], cluster_centers[:, 1], c='red', s=50, marker='X', label='Centroids')

    if feature_names and len(feature_names) >= 2:
        plt.xlabel(feature_names[0])
        plt.ylabel(feature_names[1])
    else:
        plt.xlabel('Feature 1')
        plt.ylabel('Feature 2')

    plt.title('K-means Clustering')
    plt.legend()
    plt.show()
    return None

# Load the dataset
file_path = r'https://drive.google.com/uc?export=download&id=1Gs3nFWs_nfS4CcQm6YxF3JIaM__lClcR'  # Replace with actual file path
data = load_dataset(file_path)

# Selected features for clustering
selected_features = ['feature1', 'feature2']  # Replace with actual feature names

# Preprocess the data
X_scaled = preprocess_data(data, selected_features)

# Choose the number of clusters (K)
num_clusters = 3  # Replace with the desired number of clusters

# Apply K-Means clustering
clusters, cluster_centers = apply_kmeans_clustering(X_scaled, num_clusters)

# Visualize the clusters
visualize_clusters(X_scaled, clusters, cluster_centers)
