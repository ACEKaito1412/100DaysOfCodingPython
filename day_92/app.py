import cv2 as cv
import numpy as np

img = cv.imread('image/cat.jpg')

np_img = np.asarray(img)
array = np_img.reshape(-1, 3)

print(array.shape)

unique_colors, counts = np.unique(array, axis=0, return_counts=True)


sorted_indices = np.argsort(-counts)  # negative for descending order
sorted_colors = unique_colors[sorted_indices]
sorted_counts = counts[sorted_indices]

for i in range(10):
    print(f"color: {sorted_colors[sorted_counts[i]]} : id: {sorted_counts[i]} {i}")