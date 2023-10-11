import matplotlib.pyplot as plt
import re

embedding_dict = {}

with open('output/embedding.txt', 'r') as f:
    for line in f:
        if ':' in line:
            word, coords_str = line.strip().split(':')
            coords = [float(x) for x in re.findall(r"[-+]?\d*\.\d+|\d+", coords_str)]
        else:
            coords_str = line.strip()
            coords += [float(x) for x in re.findall(r"[-+]?\d*\.\d+|\d+", coords_str)]
        embedding_dict[word] = coords

# Create the scatter plot (only first two dimensions)
plt.figure(figsize=(10, 10))
for word, coords in embedding_dict.items():
    plt.scatter(coords[0], coords[1])
    plt.annotate(word, (coords[0], coords[1]))

# Show the plot
plt.show()