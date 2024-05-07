import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont

# Define the coordinates of points A and B
x1, y1, z1 = 0, 0, 0  # A(x1, y1, z1)
x2, y2, z2 = 4, 3, 2  # B(x2, y2, z2)

# Define the ratios m1 and m2
m1, m2 = 2, 3

# Calculate the coordinates of point R
x_R = (m1 * x2 + m2 * x1) / (m1 + m2)
y_R = (m1 * y2 + m2 * y1) / (m1 + m2)
z_R = (m1 * z2 + m2 * z1) / (m1 + m2)

# Create a figure and axis
fig, ax = plt.subplots(figsize=(8, 6))

# Plot the line segment AB
ax.plot([x1, x2], [y1, y2], [z1, z2], 'r-', linewidth=2)

# Plot the points A, B, and R
ax.scatter(x1, y1, z1, color='b', marker='o', label='A')
ax.scatter(x2, y2, z2, color='b', marker='o', label='B')
ax.scatter(x_R, y_R, z_R, color='g', marker='o', label='R')

# Add labels to the points
ax.text(x1 + 0.1, y1 + 0.1, z1 + 0.1, 'A', fontsize=12)
ax.text(x2 + 0.1, y2 + 0.1, z2 + 0.1, 'B', fontsize=12)
ax.text(x_R + 0.1, y_R + 0.1, z_R + 0.1, 'R', fontsize=12)

# Set axis labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('If a point R divides the line segment AB internally in the ratio m1:m2,\nwhere A(x1, y1, z1) and B(x2, y2, z2), what are the coordinates of R?')

# Add a legend
ax.legend()

# Adjust the view angle
ax.view_init(elev=30, azim=-45)

# Save the plot as an image
plt.savefig('line.jpg', dpi=300, bbox_inches='tight')

# Open the image and add the context at the top
img = Image.open('line.jpg')
draw = ImageDraw.Draw(img)
font = ImageFont.truetype('arial.ttf', 16)
context = "If a point R divides the line segment AB internally in the ratio m1:m2, where A(x1, y1, z1) and B(x2, y2, z2), what are the coordinates of R?"
draw.text((10, 10), context, font=font, fill=(0, 0, 0))
img.save('line.jpg')

