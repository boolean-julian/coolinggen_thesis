import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
rc('text', usetex=True)

fig, ax = plt.subplots(figsize=(2,2))
ax.set_aspect("equal", "box")
ax.axis("off")

def plot_points(points, f = "-"):
	xs = [p[0] for p in points]
	ys = [p[1] for p in points]
	plt.plot(xs, ys, f)

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

plot_points(s1)
plot_points(s2)
plot_points(cs)

fs = 16
plt.text(*s1[0], r"$\gamma_1$", ha = "right", va = "top", fontsize = fs)
plt.text(*s2[0], r"$\gamma_2$", ha = "right", va = "top", fontsize = fs)
plt.text(*cs[625], r"$\phi^{\gamma_1, \gamma_2}_1$", ha = "right", va = "top", fontsize = fs)

plt.tight_layout()
plt.savefig("verySimpleFillet.svg")
plt.show()