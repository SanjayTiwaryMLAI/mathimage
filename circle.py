import matplotlib.pyplot as plt
import seaborn as sns

# Set the context for the plot
context = "Draw a circle using Matplotlib and Seaborn"

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(5, 5), dpi=300)

# Draw the circle
circle = plt.Circle((0, 0), radius=2, fill=False, color='r', linewidth=2)
ax.add_artist(circle)

# Set the aspect ratio to make the circle appear circular
ax.set_aspect('equal')

# Label the edges
ax.annotate('A', xy=(2, 0), xytext=(2.2, 0), fontsize=12)
ax.annotate('B', xy=(0, 2), xytext=(0, 2.2), fontsize=12)
ax.annotate('C', xy=(-2, 0), xytext=(-2.2, 0), fontsize=12)
ax.annotate('D', xy=(0, -2), xytext=(0, -2.2), fontsize=12)

# Add the context as the title
ax.set_title(context, fontsize=14, pad=20)

# Remove the axis ticks and spines
ax.set_xticks([])
ax.set_yticks([])
sns.despine(ax=ax, left=True, bottom=True)

# Save the plot as an image
plt.savefig('circle.jpg', bbox_inches='tight', dpi=300)

