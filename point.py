import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Set the figure size and resolution
fig = plt.figure(figsize=(8, 6), dpi=300)

# Add the question or problem statement at the top of the image
fig.suptitle("What are the three coordinates used to represent a point in 3D coordinate geometry?", fontsize=14, y=0.95)

# Create a 3D plot
ax = fig.add_subplot(111, projection='3d')

# Define the coordinate axes
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.zeros_like(X)

# Plot the coordinate planes
ax.plot_surface(X, Y, Z, alpha=0.2, color='gray')
ax.plot_surface(X, Z, Y, alpha=0.2, color='gray')
ax.plot_surface(Z, X, Y, alpha=0.2, color='gray')

# Define a point in 3D space
x0, y0, z0 = 2, -3, 4

# Plot the point
ax.scatter(x0, y0, z0, s=100, color='r', label='Point (x, y, z)')

# Label the axes
ax.set_xlabel('X', fontsize=12)
ax.set_ylabel('Y', fontsize=12)
ax.set_zlabel('Z', fontsize=12)

# Set axis limits
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_zlim(-5, 5)

# Add annotations for the point coordinates
ax.text(x0 + 0.2, y0, z0, f'({x0}, {y0}, {z0})', fontsize=12)

# Add a legend
ax.legend()

# Adjust the spacing and alignment
plt.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.85)

# Save the image
plt.savefig('point.jpg', dpi=300, bbox_inches='tight')

