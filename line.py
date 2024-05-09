import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(8, 6))

# Define the question or problem statement
question = "If three points A(x1, y1, z1), B(x2, y2, z2), and C(x3, y3, z3) are collinear, which of the following conditions must be satisfied?"

# Define the condition
condition = r"$\frac{x_2 - x_1}{x_3 - x_1} = \frac{y_2 - y_1}{y_3 - y_1} = \frac{z_2 - z_1}{z_3 - z_1}$"

# Define the points
A = np.array([1, 1, 1])
B = np.array([3, 3, 3])
C = np.array([5, 5, 5])

# Plot the points
ax.scatter(A[0], A[1], c='r', s=100, label='A')
ax.scatter(B[0], B[1], c='g', s=100, label='B')
ax.scatter(C[0], C[1], c='b', s=100, label='C')

# Plot the line connecting the points
ax.plot([A[0], B[0], C[0]], [A[1], B[1], C[1]], 'k--', linewidth=2)

# Add labels and annotations
ax.text(A[0] - 0.2, A[1] - 0.2, f'A({A[0]}, {A[1]}, {A[2]})', fontsize=12)
ax.text(B[0] - 0.2, B[1] - 0.2, f'B({B[0]}, {B[1]}, {B[2]})', fontsize=12)
ax.text(C[0] - 0.2, C[1] - 0.2, f'C({C[0]}, {C[1]}, {C[2]})', fontsize=12)

# Add the question and condition
ax.text(0.5, 0.9, question, ha='center', va='center', transform=ax.transAxes, fontsize=14, wrap=True)
ax.text(0.5, 0.8, condition, ha='center', va='center', transform=ax.transAxes, fontsize=16)

# Set axis limits and labels
ax.set_xlim(0, 6)
ax.set_ylim(0, 6)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.legend()

# Adjust spacing and save the figure
plt.tight_layout()
plt.savefig('line.jpg', dpi=300, bbox_inches='tight')

