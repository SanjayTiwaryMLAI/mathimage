import matplotlib.pyplot as plt
import seaborn as sns

# Set the figure size
plt.figure(figsize=(6, 6))

# Create a blank canvas
ax = plt.subplot(111)

# Set the context/question at the top
question = "If the incentre of a triangle with vertices A(2, 3, 4), B(4, 5, 6), and C(6, 7, 8) is (3, 4, 5), what is the value of the ratio (a + b - c)/a, where a, b, and c are the sides of the triangle?"
plt.text(0, 1.05, question, ha='left', va='bottom', transform=ax.transAxes, fontsize=12, wrap=True)

# Define the coordinates of the triangle vertices
A = (2, 3)
B = (4, 5)
C = (6, 7)

# Draw the triangle
plt.plot([A[0], B[0]], [A[1], B[1]], '-', color='black', label='A-B')
plt.plot([B[0], C[0]], [B[1], C[1]], '-', color='black', label='B-C')
plt.plot([C[0], A[0]], [C[1], A[1]], '-', color='black', label='C-A')

# Label the edges
plt.text((A[0] + B[0]) / 2, (A[1] + B[1]) / 2, 'A', ha='center', va='center', fontsize=12)
plt.text((B[0] + C[0]) / 2, (B[1] + C[1]) / 2, 'B', ha='center', va='center', fontsize=12)
plt.text((C[0] + A[0]) / 2, (C[1] + A[1]) / 2, 'C', ha='center', va='center', fontsize=12)

# Set the axis limits and remove ticks
plt.xlim(0, 8)
plt.ylim(0, 8)
plt.xticks([])
plt.yticks([])

# Save the plot as triangle.jpg
plt.savefig('triangle.jpg', dpi=100, bbox_inches='tight')

# Show the plot
plt.show()

