import pygame
import math
import random
import os

# Constants
WINDOW_WIDTH = 2160
WINDOW_HEIGHT = 1080
ORIGIN_X = WINDOW_WIDTH // 2
ORIGIN_Y = WINDOW_HEIGHT // 3
G = 9.81

# Colors
BLACK = (0, 0, 0)

class Link:
    def __init__(self, length, mass, radius, theta_0, omega_0):
        self.length = length
        self.states = [theta_0, omega_0]
        self.mass = mass
        self.radius = radius  # Add radius attribute
        self.shape = [(ORIGIN_X, ORIGIN_Y), (0, 0)]

class Mass:
    def __init__(self, mass, radius):
        self.mass = mass
        self.radius = radius

class DoublePendulum:
    def __init__(self, link1, link2, color):
        self.link1 = link1
        self.link2 = link2
        self.states = [link1.states[1], link2.states[1], link1.states[0], link2.states[0]]
        self.color = color

    def system(self, states):
        m1 = self.link1.mass.mass
        m2 = self.link2.mass.mass
        l1 = self.link1.length
        l2 = self.link2.length
        omega1, omega2, theta1, theta2 = states

        m = [[(m1 + m2) * l1, m2 * l2 * math.cos(theta1 - theta2)],
             [l1 * math.cos(theta1 - theta2), l2]]
        f = [(-m2 * l2 * omega2**2 * math.sin(theta1 - theta2) - (m1 + m2) * G * math.sin(theta1)),
             (l1 * omega1**2 * math.sin(theta1 - theta2) - G * math.sin(theta2))]

        det_m = m[0][0] * m[1][1] - m[0][1] * m[1][0]
        acceleration = [0, 0]
        acceleration[0] = (f[0] * m[1][1] - f[1] * m[0][1]) / det_m
        acceleration[1] = (f[1] * m[0][0] - f[0] * m[1][0]) / det_m

        return acceleration + [omega1, omega2]

    def runge_kutta(self, states, dt):
        k1 = self.system(states)
        k2 = self.system([x + 0.5 * y * dt for x, y in zip(states, k1)])
        k3 = self.system([x + 0.5 * y * dt for x, y in zip(states, k2)])
        k4 = self.system([x + y * dt for x, y in zip(states, k3)])

        return [(dt * (x + 2 * y + 2 * z + w) / 6) for x, y, z, w in zip(k1, k2, k3, k4)]

    def get_position(self):
        scale = 150  # Adjust scale factor
        l1 = self.link1.length
        l2 = self.link2.length
        theta1 = self.states[2]
        theta2 = self.states[3]
        x1 = l1 * scale * math.sin(theta1) + ORIGIN_X
        y1 = l1 * scale * math.cos(theta1) + ORIGIN_Y
        x2 = x1 + l2 * scale * math.sin(theta2)
        y2 = y1 + l2 * scale * math.cos(theta2)

        return (x1, y1), (x2, y2)

    def update_position(self, dt):
        self.states = [x + y for x, y in zip(self.states, self.runge_kutta(self.states, dt))]

        pos1, pos2 = self.get_position()

        self.link1.shape = [(ORIGIN_X, ORIGIN_Y), pos1]
        self.link2.shape = [pos1, pos2]

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# Create DoublePendulum instances
num_pendulums = 500  # Number of pendulums
pendulums = []
for i in range(num_pendulums):
    theta1_offset = i * (2 * math.pi / num_pendulums)  # Add offset to initial angle
    theta2_offset = i * (2 * math.pi / num_pendulums) / 2  # Add offset to initial angle
    link1 = Link(2.0, Mass(1.0, 10.0), 10.0, math.radians(90) + theta1_offset, 2.0)
    link2 = Link(2.0, Mass(3.0, 10.0), 10.0, math.radians(130) + theta2_offset, 0.0)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    pendulums.append(DoublePendulum(link1, link2, color))

# Create directory to store frames
frames_dir = 'frames'
os.makedirs(frames_dir, exist_ok=True)

# Simulation Loop
is_running = True
frame_duration = 1 / 60  # Duration of each frame in seconds (60 fps)
total_duration = 10  # Total duration of the video in seconds
num_frames = int(total_duration / frame_duration)  # Total number of frames

for frame_num in range(num_frames):
    dt = frame_duration  # Constant time step for video recording

    for pendulum in pendulums:
        pendulum.update_position(dt)
        pygame.draw.line(screen, pendulum.color, pendulum.link1.shape[0], pendulum.link1.shape[1], 5)
        pygame.draw.line(screen, pendulum.color, pendulum.link2.shape[0], pendulum.link2.shape[1], 5)

    # Capture current frame
    frame_filename = os.path.join(frames_dir, f'frame_{frame_num:04}.png')
    pygame.image.save(screen, frame_filename)

# Quit Pygame
pygame.quit()
