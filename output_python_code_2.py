import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set the position vectors of the vertices
alpha, beta, gamma = 1, 2, 3
A = np.array([alpha, beta, gamma])
B = np.array([beta, gamma, alpha])
C = np.array([gamma, alpha, beta])

# Create a figure and axis
fig, ax = plt.subplots(figsize=(6, 6))

# Draw the triangle
ax.plot([A[0], B[0]], [A[1], B[1]], 'k-', label='AB')
ax.plot([B[0], C[0]], [B[1], C[1]], 'k-', label='BC')
ax.plot([C[0], A[0]], [C[1], A[1]], 'k-', label='AC')

# Label the vertices
ax.text(A[0], A[1], r'$\vec{A}=\alpha\hat{\imath}+\beta\hat{\jmath}+\gamma\hat{k}$', fontsize=12)
ax.text(B[0], B[1], r'$\vec{B}=\beta\hat{\imath}+\gamma\hat{\jmath}+\alpha\hat{k}$', fontsize=12)
ax.text(C[0], C[1], r'$\vec{C}=\gamma\hat{\imath}+\alpha\hat{\jmath}+\beta\hat{k}$', fontsize=12)

# Add context to the top
context = "If the position vectors of the vertices A, B, and C of a triangle △ABC are αi+βj+γk, βi+γj+αk, and γi+αj+βk respectively, then △ABC is"
ax.text(0.5, 1.05, context, ha='center', va='bottom', transform=ax.transAxes, fontsize=12)

# Set axis limits and remove ticks
ax.set_xlim([-1, 4])
ax.set_ylim([-1, 4])
ax.set_xticks([])
ax.set_yticks([])

# Save the figure as a JPG file
plt.savefig('triangle.jpg', dpi=300, bbox_inches='tight')

