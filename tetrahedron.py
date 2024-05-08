import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns

# Define the vertices of the tetrahedron
x1, y1, z1 = 0, 0, 0  # Vertex A
x2, y2, z2 = 1, 0, 0  # Vertex B
x3, y3, z3 = 0, 1, 0  # Vertex C
x4, y4, z4 = 0, 0, 1  # Vertex D

# Calculate the centroid (center of mass)
centroid_x = (x1 + x2 + x3 + x4) / 4
centroid_y = (y1 + y2 + y3 + y4) / 4
centroid_z = (z1 + z2 + z3 + z4) / 4

# Create a 3D figure
fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111, projection='3d')

# Set the plot limits
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_zlim([-1, 1])

# Draw the tetrahedron
vertices = np.array([[x1, y1, z1], [x2, y2, z2], [x3, y3, z3], [x4, y4, z4]])
faces = [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]]
colors = sns.color_palette("husl", len(faces))

for face, color in zip(faces, colors):
    triangle = Poly3DCollection([vertices[face]], alpha=0.5, edgecolor='k')
    triangle.set_facecolor(color)
    ax.add_collection3d(triangle)

# Label the vertices
ax.text(x1, y1, z1, 'A', fontsize=12)
ax.text(x2, y2, z2, 'B', fontsize=12)
ax.text(x3, y3, z3, 'C', fontsize=12)
ax.text(x4, y4, z4, 'D', fontsize=12)

# Add the centroid
ax.scatter(centroid_x, centroid_y, centroid_z, color='r', marker='o', s=50)
ax.text(centroid_x, centroid_y, centroid_z, 'Centroid', fontsize=12, color='r')

# Add context and question at the top
ax.text2D(0.05, 0.95, "What are the coordinates of the centroid (center of mass) of a tetrahedron (pyramid with triangular base and 3 other triangular faces meeting at a common vertex) with vertices A(x1, y1, z1), B(x2, y2, z2), C(x3, y3, z3), and D(x4, y4, z4)?", transform=ax.transAxes, fontsize=10, verticalalignment='top')

# Save the plot as an image
plt.savefig('tetrahedron.jpg', dpi=300, bbox_inches='tight')
plt.show()

