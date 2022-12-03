import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(10,4))
ax.set_aspect("equal", "box")
ax.axis("off")

def derivative(curve, t):
	dt = 1e-4

	if t+dt > 1:
		dt = -dt

	here = curve(t)
	there = curve(t+dt)

	return 1./dt * (there - here)

def curve1(t):
	return np.array([t, 0.05*np.sin(2*np.pi*t)+0])

def curve2(t):
	return np.array([t+0.5,0.05*np.sin(2*np.pi*t)+1])

def continuation(curve1, curve2, t):
	c1 = curve1(1)
	c2 = curve2(0)

	dc1 = derivative(curve1, 1)
	dc2 = derivative(curve2, 0)

	d =    c1
	c =                  dc1
	b = -3*c1 + 3*c2 - 2*dc1 - dc2
	a =  2*c1 - 2*c2 +   dc1 + dc2

	return a*t**3 + b*t**2 + c*t + d

def plot_points(points):
	plt.plot(points[:,0], points[:,1])

ts = np.linspace(0, 1, 1000)
c1 = np.array([curve1(t) for t in ts])
c2 = np.array([curve2(t) for t in ts])

plot_points(c1)
plot_points(c2)

c3 = np.array([continuation(curve1, curve2, t) for t in ts])
plot_points(c3)


plt.show()