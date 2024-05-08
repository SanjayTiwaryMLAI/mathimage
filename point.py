import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Define the points A and B
x1, y1, z1 = 1, 2, 3  # Point A
x2, y2, z2 = 4, 5, 6  # Point B

# Create a 3D figure
fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111, projection='3d')

# Plot the points
ax.scatter(x1, y1, z1, color='r', label='A')
ax.scatter(x2, y2, z2, color='g', label='B')

# Label the axes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Set the plot limits
ax.set_xlim(0, 6)
ax.set_ylim(0, 7)
ax.set_zlim(0, 8)

# Add a title
ax.set_title('Distance Formula for 3D Points')

# Add context at the top
context = "The distance formula for finding the distance between two points A(x1, y1, z1) and B(x2, y2, z2) in 3D coordinate geometry is:"
fig.suptitle(context, fontsize=12, y=0.95)

# Add labels for the points
ax.text(x1, y1, z1, 'A', color='r')
ax.text(x2, y2, z2, 'B', color='g')

# Calculate and display the distance
distance = np.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
ax.text(3, 3, 7, f'Distance = {distance:.2f}', fontsize=12)

# Show the legend
ax.legend()

# Save the plot as an image
plt.savefig('point.jpg', dpi=100, bbox_inches='tight')

