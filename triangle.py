import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Set the figure size and DPI
fig, ax = plt.subplots(figsize=(8, 6), dpi=300)

# Add the context/question at the top
ax.set_title("If the position vectors of the vertices A, B, and C of a triangle \u25b3ABC are \n"
             "\u03b1i+\u03b2j+\u03b3k, \u03b2i+\u03b3j+\u03b1k, and \u03b3i+\u03b1j+\u03b2k respectively, then \u25b3ABC is ?",
             fontsize=12, wrap=True)

# Set the plot style
sns.set_style("whitegrid")

# Define the vertices of the triangle
A = np.array([0, 0])
B = np.array([4, 0])
C = np.array([2, 3])

# Draw the triangle
ax.plot([A[0], B[0]], [A[1], B[1]], 'k-', label='A-B')
ax.plot([B[0], C[0]], [B[1], C[1]], 'k-', label='B-C')
ax.plot([C[0], A[0]], [C[1], A[1]], 'k-', label='C-A')

# Label the vertices
ax.text(A[0] - 0.2, A[1] - 0.2, 'A', fontsize=12)
ax.text(B[0] + 0.2, B[1] - 0.2, 'B', fontsize=12)
ax.text(C[0], C[1] + 0.2, 'C', fontsize=12)

# Add a legend
ax.legend(loc='upper left', fontsize=10)

# Remove the x and y ticks
ax.set_xticks([])
ax.set_yticks([])

# Save the plot
plt.savefig('triangle.jpg', bbox_inches='tight', dpi=300)

