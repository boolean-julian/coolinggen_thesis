import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc
rc('text', usetex=True)

def gamma(t):
	base_freq = 2*np.pi*t
	osci_freq = 16*base_freq
	osci_ampl = 0.02

	circle 		= np.array([1.2*np.cos(base_freq), np.sin(base_freq)])
	oscillation = np.array([np.cos(osci_freq), np.sin(osci_freq)])
	oscillation *= osci_ampl

	return circle+oscillation

def rotate_point(point, phi, origin = np.array([0,0])):
	shifted = point - origin
	rotated = np.array([[np.cos(phi),-np.sin(phi)],[np.sin(phi),np.cos(phi)]]) @ shifted

	return rotated + origin
	
def gamma2(t):
	freq = 5*np.pi
	amp = 0.04
	point = np.array([t, amp*np.sin(freq*t)])
	
	phi = 5*np.pi/12
	rotated = rotate_point(point, phi)

	return rotated

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

ts = np.linspace(-0.05, 1.05, 1000)
ps = [gamma2(t) for t in ts]
ds = [-0.1, 0.1]
os = [[offset(gamma2, d, t) for t in ts] for d in ds]

fig, ax = plt.subplots(figsize=(4,8))
ax.set_aspect("equal", "box")

plot_points(ps)
for i in range(len(ds)):
	plot_points(os[i])

fontsize = 18
plt.text(*ps[-1], r"$\gamma$", va="top", ha="left", fontsize=fontsize)
for i in range(len(ds)):
	plt.text(*(os[i])[-1], r"$O^\gamma_{{{d}}}$".format(d=ds[i]), va="top", ha="left", fontsize=fontsize)

plt.axis("off")
plt.tight_layout()
plt.savefig("offsetCurveExampleBeamer.svg")
plt.show()
