import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(8, 6))

ax.set_aspect("equal", "box")
ax.axis("off")

def gamma1(t):
	lo, hi = 0.85, 0.935
	s = (hi-lo)*t+lo

	return np.array([s, -0.15*s])

def gamma2(t):
	lo, hi = 0.85, 0.931
	s = (hi-lo)*t+lo

	return np.array([s, -0.2000103805])

def gamma3(t):
	center = np.array([0.931,-0.17])
	radius = 0.2+center[1]

	lo, hi = -90, 82

	lp = lo*np.pi/180
	hp = hi*np.pi/180

	s = (hp-lp)*t+lp
	return radius*np.array([np.cos(s), np.sin(s)])+center


def grad(gamma, t):
	eps = 0.001
	if t+eps > 1:
		eps = -eps

	return (gamma(t+eps)-gamma(t))/eps

def normal(point):
	return np.array([-point[1], point[0]])

def norm(point):
	return np.sqrt(point[0]**2 + point[1]**2)

def offset(gamma, distance, t):
	p = gamma(t)
	n = normal(grad(gamma, t))
	n = n/norm(n)

	return p+distance*n

def linear_interpolation(t, start, end):
	return (1-t)*start + t*end

def sigmoid(t, s):
	return 1/(1 + np.exp(-s*t))

def cubic_interpolation(t, start, end):
	return 2*(start-end)*t**3 - 3*(start-end)*t**2 + start

def sigmoid_interpolation(t, start, end, s):
	return (end-start)*sigmoid(t-0.5, s)+start

def linear_interpolation_offset(gamma, distanceStart, distanceEnd, t):
	p = gamma(t)
	n = normal(grad(gamma, t))
	n = n/norm(n)

	currentDistance = linear_interpolation(t, distanceStart, distanceEnd)

	return p+currentDistance*n

def cubic_interpolation_offset(gamma, distanceStart, distanceEnd, t):
	p = gamma(t)
	n = normal(grad(gamma, t))
	n = n/norm(n)

	currentDistance = cubic_interpolation(t, distanceStart, distanceEnd)

	return p+currentDistance*n

def sigmoid_interpolation_offset(gamma, distanceStart, distanceEnd, t, s):
	p = gamma(t)
	n = normal(grad(gamma, t))
	n = n/norm(n)

	currentDistance = sigmoid_interpolation(t, distanceStart, distanceEnd, s)

	return p+currentDistance*n

def plot_points(points, color = "blue", f = True):
	xs = [p[0] for p in points]
	ys = [p[1] for p in points]

	if f:
		plt.plot(xs, ys, '-', color = color)
	else:
		plt.plot(xs, ys, '--', color = color)

ts = np.linspace(0, 1, 100)

g1p = np.array([gamma1(t) for t in ts])
g2p = np.array([gamma2(t) for t in ts])

g3p = np.array([gamma3(t) for t in ts])


o1 = 0.008
o2 = 0.002

o1p = np.array([offset(gamma1, -o1, t) for t in ts])
o2p = np.array([offset(gamma2, +o2, t) for t in ts])
o3p = np.array([linear_interpolation_offset(gamma3, +o2, +o1, t) for t in ts])
o4p = np.array([sigmoid_interpolation_offset(gamma3, +o2, +o1, t, 15) for t in ts])
o5p = np.array([cubic_interpolation_offset(gamma3, +o2, +o1, t) for t in ts])

o5p = np.array([offset(gamma3, +o1, t) for t in ts])
o4p = np.array([offset(gamma3, +o2, t) for t in ts])


plot_points(g1p, "tab:blue")
plot_points(g2p, "tab:green")
plot_points(g3p, "tab:orange")

plot_points(o1p, "tab:blue", False)
plot_points(o2p, "tab:green", False)
#plot_points(o3p, "tab:blue", False)
plot_points(o4p, "tab:green", False)
plot_points(o5p, "tab:blue", False)

plt.tight_layout()

plt.savefig("nonAlignedOffset.svg")
plt.show()