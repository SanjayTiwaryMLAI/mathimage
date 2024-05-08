import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Set the context and question
context = "What are the three coordinates used to represent a point in 3D space?"

# Set the figure size and resolution
fig, ax = plt.subplots(figsize=(4, 4), dpi=300)

# Set the axis limits
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_zlim([-1, 1])

# Draw the point
point_x, point_y, point_z = 0, 0, 0
ax.scatter(point_x, point_y, point_z, color='red', s=50, label='Point')

# Label the axes
ax.set_xlabel('X', fontsize=10)
ax.set_ylabel('Y', fontsize=10)
ax.set_zlabel('Z', fontsize=10)

# Add the context at the top
ax.text(0, 1.1, context, ha='center', va='bottom', fontsize=10, transform=ax.transAxes)

# Add a legend
ax.legend(fontsize=8)

# Set the aspect ratio to equal
ax.set_box_aspect((1, 1, 1))

# Remove the grid and tick labels
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])
ax.grid(False)

# Save the plot as an image
plt.savefig('point.jpg', dpi=300, bbox_inches='tight', pad_inches=0.1)

