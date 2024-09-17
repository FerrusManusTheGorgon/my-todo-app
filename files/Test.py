import numpy as np

# Correct cosine similarity function
def cosine(vector1, vector2):
    dot_product = np.dot(vector1, vector2)
    magnitude_product = np.linalg.norm(vector1) * np.linalg.norm(vector2)
    return dot_product / magnitude_product

# Correct Euclidean distance function
def euclidean(vector1, vector2):
    return np.linalg.norm(vector1 - vector2)

# Example usage
vector1 = np.array([15, 5 ,7, 1, 1, 0, 0, 1])
vector2 = np.array([1, 5, 7, 8, 8, 0, 0, 20])

cosine_similarity = cosine(vector1, vector2)
euclidean_distance = euclidean(vector1, vector2)

print(f"Cosine Similarity: {cosine_similarity}")
print(f"Euclidean Distance: {euclidean_distance}")
