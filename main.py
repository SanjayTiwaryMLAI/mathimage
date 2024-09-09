import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib.patches import Polygon

# Set up the plot
plt.figure(figsize=(10, 8))
sns.set_style("whitegrid")

# Create the triangle
base = 8
height = 6
triangle = Polygon([(0, 0), (base, 0), (base, height)], closed=True, facecolor='lightblue', edgecolor='blue')

# Set up the axes
ax = plt.gca()
ax.add_patch(triangle)
ax.set_xlim(-1, 10)
ax.set_ylim(-1, 8)

# Add labels and annotations
ax.text(4, -0.5, f'Base = {base} cm', ha='center', va='center', fontsize=12)
ax.text(8.5, 3, f'Height = {height} cm', ha='left', va='center', fontsize=12, rotation=90)
ax.text(4, 2, f'Area = 1/2 \u00d7 base \u00d7 height\\n= 1/2 \u00d7 {base} \u00d7 {height}\\n= {base*height/2} cm\u00b2',
        ha='center', va='center', fontsize=12, bbox=dict(facecolor='white', edgecolor='gray', alpha=0.8))

# Add arrow for height
ax.annotate('', xy=(base, height), xytext=(base, 0), arrowprops=dict(arrowstyle='<->', color='red'))

# Set title
plt.title('Triangle Area Calculation', fontsize=16, fontweight='bold')

# Remove axis ticks
ax.set_xticks([])
ax.set_yticks([])

# Save the plot
plt.savefig('image.jpg', dpi=100, bbox_inches='tight')
plt.close()

