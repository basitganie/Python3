import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.integrate import solve_ivp

# Define the harmonic oscillator equation
def harmonic_oscillator(t, y, omega):
    x, v = y
    dxdt = v
    dvdt = -omega**2 * x
    return [dxdt, dvdt]

# Parameters
omega = 2*np.pi  # Angular frequency

# Initial conditions
initial_conditions = [1, 0]  # Initial position and velocity

# Time points for simulation
t_span = (0, 10)  # Simulation time span
t_eval = np.linspace(t_span[0], t_span[1], 1000)  # Time points for evaluation

# Solve the differential equation
solution = solve_ivp(harmonic_oscillator, t_span, initial_conditions, args=(omega,), t_eval=t_eval)

# Interpolate solution for smoother animation
t_smooth = np.linspace(t_span[0], t_span[1], 10000)
x_smooth = np.interp(t_smooth, solution.t, solution.y[0])

# Create a function to update the plot
def update_plot(frame):
    line.set_data(t_smooth[:frame], x_smooth[:frame])
    return line,

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(t_span)
ax.set_ylim(-1.5, 1.5)

# Plot the initial position
line, = ax.plot([], [], lw=2)

# Create animation with increased speed
ani = FuncAnimation(fig, update_plot, frames=len(t_smooth), interval=10, blit=True)  # Decreased interval for higher fps

plt.xlabel('Time')
plt.ylabel('Position')
plt.title('Harmonic Oscillator Animation')
plt.grid(True)

plt.show()
