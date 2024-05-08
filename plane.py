import matplotlib.pyplot as plt
import seaborn as sns

# Set the figure size and DPI
fig, ax = plt.subplots(figsize=(6, 4), dpi=300)

# Add the question at the top
ax.text(0.5, 0.95, "What are the coordinates used to represent points in 3D space?", transform=ax.transAxes, ha="center", va="top", fontsize=12)

# Create a 3D plane
x = [-1, 1, 1, -1, -1]
y = [-1, -1, 1, 1, -1]
z = [0, 0, 0, 0, 0]

# Plot the plane
ax.plot(x, y, z, color='black', linewidth=2)

# Label the edges
ax.text(-1.1, -1.1, 0, 'A', fontsize=10)
ax.text(1.1, -1.1, 0, 'B', fontsize=10)
ax.text(1.1, 1.1, 0, 'C', fontsize=10)
ax.text(-1.1, 1.1, 0, 'D', fontsize=10)

# Remove axis ticks and labels
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])

# Set the aspect ratio to equal
ax.set_box_aspect((1, 1, 1))

# Adjust the plot limits
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_zlim(-0.5, 0.5)

# Set the view angle
ax.view_init(elev=30, azim=-45)

# Save the plot as plane.jpg
plt.savefig("plane.jpg", dpi=300, bbox_inches="tight")

