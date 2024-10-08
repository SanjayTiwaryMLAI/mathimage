import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

# Set up the plot
plt.figure(figsize=(10, 8))
sns.set_style("whitegrid")

# Create the parallelogram
parallelogram = Polygon([(0, 0), (10, 0), (12, 8), (2, 8)], facecolor='lightblue', edgecolor='blue', alpha=0.7)

# Add the parallelogram to the plot
ax = plt.gca()
ax.add_patch(parallelogram)

# Set axis limits
ax.set_xlim(-1, 13)
ax.set_ylim(-1, 9)

# Remove axis ticks
ax.set_xticks([])
ax.set_yticks([])

# Add labels and annotations
plt.text(5, -0.5, '10 cm', ha='center', va='top')
plt.text(-0.5, 4, '8 cm', ha='right', va='center', rotation=90)
plt.text(11, 4, '8 cm', ha='left', va='center', rotation=90)
plt.text(6, 8.5, 'Parallelogram', ha='center', va='bottom', fontweight='bold')

# Add arrow for height
plt.arrow(10, 0, 0, 8, width=0.1, head_width=0.3, head_length=0.3, fc='red', ec='red', length_includes_head=True)

# Add formula and calculation
plt.text(13, 4, 'Area = base \u00d7 height\\n= 10 cm \u00d7 8 cm\\n= 80 cm\u00b2', ha='left', va='center', bbox=dict(facecolor='white', edgecolor='gray', alpha=0.7))

# Set title
plt.title('Area of a Parallelogram', fontsize=16, fontweight='bold')

# Save the plot as an image
plt.savefig('image.jpg', dpi=100, bbox_inches='tight')

# Show the plot (optional, for preview)
plt.show()

