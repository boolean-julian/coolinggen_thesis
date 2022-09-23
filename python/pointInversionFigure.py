import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc
rc('text', usetex=True)

fig, ax = plt.subplots(figsize=(10,5))
ax.set_aspect("equal", "box")
ax.axis("off")

def plot_point(point):
	plt.plot(point[0], point[1], 'o', color="tab:blue")

def plot_points(points, f = '-'):
	xs = [point[0] for point in points]
	ys = [point[1] for point in points]

	if (f == '--'):
		plt.plot(xs, ys, f, color="tab:blue")
	else:		
		plt.plot(xs, ys, f, color="tab:orange")

def gamma(t):
	amp = 0.25
	freq = 0.5
	return np.array([t, amp*np.sin(t*np.pi*freq*t)])

def norm(p):
	return np.linalg.norm(p)

def distance(p1, p2):
	return norm(p1-p2)

def point_inversion(gamma, point):
	samples = 1000

	ts = np.linspace(0, 1, samples)
	gs = np.array([gamma(t) for t in ts])

	best_i = 0
	best_dist = 1e5

	for i in range(len(gs)):
		curr_dist = distance(gs[i], point)
		if curr_dist < best_dist:
			best_i = i
			best_dist = curr_dist

	return best_i/samples

ts = np.linspace(0, 1, 1000)

gs = np.array([gamma(t) for t in ts])
ps = np.array([
	[-0.15, -0.15],
	[+0.10, +0.20],
	[+0.40, -0.10],
	[+0.50, +0.30],
	[+0.89, +0.00],
	[+1.05, +0.40]
])

ss = [point_inversion(gamma, p) for p in ps]
fs = np.array([gamma(s) for s in ss])

print(ss)

plot_points(gs)
[plot_points([ps[i], fs[i]], '--') for i in range(len(ps))]
[plot_point(p) for p in ps]
[plot_point(p) for p in fs]

plt.tight_layout()
plt.savefig("pointInversionFigure.svg")
plt.show()