import matplotlib.pyplot as plt
import re
import numpy as np
from sklearn.manifold import TSNE

embedding_dict = {}
word_coords = []

with open('output/embedding.txt', 'r') as f:
    for line in f:
        if ':' in line:
            if word_coords:  # Save the previous word_coords
                embedding_dict[word] = word_coords
            
            word, coords_str = line.strip().split(':')
            word_coords = [float(x) for x in re.findall(r"[-+]?\d*\.\d+|\d+", coords_str)]
        else:
            coords_str = line.strip()
            word_coords += [float(x) for x in re.findall(r"[-+]?\d*\.\d+|\d+", coords_str)]

    embedding_dict[word] = word_coords  # Save the last word_coords

word_list = list(embedding_dict.keys())
vector_lengths = [len(embedding_dict[word]) for word in word_list]

# Find the common vector length (ignoring unusually long vectors)
from collections import Counter
common_length = Counter(vector_lengths).most_common(1)[0][0]

# Filter out any word with an unusually long or short vector
filtered_word_list = [word for word in word_list if len(embedding_dict[word]) == common_length]

embeddings_matrix = np.array([embedding_dict[word] for word in filtered_word_list])

# Apply t-SNE dimensionality reduction
tsne = TSNE(n_components=2, random_state=42, perplexity=len(filtered_word_list) - 1)  # Set perplexity based on n_samples
reduced_embeddings = tsne.fit_transform(embeddings_matrix)

# Create the scatter plot
plt.figure(figsize=(10, 10))
for i, word in enumerate(filtered_word_list):
    coords = reduced_embeddings[i]
    plt.scatter(coords[0], coords[1])
    plt.annotate(word, (coords[0], coords[1]))

# Show the plot
plt.show()