import matplotlib.pyplot as plt
import numpy as np

def gamma(t):
	return np.array([np.cos(2*np.pi*t)+0.05*np.cos(20*np.pi*t), np.sin(2*np.pi*t)+0.05*np.sin(20*np.pi*t)])

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

def plot_points(points):
	xs = [p[0] for p in points]
	ys = [p[1] for p in points]

	plt.plot(xs, ys, '-')

ts = np.linspace(0, 1, 1000)

ps = [gamma(t) for t in ts]
o1 = [offset(gamma, 0.1, t) for t in ts]
o2 = [offset(gamma, 0.2, t) for t in ts]
o3 = [offset(gamma, 0.3, t) for t in ts]

fig, ax = plt.subplots(figsize=(5,5))
ax.set_aspect("equal", "box")

plot_points(ps)
plot_points(o1)
plot_points(o2)
plot_points(o3)

plt.axis("off")
plt.show()
