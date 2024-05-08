import matplotlib.pyplot as plt
import numpy as np

# Define the context
context = "ABCDEF is a hexagon (six-sided polygon). Find the value of AB+BC+CD+DE+AF+FE+AE ?"

# Define the vertices of the hexagon
vertices = np.array([[0, 0], [1, 0], [1.5, 0.866], [1, 1.732], [0, 1.732], [-0.5, 0.866]])

# Define the edge labels
labels = ['A', 'B', 'C', 'D', 'E', 'F']

# Create a figure and axis
fig, ax = plt.subplots(figsize=(6, 6))

# Draw the hexagon
ax.plot(vertices[:, 0], vertices[:, 1], 'k-')
ax.plot([vertices[-1, 0], vertices[0, 0]], [vertices[-1, 1], vertices[0, 1]], 'k-')  # Connect the last vertex to the first

# Label the edges
for i, (x, y) in enumerate(vertices):
    ax.text(x, y, labels[i], fontsize=12, ha='center', va='center')

# Add the context at the top
ax.text(0.5, 1.1, context, ha='center', va='top', transform=ax.transAxes, fontsize=12)

# Set the aspect ratio and remove ticks
ax.set_aspect('equal')
ax.set_xticks([])
ax.set_yticks([])

# Save the plot as an image
plt.savefig('hexagon.jpg', dpi=100, bbox_inches='tight')

