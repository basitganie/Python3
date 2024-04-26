import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

# Define the x values
x = np.linspace(-10, 10, 100)

# Initialize the figure
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-2, 2)

# Initialize empty plots
line1, = ax.plot([], [], lw=2, label='Sin(x + t)')
line2, = ax.plot([], [], lw=2, label='Cos(x + t)')

# Add legend
ax.legend()

# Update function for the animation
def update(frame):
    y1 = np.sin(x + frame)
    y2 = np.cos(x + frame)

    line1.set_data(x, y1)
    line2.set_data(x, y2)

    return line1, line2

# Create animation
ani = FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 300), interval=10)

# Save the animation as a GIF
ani.save('animation.gif', writer='pillow')

plt.show()
