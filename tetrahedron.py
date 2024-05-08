import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the vertices of the tetrahedron
A = np.array([1, 2, 3])
B = np.array([4, 5, 6])
C = np.array([7, 8, 9])
D = np.array([10, 11, 12])

# Create a figure and 3D axes
fig = plt.figure(figsize=(8, 6), dpi=300)
ax = fig.add_subplot(111, projection='3d')

# Plot the vertices
ax.scatter([A[0], B[0], C[0], D[0]], [A[1], B[1], C[1], D[1]], [A[2], B[2], C[2], D[2]], color='r', marker='o')

# Label the vertices
ax.text(A[0], A[1], A[2], 'A', color='k')
ax.text(B[0], B[1], B[2], 'B', color='k')
ax.text(C[0], C[1], C[2], 'C', color='k')
ax.text(D[0], D[1], D[2], 'D', color='k')

# Draw the edges of the tetrahedron
ax.plot([A[0], B[0]], [A[1], B[1]], [A[2], B[2]], color='k')
ax.plot([A[0], C[0]], [A[1], C[1]], [A[2], C[2]], color='k')
ax.plot([A[0], D[0]], [A[1], D[1]], [A[2], D[2]], color='k')
ax.plot([B[0], C[0]], [B[1], C[1]], [B[2], C[2]], color='k')
ax.plot([B[0], D[0]], [B[1], D[1]], [B[2], D[2]], color='k')
ax.plot([C[0], D[0]], [C[1], D[1]], [C[2], D[2]], color='k')

# Set the axis labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('What is the centroid (center of mass) of a tetrahedron with vertices A(1, 2, 3), B(4, 5, 6), C(7, 8, 9), and D(10, 11, 12)?')

# Adjust the view angle
ax.view_init(elev=30, azim=45)

# Save the plot as an image
plt.savefig('tetrahedron.jpg', dpi=300, bbox_inches='tight')

