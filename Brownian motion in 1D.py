from matplotlib.animation import FuncAnimation
import numpy as np
import matplotlib.pyplot as plt

T = 10
dt = 0.01
N = int(T / dt)

dW = np.sqrt(dt) * np.random.randn(N)
W = np.cumsum(dW)

fig, ax = plt.subplots(figsize=(10, 3))

x_min, x_max = W.min(), W.max()
ax.set_xlim(x_min - 1, x_max + 1)
ax.set_ylim(-1, 1)

ax.hlines(0, x_min - 1, x_max + 1, colors='lightgray', linestyles='--')
ax.set_yticks([])
ax.set_title("1D Brownian Motion (dot moving left–right)")

point, = ax.plot([W[0]], [0], 'bo', markersize=10)


def update(frame):
    point.set_data([W[frame]], [0])
    return point,


ani = FuncAnimation(fig, update, frames=N, interval=20, blit=False)
plt.show()
