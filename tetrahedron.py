import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns

# Define the vertices of the tetrahedron
A = np.array([0, 0, 0])
B = np.array([1, 0, 0])
C = np.array([0, 1, 0])
D = np.array([0, 0, 1])

# Create a 3D figure
fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111, projection='3d')

# Plot the tetrahedron
r = [-1, 1]
X, Y = np.meshgrid(r, r)
Z = np.zeros_like(X)

# Plot the base triangle (ABC)
ax.plot_surface(X, Y, Z, alpha=0.5, color='b')

# Plot the side triangles (ABD, ACD, BCD)
ax.plot_surface(X, Z, Y, alpha=0.5, color='r')
ax.plot_surface(Z, X, Y, alpha=0.5, color='g')
ax.plot_surface(X, Z, -Y, alpha=0.5, color='y')

# Label the vertices
ax.text(A[0], A[1], A[2], 'A', fontsize=12)
ax.text(B[0], B[1], B[2], 'B', fontsize=12)
ax.text(C[0], C[1], C[2], 'C', fontsize=12)
ax.text(D[0], D[1], D[2], 'D', fontsize=12)

# Set axis labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Tetrahedron')

# Calculate and display the centroid
centroid = np.mean([A, B, C, D], axis=0)
ax.text(centroid[0], centroid[1], centroid[2], 'Centroid', fontsize=12, color='k')

# Save the plot as an image
plt.savefig('tetrahedron.jpg', dpi=300, bbox_inches='tight')
plt.show()

