import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Define the vertices of the triangle
A = np.array([1, 2, 3])
B = np.array([4, 5, 6])
C = np.array([7, 8, 9])

# Calculate the centroid (center of mass) of the triangle
centroid = (A + B + C) / 3

# Create a figure and axis
fig, ax = plt.subplots(figsize=(6, 4), dpi=300)

# Set the title and context
ax.set_title("What are the coordinates of the centroid (center of mass)\nof a triangle with vertices A(1, 2, 3), B(4, 5, 6), and C(7, 8, 9)?", fontsize=12)

# Draw the triangle
triangle = plt.Polygon([A[:2], B[:2], C[:2]], fill=False, edgecolor='k', linewidth=2)
ax.add_patch(triangle)

# Label the vertices
ax.text(A[0], A[1], 'A', fontsize=10, ha='center', va='bottom')
ax.text(B[0], B[1], 'B', fontsize=10, ha='center', va='bottom')
ax.text(C[0], C[1], 'C', fontsize=10, ha='center', va='bottom')

# Plot the centroid
ax.scatter(centroid[0], centroid[1], color='r', marker='o', s=50)
ax.text(centroid[0], centroid[1], 'Centroid', fontsize=10, ha='center', va='bottom')

# Set the aspect ratio and limits
ax.set_aspect('equal')
ax.autoscale_view()

# Remove the axes ticks and spines
ax.set_xticks([])
ax.set_yticks([])
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

# Save the plot as an image
plt.savefig('triangle.jpg', dpi=300, bbox_inches='tight')
plt.show()

