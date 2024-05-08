import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Set the context and question
context = "What is the area of a rectangle?"

# Set the dimensions of the rectangle
length = 10
width = 6

# Set the figure size and DPI
fig, ax = plt.subplots(figsize=(4, 3), dpi=300)

# Draw the rectangle
rect = plt.Rectangle((0, 0), length, width, edgecolor='black', facecolor='lightgray', linewidth=2)
ax.add_patch(rect)

# Label the edges
ax.text(length/2, -0.5, 'A', ha='center', va='top', fontsize=12)
ax.text(length+0.5, width/2, 'B', ha='left', va='center', fontsize=12)
ax.text(length/2, width+0.5, 'C', ha='center', va='bottom', fontsize=12)
ax.text(-0.5, width/2, 'D', ha='right', va='center', fontsize=12)

# Set the axis limits and remove ticks
ax.set_xlim([-1, length+1])
ax.set_ylim([-1, width+1])
ax.set_xticks([])
ax.set_yticks([])

# Add the context and question at the top
ax.text(0.5, 1.1, context, ha='center', va='bottom', transform=ax.transAxes, fontsize=14, fontweight='bold')

# Set the background color
fig.patch.set_facecolor('white')

# Save the plot as rectangle.jpg
plt.savefig('rectangle.jpg', bbox_inches='tight', dpi=300)

