import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Set the figure size
fig, ax = plt.subplots(figsize=(5, 5))

# Set the context/question at the top
ax.set_title("What condition must be satisfied for three points A, B, and C\nto be collinear (lie on the same line) in 3D space?", fontsize=12)

# Define the points A, B, and C
A = np.array([0, 0, 0])
B = np.array([2, 2, 2])
C = np.array([4, 4, 4])

# Draw the line connecting A, B, and C
ax.plot([A[0], B[0], C[0]], [A[1], B[1], C[1]], [A[2], B[2], C[2]], 'r-', linewidth=2)

# Label the points
ax.text(A[0], A[1], A[2], 'A', fontsize=12)
ax.text(B[0], B[1], B[2], 'B', fontsize=12)
ax.text(C[0], C[1], C[2], 'C', fontsize=12)

# Set the aspect ratio to make the plot look like a cube
ax.set_box_aspect((1, 1, 1))

# Set the axis labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Save the plot as line.jpg
plt.savefig('line.jpg', dpi=300, bbox_inches='tight')

