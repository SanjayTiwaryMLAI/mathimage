import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Define the endpoints of the line segment
A = np.array([1, 2, 3])
B = np.array([4, 5, 6])

# Calculate the vector AB
AB = B - A

# Divide the line segment in the ratio 2:3
P = A + (2 / 5) * AB

# Create a 3D figure
fig = plt.figure(figsize=(6, 6), dpi=300)
ax = fig.add_subplot(111, projection='3d')

# Plot the line segment
ax.plot([A[0], B[0]], [A[1], B[1]], [A[2], B[2]], 'r-', linewidth=2)

# Label the endpoints
ax.text(A[0], A[1], A[2], 'A', fontsize=12)
ax.text(B[0], B[1], B[2], 'B', fontsize=12)
ax.text(P[0], P[1], P[2], 'P', fontsize=12)

# Set axis labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('If a point P(x, y, z) divides the line segment AB with endpoints A(1, 2, 3) and B(4, 5, 6) in the ratio 2:3 internally, what are the coordinates of P?')

# Set axis limits
ax.set_xlim(0, 5)
ax.set_ylim(0, 6)
ax.set_zlim(0, 7)

# Save the plot
plt.savefig('line.jpg', dpi=300, bbox_inches='tight')
plt.show()

