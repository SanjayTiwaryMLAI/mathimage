import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set the context
context = "If the adjacent sides of a parallelogram are 3i+2j and -i+4j+2k, find the area of the parallelogram."

# Create a figure and axis
fig, ax = plt.subplots(figsize=(8, 6))

# Draw the parallelogram
x = [0, 3, 2, -1]
y = [0, 2, 6, 4]
ax.plot(x, y, marker='o', markersize=10, color='black')
ax.plot([x[0], x[-1]], [y[0], y[-1]], color='black')  # Complete the last edge

# Label the edges (optional)
ax.text(1.5, 1, 'A', fontsize=12, ha='center', va='center')
ax.text(2.5, 4, 'B', fontsize=12, ha='center', va='center')
ax.text(0.5, 5, 'C', fontsize=12, ha='center', va='center')
ax.text(-0.5, 2, 'D', fontsize=12, ha='center', va='center')

# Add context at the top
ax.text(0, 1.05, context, transform=ax.transAxes, fontsize=12, ha='left', va='top')

# Set axis limits and remove ticks
ax.set_xlim([-2, 4])
ax.set_ylim([-1, 7])
ax.set_xticks([])
ax.set_yticks([])

# Save the plot as a JPG image
plt.savefig('parallelogram.jpg', dpi=300, bbox_inches='tight')

# Show the plot
plt.show()

