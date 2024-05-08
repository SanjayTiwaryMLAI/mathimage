import matplotlib.pyplot as plt
import numpy as np

# Define the position vectors of the vertices
a = np.array([1, 1, 1])  # α, β, γ
b = np.array([1, 2, 3])  # β, γ, α
c = np.array([3, 1, 2])  # γ, α, β

# Create a figure and axis
fig, ax = plt.subplots(figsize=(5, 5))

# Plot the vertices and label them
ax.scatter(a[0], a[1], marker='o', label='A')
ax.scatter(b[0], b[1], marker='o', label='B')
ax.scatter(c[0], c[1], marker='o', label='C')

# Connect the vertices to form the triangle
ax.plot([a[0], b[0]], [a[1], b[1]], 'k-')
ax.plot([b[0], c[0]], [b[1], c[1]], 'k-')
ax.plot([c[0], a[0]], [c[1], a[1]], 'k-')

# Add labels to the edges
ax.text((a[0] + b[0]) / 2, (a[1] + b[1]) / 2, 'AB', ha='center', va='center')
ax.text((b[0] + c[0]) / 2, (b[1] + c[1]) / 2, 'BC', ha='center', va='center')
ax.text((c[0] + a[0]) / 2, (c[1] + a[1]) / 2, 'AC', ha='center', va='center')

# Add the context/question at the top
ax.text(0.5, 1.05, "If the position vectors of the vertices A, B, and C of a triangle ΔABC are αi+βj+γk, βi+γj+αk, and γi+αj+βk respectively, then ΔABC is?", ha='center', va='bottom', transform=ax.transAxes)

# Set aspect ratio and axis limits
ax.set_aspect('equal')
ax.set_xlim([-1, 4])
ax.set_ylim([-1, 4])

# Show the legend
ax.legend()

# Save the plot as an image
plt.savefig('triangle.jpg', dpi=300, bbox_inches='tight')

