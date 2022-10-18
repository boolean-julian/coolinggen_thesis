import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
#rc('text', usetex=True)

def grad(gamma, t):
	eps = 0.001
	if t+eps > 1:
		eps = -eps

	return (gamma(t+eps)-gamma(t))/eps

def normal(point):
	return np.array([-point[1], point[0]])

def norm(point):
	return np.sqrt(point[0]**2 + point[1]**2)

# Basic offset
def offset(gamma, distance, t):
	p = gamma(t)
	n = normal(grad(gamma, t))
	n = n/norm(n)

	return p+distance*n

# Plot
def plot_points(ax, points):
	xs = [p[0] for p in points]
	ys = [p[1] for p in points]

	ax.plot(xs, ys)

fig, ax = plt.subplots(figsize=(5,5))
ax.set_aspect("equal", "box")
ax.axis("off")

# Script
def curve(t):
	return np.array([0.05*np.sin(4*np.pi*t), t])

offsets = np.linspace(-0.4, 0.4, 5)
print(offsets)

ts = np.linspace(0, 1, 1000)
cs = [np.array([offset(curve, o, t) for t in ts]) for o in offsets]

for i in range(len(offsets)):
	plot_points(ax, cs[i])

plt.show()