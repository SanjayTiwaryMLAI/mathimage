import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the coordinates of the three points
x1, y1, z1 = 0, 0, 0  # Point A
x2, y2, z2 = 2, 2, 2  # Point B
x3, y3, z3 = 4, 4, 4  # Point C

# Create a figure and 3D axis
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Plot the points
ax.scatter(x1, y1, z1, c='r', marker='o', label='A')
ax.scatter(x2, y2, z2, c='g', marker='o', label='B')
ax.scatter(x3, y3, z3, c='b', marker='o', label='C')

# Draw the line connecting the three points
ax.plot([x1, x2, x3], [y1, y2, y3], [z1, z2, z3], 'k-', linewidth=2)

# Set labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Condition for Three Points to be Collinear in 3D Space')

# Add a legend
ax.legend()

# Save the plot as an image
plt.savefig('line.jpg', dpi=300, bbox_inches='tight')

