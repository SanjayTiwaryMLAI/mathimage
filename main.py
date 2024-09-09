import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set up the plot
plt.figure(figsize=(10, 8))
sns.set_style("whitegrid")

# Create the parallelogram
x = [0, 4, 5, 1]
y = [0, 0, 3, 3]

# Plot the parallelogram
plt.fill(x, y, alpha=0.3, color='skyblue')
plt.plot(x + [x[0]], y + [y[0]], color='navy')

# Add height line
plt.plot([0, 1], [0, 3], color='red', linestyle='--', linewidth=2)

# Add labels and annotations
plt.text(2, -0.5, 'base (b)', fontsize=12, ha='center')
plt.text(-0.3, 1.5, 'height (h)', fontsize=12, va='center', rotation=90)
plt.text(2.5, 1.5, 'Area = b \u00d7 h', fontsize=14, ha='center', bbox=dict(facecolor='white', edgecolor='gray', alpha=0.8))

# Add arrow for height
plt.annotate('', xy=(1, 3), xytext=(0, 0), arrowprops=dict(arrowstyle='<->', color='red'))

# Set axis limits and labels
plt.xlim(-0.5, 5.5)
plt.ylim(-1, 4)
plt.xlabel('Base', fontsize=12)
plt.ylabel('Height', fontsize=12)

# Set title
plt.title('Area of a Parallelogram', fontsize=16, fontweight='bold')

# Remove top and right spines
sns.despine()

# Adjust layout and save the image
plt.tight_layout()
plt.savefig('image.jpg', dpi=100, bbox_inches='tight')
plt.close()

