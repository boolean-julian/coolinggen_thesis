import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import rc
rc('text', usetex=True)

fig, ax = plt.subplots(1, 2, subplot_kw={'projection': '3d'}, figsize=(6,3))

for i in range(len(ax)):
	ax[i].set_zlim((-1, 1))
	ax[i].axis("off")
	ax[i].view_init(60, 45)

def plot_points(ax, points):
	xs = points[:,0]
	ys = points[:,1]
	zs = points[:,2]

	ax.plot3D(xs, ys, zs)

def plot_surf(ax, points):
	xs = points[:,0]
	ys = points[:,1]
	zs = points[:,2]
	ax.plot_surface(C[:,:,0], C[:,:,1], C[:,:,2], color = "tab:purple")

def sc(t):
	amp = 0.5
	freq = 0.5
	return amp*np.sin(2*np.pi*freq*t)

def sd(t):
	amp = 0.05
	freq = 5.5
	return amp*np.sin(2*np.pi*freq*t)

def c0(t):
	return np.array([t, 0, sc(t)])

def c1(t):
	return np.array([t, 1, -sd(t)])

def d0(t):
	return np.array([0, t, -sc(t)])

def d1(t):
	return np.array([1, t, sd(t)])

def coon(s, t):
	lc = (1-t)*c0(s) + t*c1(s)
	ld = (1-s)*d0(t) + s*d1(t)

	b 	= (1-s) * (1-t) * c0(0) \
		+ s 	* (1-t) * c0(1) \
		+ (1-s) * t 	* c1(0) \
		+ s 	* t 	* c1(1)

	c = lc + ld - b
	return c

ts = np.linspace(0, 1, 1000)
dx = np.array([0.15, 0, 0])
cx = np.array([0, 0.10, 0])

c0p = np.array([c0(t) for t in ts])
plot_points(ax[0], c0p)

c1p = np.array([c1(t) for t in ts])
plot_points(ax[0], c1p)

d0p = np.array([d0(t) for t in ts])
plot_points(ax[0], d0p)

d1p = np.array([d1(t) for t in ts])
plot_points(ax[0], d1p)

ss = np.linspace(0, 1, 100)
C = np.array([[coon(s, t) for t in ss] for s in ss])
plot_surf(ax[1], C)


for i in range(len(ax)):
	ax[i].text(*(c0(0.5)-cx), r"$c_0$")
	ax[i].text(*(c1(0.5)+cx), r"$c_1$")
	ax[i].text(*(d0(0.5)-dx*0.5), r"$d_0$")
	ax[i].text(*(d1(0.5)+dx), r"$d_1$")

plt.tight_layout()
plt.savefig("coonsPatch.svg")

plt.show()