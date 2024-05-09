import matplotlib.pyplot as plt
import seaborn as sns

# Set the figure size and resolution
fig, ax = plt.subplots(figsize=(8, 6), dpi=300)

# Add the question at the top
ax.set_title("What is the primary focus of the document?", fontsize=14, pad=20)

# Draw a blank plot to represent "none"
sns.set_style("whitegrid")
ax.set_xlabel("")
ax.set_ylabel("")
ax.set_xticks([])
ax.set_yticks([])

# Adjust the plot area to cover 80% of the figure
plt.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.9)

# Save the plot as none.jpg
plt.savefig("none.jpg", bbox_inches="tight", dpi=300)

