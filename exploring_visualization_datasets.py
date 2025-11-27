import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_dataset(file_path):
    """
    Load the dataset from the specified file path.

    Parameters:
    file_path (str): Path to the dataset file.

    Returns:
    pd.DataFrame: Loaded dataset as a Pandas DataFrame.
    """
    dataset = pd.read_csv(file_path)
    return dataset

def inspect_data(dataset, num_rows=5):
    """
    Display the first few rows of the dataset.

    Parameters:
    dataset (pd.DataFrame): Loaded dataset.
    num_rows (int): Number of rows to display.
    """
    print("*** The first few rows of the dataset ***")
    print(dataset.head(num_rows))
    return dataset.head(num_rows)

def calculate_summary_statistics(dataset):
    """
    Calculate summary statistics for numerical columns in the dataset.

    Parameters:
    dataset (pd.DataFrame): Loaded dataset.

    Returns:
    pd.DataFrame: Summary statistics.
    """
    summary_stats = dataset.describe()
    print(summary_stats)
    return summary_stats

def visualize_data(dataset):
    """
    Create visualizations to explore the dataset.

    Parameters:
    dataset (pd.DataFrame): Loaded dataset.
    """
    # Example: Histograms for numerical columns
    numeric_cols = dataset.select_dtypes(include=['number']).columns

    if len(numeric_cols) > 0:
        dataset[numeric_cols].hist(figsize=(12, 8), bins=20, edgecolor='black')
        plt.suptitle("Histograms of Numerical Features", fontsize=16)
        plt.tight_layout()
        plt.show()
    else:
        print("No numerical columns found for histograms.")

    # Example: Correlation heatmap
    if len(numeric_cols) > 1:
        plt.figure(figsize=(10, 6))
        corr_matrix = dataset[numeric_cols].corr()

        sns.heatmap(
            corr_matrix,
            annot=True,
            fmt=".2f",
            cmap="coolwarm",
            linewidths=0.5
        )
        plt.title("Correlation Heatmap")
        plt.show()
    else:
        print("Not enough numerical columns for a correlation heatmap.")

    return None

def handle_missing_values(dataset):
    """
    Handle missing values in the dataset.

    Parameters:
    dataset (pd.DataFrame): Loaded dataset.

    Returns:
    pd.DataFrame: Dataset with missing values handled.
    """
    # Example: Fill missing values with column mean

    dataset_filled = dataset.copy()

    numeric_cols = dataset_filled.select_dtypes(include=['number']).columns
    dataset_filled[numeric_cols] = dataset_filled[numeric_cols].fillna(dataset_filled[numeric_cols].mean())

    categorical_cols = dataset_filled.select_dtypes(include=['object']).columns

    for col in categorical_cols:
        if dataset_filled[col].isnull().sum() > 0:
            dataset_filled[col] = dataset_filled[col].fillna(dataset_filled[col].mode()[0])

    return dataset_filled

# Load the dataset
file_path = r"https://drive.google.com/uc?export=download&id=1g8FMBY5wQaw9jyjPKfvdEnHdZ1Efr90N"  # Replace with the actual file path
data = load_dataset(file_path)

# Perform data exploration
inspect_data(data)
summary_stats = calculate_summary_statistics(data)
visualize_data(data)
data_filled = handle_missing_values(data)

