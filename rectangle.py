import seaborn as sns
import matplotlib.pyplot as plt

# Set the figure size and DPI
fig, ax = plt.subplots(figsize=(8, 6), dpi=300)

# Add the context/question at the top
ax.set_title("What is the area of a rectangle?", fontsize=16, pad=20)

# Draw the rectangle
rect = plt.Rectangle((0.1, 0.1), 0.8, 0.6, facecolor='lightblue', edgecolor='black')
ax.add_patch(rect)

# Label the edges
ax.text(0.05, 0.6, 'A', fontsize=12, ha='center', va='center')
ax.text(0.9, 0.6, 'B', fontsize=12, ha='center', va='center')
ax.text(0.05, 0.1, 'C', fontsize=12, ha='center', va='center')
ax.text(0.9, 0.1, 'D', fontsize=12, ha='center', va='center')

# Remove axis ticks and spines
ax.set_xticks([])
ax.set_yticks([])
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

# Adjust the plot layout
plt.tight_layout()

# Save the plot as a JPEG file
plt.savefig('rectangle.jpg', dpi=300, bbox_inches='tight')

