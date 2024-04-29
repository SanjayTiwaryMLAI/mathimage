import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Define the vertex positions
A = np.array([1, 2, 3])  # αi + βj + γk
B = np.array([2, 3, 1])  # βi + γj + αk
C = np.array([3, 1, 2])  # γi + αj + βk

# Create a figure and axis
fig, ax = plt.subplots(figsize=(6, 6))

# Draw the triangle
ax.plot([A[0], B[0]], [A[1], B[1]], color='r', label='A-B')
ax.plot([B[0], C[0]], [B[1], C[1]], color='r', label='B-C')
ax.plot([C[0], A[0]], [C[1], A[1]], color='r', label='C-A')

# Label the vertices
ax.text(A[0], A[1], 'A', fontsize=12, ha='center', va='bottom')
ax.text(B[0], B[1], 'B', fontsize=12, ha='center', va='bottom')
ax.text(C[0], C[1], 'C', fontsize=12, ha='center', va='bottom')

# Set axis limits and aspect ratio
ax.set_xlim(min(A[0], B[0], C[0]) - 1, max(A[0], B[0], C[0]) + 1)
ax.set_ylim(min(A[1], B[1], C[1]) - 1, max(A[1], B[1], C[1]) + 1)
ax.set_aspect('equal')

# Add the context/question at the top
question = "If the position vectors of the vertices A, B, and C of a triangle \u25b3ABC are \u03b1i+\u03b2j+\u03b3k, \u03b2i+\u03b3j+\u03b1k, and \u03b3i+\u03b1j+\u03b2k respectively, then \u25b3ABC is"
ax.text(0.5, 1.05, question, transform=ax.transAxes, ha='center', va='bottom', fontsize=10, wrap=True)

# Save the plot as triangle.jpg
plt.savefig('triangle.jpg', dpi=300, bbox_inches='tight')
plt.show()

