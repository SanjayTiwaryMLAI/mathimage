import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Set up the plot
plt.figure(figsize=(10, 8))
sns.set_style("whitegrid")

# Create points A and B
A = np.array([1, 1])
B = np.array([7, 5])

# Calculate point R using arbitrary ratio (you can change these values)
m1, m2 = 2, 3
R = (m2 * A + m1 * B) / (m1 + m2)

# Plot the line segment AB
plt.plot([A[0], B[0]], [A[1], B[1]], 'b-', linewidth=2)

# Plot points A, B, and R
plt.scatter([A[0], B[0], R[0]], [A[1], B[1], R[1]], c=['red', 'red', 'green'], s=100)

# Add labels for points
plt.text(A[0]-0.5, A[1]-0.3, 'A', fontsize=12, fontweight='bold')
plt.text(B[0]+0.2, B[1]+0.2, 'B', fontsize=12, fontweight='bold')
plt.text(R[0]+0.2, R[1]-0.3, 'R', fontsize=12, fontweight='bold')

# Add labels for segments
plt.text((A[0]+R[0])/2-0.5, (A[1]+R[1])/2-0.3, f'{m1}', fontsize=12, color='blue')
plt.text((R[0]+B[0])/2+0.3, (R[1]+B[1])/2+0.3, f'{m2}', fontsize=12, color='blue')

# Set axis limits
plt.xlim(0, 8)
plt.ylim(0, 6)

# Add title and labels
plt.title("Section Formula: Dividing a Line Segment Internally", fontsize=16, fontweight='bold')
plt.xlabel("X-axis", fontsize=12)
plt.ylabel("Y-axis", fontsize=12)

# Add the section formula as text
formula = r"$R = \frac{m_2A + m_1B}{m_1 + m_2}$"
plt.text(0.5, 5.5, formula, fontsize=16, bbox=dict(facecolor='white', alpha=0.8))

# Add explanation
explanation = (
    "The section formula divides the line segment AB\n"
    f"internally in the ratio {m1}:{m2}.\n"
    "A, B: Endpoints of the line segment\n"
    "R: Point of division"
)
plt.text(0.5, 0.5, explanation, fontsize=12, bbox=dict(facecolor='white', alpha=0.8))

# Adjust layout and save the image
plt.tight_layout()
plt.savefig("image.jpg", dpi=100)
plt.close()

