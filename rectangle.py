import matplotlib.pyplot as plt
import seaborn as sns

# Set the context and style
sns.set_context("notebook", font_scale=1.5, rc={"lines.linewidth": 2.5})
sns.set_style("whitegrid")

# Create a figure with fixed size and resolution
fig, ax = plt.subplots(figsize=(8, 6), dpi=300)

# Add the question at the top
ax.text(0.5, 0.9, "What is the area of a rectangle?", ha="center", va="center", transform=ax.transAxes, fontsize=16)

# Draw the rectangle
rect = plt.Rectangle((0.2, 0.2), 0.6, 0.4, facecolor="none", edgecolor="black", linewidth=2)
ax.add_patch(rect)

# Label the edges
ax.text(0.1, 0.5, "A", ha="center", va="center", fontsize=14)
ax.text(0.9, 0.5, "B", ha="center", va="center", fontsize=14)
ax.text(0.5, 0.1, "C", ha="center", va="center", fontsize=14)
ax.text(0.5, 0.9, "D", ha="center", va="center", fontsize=14)

# Remove axis ticks and labels
ax.set_xticks([])
ax.set_yticks([])

# Save the plot
plt.savefig("rectangle.jpg", bbox_inches="tight", dpi=300)

