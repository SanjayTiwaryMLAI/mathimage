import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(8, 6))

# Add the context at the top
context = "If the adjacent sides of a parallelogram are 3i+2j and -i+4j+2k, find the area of the parallelogram."
ax.set_title(context, fontsize=12, pad=20)

# Define the coordinates of the parallelogram vertices
x = [0, 3, 2, -1]
y = [0, 2, 6, 4]

# Draw the parallelogram
sns.lineplot(x, y, marker='o', sort=False, label='Parallelogram')

# Label the edges
labels = ['A', 'B', 'C', 'D']
for i, (x_coord, y_coord, label) in enumerate(zip(x, y, labels)):
    ax.annotate(label, (x_coord, y_coord), xytext=(5, 5), textcoords='offset points')

# Set axis limits and aspect ratio
ax.set_xlim(-2, 4)
ax.set_ylim(-1, 7)
ax.set_aspect('equal')

# Remove axis ticks and spines
ax.set_xticks([])
ax.set_yticks([])
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

# Save the plot as a JPG image
plt.savefig('parallelogram.jpg', dpi=300, bbox_inches='tight')
plt.show()

