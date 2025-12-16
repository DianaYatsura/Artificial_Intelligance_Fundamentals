import cv2 as cv
import numpy as np
from sklearn.cluster import KMeans  # Import KMeans class from scikit-learn
import os
from urllib.request import urlopen

def detect_dominant_color(image_path):
    """
    Detects the dominant color in an image and calculates its presence percentage.

    Args:
        image_path (str): Path to the input image file.

    Returns:
        dominant_color (tuple): RGB values of the detected dominant color.
        percentage (float): Percentage of the dominant color's presence in the image.
    """
    # Read the image
    if os.path.exists(image_path):
      img = cv.imread(image_path)
    else:
      url = f'https://github.com/mehalyna/cooltest/raw/master/cooltest/{image_path}'
      data = urlopen(url).read()
      with open(image_path, 'wb') as f:
          f.write(data)
      img = cv.imread(image_path)

    # Convert image from BGR to HSV color space
    img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    # Flatten the HSV image into array
    hsv_flattened = img_hsv.reshape(-1, 3)

    # Apply K-Means clustering, number of clusters (you can adjust this)
    kmeans = KMeans(n_clusters=3, random_state=42)
    kmeans.fit(hsv_flattened)

    # Get the dominant color cluster
    labels, counts = np.unique(kmeans.labels_, return_counts=True)
    dominant_index = np.argmax(counts)
    dominant_hsv = kmeans.cluster_centers_[dominant_index].astype(int)

    # Convert dominant color from HSV to RGB
    dominant_hsv = np.uint8([[dominant_hsv]])
    dominant_rgb = cv.cvtColor(dominant_hsv, cv.COLOR_HSV2RGB)[0][0]
    dominant_color = int(dominant_rgb[2]), int(dominant_rgb[1]), int(dominant_rgb[0])

    # Calculate the percentage of dominant color's presence
    percentage = counts[dominant_index] / hsv_flattened.shape[0] * 100
    return dominant_color, percentage

# Path to the input image
image_path = '/content/drive/MyDrive/sunflowers.png'

# Call the function and get the results
dominant_color, percentage = detect_dominant_color(image_path)

# Print the results
print(f"Dominant Color: {dominant_color}")
print(f"Percentage: {percentage:.2f}%")
