import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
rc('text', usetex=True)

fig, ax = plt.subplots(1, 3, figsize=(6,2))
for a in ax:
	a.set_aspect("equal", "box")
	a.axis("off")

def plot_points(ax, points, f = "-"):
	xs = [p[0] for p in points]
	ys = [p[1] for p in points]
	ax.plot(xs, ys, f)

def circle(t):
	return np.array([np.cos(2*np.pi*t), np.sin(2*np.pi*t)])

def straight1(t):
	return np.array([2*t-1, 1])

def straight2(t):
	return np.array([1, 2*t-1])

ts = np.linspace(0, 1, 1000)

s1 = np.array([straight1(t) for t in ts])
s2 = np.array([straight2(t) for t in ts])
cs = np.array([circle(t) for t in ts])

plot_points(ax[0], s1)
plot_points(ax[0], s2)
plot_points(ax[0], cs)

fs = 16
ax[0].text(*s1[0], r"$\gamma_1$", ha = "right", va = "top", fontsize = fs)
ax[0].text(*s2[0], r"$\gamma_2$", ha = "right", va = "top", fontsize = fs)
ax[0].text(*cs[625], r"$\phi^{\gamma_1, \gamma_2}_1$", ha = "right", va = "top", fontsize = fs)

plot_points(ax[2], np.array([straight1(t) for t in np.linspace(0,0.5,1000, endpoint=True)]))
plot_points(ax[2], np.array([straight2(t) for t in np.linspace(0,0.5,1000, endpoint=True)]))
plot_points(ax[2], np.array([circle(t) for t in np.linspace(0,0.25,1000, endpoint=True)]))


plt.tight_layout()
plt.savefig("verySimpleFillet.svg")
plt.show()