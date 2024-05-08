import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Define the coordinates of points A and B
A = np.array([1, 2, 3])
B = np.array([7, 8, 9])

# Calculate the coordinates of point R
AB = B - A
R = A + (2 / 5) * AB

# Set up the figure and axes
fig, ax = plt.subplots(figsize=(5, 5), dpi=300)

# Plot the line segment AB
ax.plot([A[0], B[0]], [A[1], B[1]], [A[2], B[2]], 'k-', linewidth=2)

# Label the points
ax.text(A[0], A[1], A[2], 'A', fontsize=12)
ax.text(B[0], B[1], B[2], 'B', fontsize=12)
ax.text(R[0], R[1], R[2], 'R', fontsize=12)

# Set axis labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('If the point R divides the line segment AB internally in the ratio 2:3,\nand A(1, 2, 3) and B(7, 8, 9), what are the coordinates of R?', fontsize=12)

# Set axis limits
ax.set_xlim(0, 8)
ax.set_ylim(0, 10)
ax.set_zlim(0, 10)

# Save the plot as line.jpg
plt.savefig('line.jpg', dpi=300, bbox_inches='tight')

