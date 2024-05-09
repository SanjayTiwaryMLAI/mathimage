import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Set the context/question at the top
question = "What are the coordinates of the centroid (center of mass) of the triangle with vertices (1, 2, 3), (-2, 4, 1), and (3, -1, 5)?"

# Set the figure size and resolution
fig, ax = plt.subplots(figsize=(8, 6), dpi=300)

# Draw the triangle
x = [1, -2, 3]
y = [2, 4, -1]
ax.fill(x, y, alpha=0.5, edgecolor='black', linewidth=2)

# Label the edges
ax.annotate('A', xy=(1, 2), xytext=(1.2, 2.2), fontsize=12)
ax.annotate('B', xy=(-2, 4), xytext=(-2.2, 4.2), fontsize=12)
ax.annotate('C', xy=(3, -1), xytext=(3.2, -0.8), fontsize=12)

# Set the axis limits to cover 80% of the area
ax.set_xlim(-3, 4)
ax.set_ylim(-2, 5)

# Add the question at the top
ax.text(0.5, 0.95, question, transform=ax.transAxes, fontsize=12, ha='center', va='top')

# Remove the axis ticks and spines
ax.set_xticks([])
ax.set_yticks([])
sns.despine(ax=ax, left=True, bottom=True)

# Save the plot as triangle.jpg
plt.savefig('triangle.jpg', bbox_inches='tight', dpi=300)

