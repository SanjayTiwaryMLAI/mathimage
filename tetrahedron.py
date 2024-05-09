import seaborn as sns
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Set the figure size and resolution
fig = plt.figure(figsize=(8, 6), dpi=300)

# Add a 3D axis
ax = fig.add_subplot(111, projection='3d')

# Set the title
question = "If the centroid of a tetrahedron (pyramid with triangular base) is (2, 3, 4), and three of its vertices are (1, 2, 3), (4, 5, 6), and (3, 1, 5), what are the coordinates of the fourth vertex?"
ax.set_title(question, fontsize=12, pad=20)

# Define the vertices of the tetrahedron
vertices = np.array([[1, 2, 3], [4, 5, 6], [3, 1, 5], [2, 3, 4]])

# Define the edges of the tetrahedron
edges = [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3]]

# Draw the edges
for edge in edges:
    ax.plot([vertices[edge[0]][0], vertices[edge[1]][0]],
            [vertices[edge[0]][1], vertices[edge[1]][1]],
            [vertices[edge[0]][2], vertices[edge[1]][2]],
            color='k')

# Label the edges
edge_labels = ['A', 'B', 'C', 'D', 'E', 'F']
for i, edge in enumerate(edges):
    x1, y1, z1 = vertices[edge[0]]
    x2, y2, z2 = vertices[edge[1]]
    x_mid, y_mid, z_mid = (x1 + x2) / 2, (y1 + y2) / 2, (z1 + z2) / 2
    ax.text(x_mid, y_mid, z_mid, edge_labels[i], ha='center', va='center')

# Set the aspect ratio and adjust the view
max_val = max(np.max(vertices[:, 0]), np.max(vertices[:, 1]), np.max(vertices[:, 2]))
ax.set_xlim([-max_val, max_val])
ax.set_ylim([-max_val, max_val])
ax.set_zlim([-max_val, max_val])
ax.view_init(elev=30, azim=-45)

# Save the plot as tetrahedron.jpg
plt.savefig('tetrahedron.jpg', bbox_inches='tight', dpi=300)

