import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D

# Set seaborn style
sns.set(style="whitegrid")

# Create figure and 3D axis
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Define vertices
A = np.array([1, 2, 3])
B = np.array([2, 3, 1])
C = np.array([3, 1, 2])

# Plot vertices
ax.scatter(A[0], A[1], A[2], c='r', s=100, label='A (α, β, γ)')
ax.scatter(B[0], B[1], B[2], c='g', s=100, label='B (β, γ, α)')
ax.scatter(C[0], C[1], C[2], c='b', s=100, label='C (γ, α, β)')

# Plot edges
ax.plot([A[0], B[0]], [A[1], B[1]], [A[2], B[2]], 'k-', linewidth=2)
ax.plot([B[0], C[0]], [B[1], C[1]], [B[2], C[2]], 'k-', linewidth=2)
ax.plot([C[0], A[0]], [C[1], A[1]], [C[2], A[2]], 'k-', linewidth=2)

# Label vertices
ax.text(A[0], A[1], A[2], 'A', fontsize=12)
ax.text(B[0], B[1], B[2], 'B', fontsize=12)
ax.text(C[0], C[1], C[2], 'C', fontsize=12)

# Set axis labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Set title
ax.set_title('Triangle ABC with Position Vectors\nA(αi+βj+γk), B(βi+γj+αk), C(γi+αj+βk)', fontsize=14)

# Add legend
ax.legend()

# Adjust plot to fit 80% of the area
plt.tight_layout(rect=[0, 0, 0.8, 0.8])

# Save the figure
plt.savefig('image.jpg', dpi=100, bbox_inches='tight')

# Show the plot (optional)
plt.show()

