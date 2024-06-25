import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set the figure size and resolution
fig, ax = plt.subplots(figsize=(8, 8), dpi=100)

# Define the coordinates for the benzene ring
theta = np.linspace(0, 2 * np.pi, 7)[:-1]
x = np.cos(theta)
y = np.sin(theta)

# Plot the benzene ring
ax.plot(x, y, linewidth=2, color='black')

# Add the carbon atoms
ax.scatter(x, y, s=200, color='black', zorder=3)

# Add the hydrogen atoms
for i in range(len(x)):
    ax.scatter(x[i] + 0.2 * np.cos(theta[i]), y[i] + 0.2 * np.sin(theta[i]), s=50, color='white', edgecolors='black',
               zorder=3)

# Label the carbon atoms
for i, (cx, cy) in enumerate(zip(x, y), start=1):
    ax.annotate(f'C{i}', (cx + 0.1, cy + 0.1), fontsize=12, color='black')

# Label the hydrogen atoms
for i, (cx, cy) in enumerate(zip(x, y), start=1):
    for j in range(1, 3):
        angle = theta[i] + (j - 1) * np.pi / 3
        hx = cx + 0.3 * np.cos(angle)
        hy = cy + 0.3 * np.sin(angle)
        ax.annotate(f'H{i}{j}', (hx, hy), fontsize=10, color='black')

# Set the plot limits and remove the axes
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.2, 1.2)
ax.axis('off')

# Add a title
ax.set_title('Benzene Molecular Structure', fontsize=16, pad=20)

# Set a background color (optional)
fig.set_facecolor('white')

# Save the figure
plt.savefig('image.jpg', dpi=100, bbox_inches='tight')

print("Image saved successfully as 'image.jpg'.")

