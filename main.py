import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Set the figure size and resolution
fig, ax = plt.subplots(figsize=(8, 6), dpi=100)

# Create a rectangular shape with rounded corners
rect = patches.Rectangle((0.1, 0.1), 0.8, 0.8, linewidth=2, edgecolor='black', facecolor='lightgray', zorder=1, radius=0.1)
ax.add_patch(rect)

# Add text inside the rectangle
text = "प्रश्न 27: इंदिरा गांधी सरकार द्वारा 25 जून 1975 को भारत में आपातकाल घोषित करने का क्या कारण था?"
ax.text(0.2, 0.6, text, fontsize=14, wrap=True, zorder=2)

# Add annotations for edges and corners
ax.annotate('Edge', xy=(0.05, 0.5), xytext=(0.05, 0.4), arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10)
ax.annotate('Corner', xy=(0.85, 0.85), xytext=(0.7, 0.7), arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10)

# Remove axis ticks and spines
ax.set_xticks([])
ax.set_yticks([])
sns.despine(ax=ax, left=True, bottom=True)

# Add a title
ax.set_title("Mathematical Concept Representation", fontsize=16, fontweight='bold')

# Save the figure
plt.savefig("image.jpg", dpi=100, bbox_inches='tight')

