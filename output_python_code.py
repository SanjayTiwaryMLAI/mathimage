import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Set the context for the image
context = "ABCDEF is a hexagon (six-sided polygon). Find the value of AB+BC+CD+DE+AF+FE+AE"

# Define the vertices of the hexagon
vertices = np.array([[0, 0], [1, 0], [1.5, 0.866], [1, 1.732], [0, 1.732], [-0.5, 0.866]])

# Create a figure and axis
fig, ax = plt.subplots(figsize=(8, 6))

# Draw the hexagon
ax.plot(vertices[:, 0], vertices[:, 1], 'k-')
ax.plot([vertices[-1, 0], vertices[0, 0]], [vertices[-1, 1], vertices[0, 1]], 'k-')  # Close the loop

# Label the vertices
for i, (x, y) in enumerate(vertices):
    ax.text(x, y, chr(65 + i), fontsize=12, ha='center', va='center')

# Add the context to the top of the image
ax.text(0.5, 1.05, context, transform=ax.transAxes, fontsize=12, ha='center', va='bottom')

# Set axis limits and remove ticks
ax.set_xlim([-1, 2])
ax.set_ylim([-0.5, 2.2])
ax.set_xticks([])
ax.set_yticks([])

# Set aspect ratio to ensure equal-sided hexagon
ax.set_aspect('equal')

# Save the figure as a JPG file
plt.savefig('hexagon.jpg', dpi=300, bbox_inches='tight')

