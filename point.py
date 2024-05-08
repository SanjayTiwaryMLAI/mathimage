import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Set the context and question
context = "What is the 3D distance formula to find the distance between two points A(x1, y1, z1) and B(x2, y2, z2)?"

# Set the figure size and resolution
fig, ax = plt.subplots(figsize=(4, 4), dpi=300)

# Add the context to the top of the plot
ax.text(0.5, 0.95, context, ha='center', va='top', transform=ax.transAxes, fontsize=10, wrap=True)

# Set the axis limits
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_xticks([])
ax.set_yticks([])

# Draw the point
ax.scatter(0, 0, s=100, color='black', marker='o')

# Label the point
ax.text(0.1, 0.1, 'A', fontsize=12)

# Set the aspect ratio to make the point appear circular
ax.set_aspect('equal')

# Remove the axis labels and ticks
plt.axis('off')

# Save the plot as point.jpg
plt.savefig('point.jpg', bbox_inches='tight', dpi=300)

