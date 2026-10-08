import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

T = 1000
dt = 1
N = int(T / dt)
dW = np.sqrt(dt) * np.random.randn(N, 2)
W = np.cumsum(dW, axis=0)


fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(W[:, 0].min()-1, W[:, 0].max()+1)
ax.set_ylim(W[:, 1].min()-1, W[:, 1].max()+1)
ax.set_title("Animated 2D Brownian Motion")
line, = ax.plot([], [], lw=2)


def update(frame):
    line.set_data(W[:frame, 0], W[:frame, 1])
    return line,


ani = FuncAnimation(fig, update, frames=N, interval=10, blit=True)
plt.show()
