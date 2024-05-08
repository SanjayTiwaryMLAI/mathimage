import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Define the vertices of the tetrahedron
A = np.array([1, 2, 3])
B = np.array([4, 5, 6])
C = np.array([7, 8, 9])
D = np.array([10, 11, 12])

# Calculate the centroid of the tetrahedron
centroid = (A + B + C + D) / 4

# Create a 3D figure and axis
fig = plt.figure(figsize=(5, 5), dpi=300)
ax = fig.add_subplot(111, projection='3d')

# Plot the vertices and edges of the tetrahedron
ax.scatter(A[0], A[1], A[2], c='r', marker='o', label='A')
ax.scatter(B[0], B[1], B[2], c='g', marker='o', label='B')
ax.scatter(C[0], C[1], C[2], c='b', marker='o', label='C')
ax.scatter(D[0], D[1], D[2], c='y', marker='o', label='D')

ax.plot([A[0], B[0]], [A[1], B[1]], [A[2], B[2]], 'k-')
ax.plot([B[0], C[0]], [B[1], C[1]], [B[2], C[2]], 'k-')
ax.plot([C[0], D[0]], [C[1], D[1]], [C[2], D[2]], 'k-')
ax.plot([D[0], A[0]], [D[1], A[1]], [D[2], A[2]], 'k-')
ax.plot([A[0], C[0]], [A[1], C[1]], [A[2], C[2]], 'k-')
ax.plot([B[0], D[0]], [B[1], D[1]], [B[2], D[2]], 'k-')

# Label the vertices
ax.text(A[0], A[1], A[2], 'A', color='r')
ax.text(B[0], B[1], B[2], 'B', color='g')
ax.text(C[0], C[1], C[2], 'C', color='b')
ax.text(D[0], D[1], D[2], 'D', color='y')

# Add context and centroid information
ax.set_title('If the vertices of a tetrahedron are A(1, 2, 3), B(4, 5, 6), C(7, 8, 9), and D(10, 11, 12), \nwhat are the coordinates of its centroid?', fontsize=10)
ax.text(centroid[0], centroid[1], centroid[2], f'Centroid: ({centroid[0]:.2f}, {centroid[1]:.2f}, {centroid[2]:.2f})', color='k')

# Set aspect ratio and labels
ax.set_box_aspect((1, 1, 1))
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Add legend
ax.legend()

# Save the plot as a JPEG image
plt.savefig('tetrahedron.jpg', dpi=300, bbox_inches='tight')

