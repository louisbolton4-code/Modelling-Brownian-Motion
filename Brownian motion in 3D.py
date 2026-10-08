import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

T = 1000
dt = 1
N = int(T / dt)
dW = np.sqrt(dt) * np.random.randn(N, 3)
W = np.cumsum(dW, axis=0)

fig = plt.figure(figsize=(7, 6))
ax = fig.add_subplot(111, projection='3d')
ax.set_title("Animated 3D Brownian Motion")

ax.set_xlim(W[:,0].min()-1, W[:,0].max()+1)
ax.set_ylim(W[:,1].min()-1, W[:,1].max()+1)
ax.set_zlim(W[:,2].min()-1, W[:,2].max()+1)

line, = ax.plot([], [], [], lw=2)

def update(frame):
    line.set_data(W[:frame, 0], W[:frame, 1])
    line.set_3d_properties(W[:frame, 2])
    return line,

ani = FuncAnimation(fig, update, frames=N, interval=10, blit=True)
plt.show()