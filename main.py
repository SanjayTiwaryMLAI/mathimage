import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Define the vertices of the tetrahedron
A = np.array([0, 0, 0])
B = np.array([1, 0, 0])
C = np.array([0.5, np.sqrt(3)/2, 0])
D = np.array([0.5, 1/(2*np.sqrt(3)), np.sqrt(2/3)])

# Define the edges of the tetrahedron
edges = [
    [A, B],
    [B, C],
    [C, A],
    [A, D],
    [B, D],
    [C, D]
]

# Create a 3D figure
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Plot the edges of the tetrahedron
for edge in edges:
    ax.plot([edge[0][0], edge[1][0]], [edge[0][1], edge[1][1]], [edge[0][2], edge[1][2]], 'k-')

# Label the vertices
ax.text(A[0], A[1], A[2], 'A', fontsize=12)
ax.text(B[0], B[1], B[2], 'B', fontsize=12)
ax.text(C[0], C[1], C[2], 'C', fontsize=12)
ax.text(D[0], D[1], D[2], 'D', fontsize=12)

# Set the aspect ratio and limits
ax.set_box_aspect((1, 1, 1))
ax.set_xlim([-0.5, 1.5])
ax.set_ylim([-0.5, 1.5])
ax.set_zlim([-0.5, 1.5])

# Add labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Tetrahedron')

# Add context and question at the top
context = "What is the formula to find the coordinates of the centroid (center of mass) of a tetrahedron (pyramid with triangular base and 3 other triangular faces meeting at a common vertex) with vertices A(x1, y1, z1), B(x2, y2, z2), C(x3, y3, z3), and D(x4, y4, z4)?"
plt.figtext(0.5, 0.95, context, ha='center', fontsize=12, bbox={'facecolor': 'gray', 'alpha': 0.5, 'pad': 5})

# Save the plot as an image
plt.savefig('tetrahedron.jpg', dpi=300, bbox_inches='tight')

