import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Set the figure size and resolution
fig, ax = plt.subplots(figsize=(8, 6), dpi=300)

# Add the question at the top
ax.set_title("What is the primary focus of the book?", fontsize=14, pad=20)

# Draw the plane
x = np.linspace(-1, 1, 100)
y1 = np.sqrt(1 - x**2)
y2 = -np.sqrt(1 - x**2)

ax.plot(x, y1, color='black', label='A')
ax.plot(x, y2, color='black', label='B')
ax.axvline(0, color='black', label='C')
ax.axhline(0, color='black', label='D')

# Adjust plot limits and aspect ratio
ax.set_xlim(-1.1, 1.1)
ax.set_ylim(-1.1, 1.1)
ax.set_aspect('equal')

# Label the edges
ax.legend(title='Edges', loc='upper left', bbox_to_anchor=(1.01, 1), borderaxespad=0)

# Remove ticks and spines
ax.set_xticks([])
ax.set_yticks([])
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

# Adjust the layout and save the figure
plt.tight_layout()
plt.savefig('plane.jpg', bbox_inches='tight', dpi=300)

