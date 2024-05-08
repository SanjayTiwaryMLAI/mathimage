import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Set the context and question
context = "ABCDEF is a hexagon (six-sided polygon). Find the value of AB+BC+CD+DE+AF+FE+AE?"

# Define the vertices of the hexagon
vertices = np.array([[0, 0], [2, 0], [3, 1.73], [2, 3.46], [0, 3.46], [-1, 1.73]])

# Create a figure and axis
fig, ax = plt.subplots(figsize=(4, 4), dpi=300)

# Draw the hexagon
ax.plot(vertices[:, 0], vertices[:, 1], 'k-')
ax.plot([vertices[-1, 0], vertices[0, 0]], [vertices[-1, 1], vertices[0, 1]], 'k-')

# Label the vertices
for i, (x, y) in enumerate(vertices):
    ax.text(x, y, chr(65 + i), ha='center', va='center', fontsize=12)

# Set the axis limits and remove ticks
ax.set_xlim(-2, 4)
ax.set_ylim(-1, 5)
ax.set_xticks([])
ax.set_yticks([])

# Add the context and question as a title
ax.set_title(f"{context}", fontsize=10, wrap=True)

# Save the plot as a JPEG file
plt.savefig("hexagon.jpg", dpi=300, bbox_inches='tight')

