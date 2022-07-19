import numpy as np
import matplotlib.pyplot as plt

def distance(ps1, ps2):
	D = np.zeros((len(ps1), len(ps2)))
	for i in range(len(ps1)):
		for j in range(len(ps2)):
			D[i,j] = np.linalg.norm(ps1[i] - ps2[j])

	return D

def circle(ts, r, m):
	return [[r*np.cos(2*np.pi*t)+m[0], r*np.sin(2*np.pi*t)+m[1]] for t in ts]

def curve_gradient(curve, t):
	dt = 1e-5
	
	if t+dt > 1:
		dt = -dt

	p_curr = np.array(curve([t]))
	p_next = np.array(curve([t+dt]))

	grad = 1/dt * (p_next - p_curr)
	
	return grad

def curve_normal(curve, ts):
	normal = []
	for t in ts:
		derivative = curve_gradient(curve, t)[0]
		derivative = derivative/np.linalg.norm(derivative)		

		normal.append([-derivative[1], derivative[0]])

	return np.array(normal)

def curve1(ts):
	return [[t, 0.05 * np.sin(4*np.pi*t)] for t in ts]

def curve2(ts):
	return [[0.05 * np.sin(4*np.pi*t), t] for t in ts]

def plot_point(point):
	plt.plot(point[0], point[1], 'x')

def plot_points(points, color):
	xs = [p[0] for p in points]
	ys = [p[1] for p in points]

	plt.plot(xs, ys, '-', color = color)

def make_fillet_circle(fun1, fun2, radius, samples):
	# Input curves
	ts = np.linspace(0, 1, samples)
	original1 = fun1(ts)
	original2 = fun2(ts)

	# Radius-offset curves
	normal1 = curve_normal(fun1, ts)
	normal2 = curve_normal(fun2, ts)

	offset1 = original1 + radius * normal1
	offset2 = original2 - radius * normal2

	# Minimum of distance between radius-offset curves
	D = distance(offset1, offset2)
	intersectionIndex1, intersectionIndex2 = np.unravel_index(np.argmin(D), D.shape)

	midPoint1 = offset1[intersectionIndex1]
	midPoint2 = offset2[intersectionIndex2]
	midPoint = 0.5 * (midPoint1 + midPoint2)

	# Truncate original curves to fit the fillet
	#original1 = original1[intersectionIndex1:]
	#original2 = original2[intersectionIndex2:]

	# Make fillet
	filletCircle = circle(ts, radius, midPoint)

	plot_points(filletCircle, "tab:orange")


fig, ax = plt.subplots(figsize=(5,5))
ax.set_aspect("equal", "box")

samples = 500
radii = [0.05, 0.1, 0.2, 0.4]

ts = np.linspace(0, 1, samples)
original1 = curve1(ts)
original2 = curve2(ts)

plot_points(original1, "tab:blue")
plot_points(original2, "tab:blue")

for r in radii:
	make_fillet_circle(curve1, curve2, r, samples)

plt.axis("off")
plt.savefig("filletVisuals.svg")
plt.show()