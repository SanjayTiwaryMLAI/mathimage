import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set the figure size and resolution
fig, ax = plt.subplots(figsize=(8, 6), dpi=300)

# Create the hexagon coordinates
theta = np.linspace(0, 2 * np.pi, 7)[:-1]
x = np.cos(theta)
y = np.sin(theta)

# Plot the hexagon
ax.fill(x, y, color='lightblue', edgecolor='black', linewidth=2, zorder=2)

# Add the question or problem statement at the top
ax.text(0, 1.1, "ABCDEF is a hexagon (six-sided polygon). Find the value of AB+BC+CD+DE+AF+FE+AE?",
        ha='center', va='bottom', fontsize=12, transform=ax.transAxes)

# Label the vertices
vertices = ['A', 'B', 'C', 'D', 'E', 'F']
for i, (x, y) in enumerate(zip(x, y)):
    ax.text(x, y, vertices[i], ha='center', va='center', fontsize=12)

# Label the edges
edges = ['AB', 'BC', 'CD', 'DE', 'EF', 'FA']
for i, (x1, y1, x2, y2) in enumerate(zip(x, y, np.roll(x, -1), np.roll(y, -1))):
    ax.text((x1 + x2) / 2, (y1 + y2) / 2, edges[i], ha='center', va='center', fontsize=10)

# Set the aspect ratio and remove axis ticks
ax.set_aspect('equal')
ax.set_xticks([])
ax.set_yticks([])

# Adjust the plot area to cover approximately 80% of the image
plt.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.9)

# Save the image as hexagon.jpg with 300 dpi resolution
plt.savefig('hexagon.jpg', dpi=300, bbox_inches='tight')

