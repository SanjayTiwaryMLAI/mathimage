import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Set the context/question
context = "What are the three coordinates used to represent a point in 3D coordinate geometry?"

# Create a small image with fixed size pixels
fig, ax = plt.subplots(figsize=(5, 5))

# Add the context into the image at the top
ax.set_title(context, fontsize=12, pad=20)

# Draw the point
point_x, point_y, point_z = 0, 0, 0  # Coordinates of the point
ax.scatter(point_x, point_y, point_z, s=100, color='red', marker='o', label='Point')

# Label the axes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Set axis limits
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_zlim(-1, 1)

# Add a legend
ax.legend()

# Save the plot as point.jpg
plt.savefig('point.jpg', dpi=300, bbox_inches='tight')

