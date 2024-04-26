import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Set the context
context = "If the position vectors of the vertices A, B, and C of a triangle △ABC are αi+βj+γk, βi+γj+αk, and γi+αj+βk respectively, then △ABC is"

# Set up the figure
fig, ax = plt.subplots(figsize=(8, 6))

# Draw the triangle
x = np.array([0, 2, 1])
y = np.array([0, 0, 2])
ax.plot(x, y, linewidth=2, color='black')
ax.fill(x, y, alpha=0.2, color='gray')

# Label the vertices
ax.text(0, 0, 'A', fontsize=12, ha='right', va='bottom')
ax.text(2, 0, 'B', fontsize=12, ha='left', va='bottom')
ax.text(1, 2, 'C', fontsize=12, ha='center', va='top')

# Add the context
ax.text(0.5, 0.95, context, ha='center', va='top', transform=ax.transAxes, fontsize=12, wrap=True)

# Remove axis ticks and spines
ax.set_xticks([])
ax.set_yticks([])
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

# Set aspect ratio and adjust limits
ax.set_aspect('equal', adjustable='box')
ax.set_xlim([-0.5, 2.5])
ax.set_ylim([-0.5, 2.5])

# Save the plot as a JPG image
plt.savefig('triangle.jpg', dpi=300, bbox_inches='tight')

