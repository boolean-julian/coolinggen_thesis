import matplotlib.pyplot as plt
import numpy as np

def circle0(t):
	return np.array([np.sin(2*np.pi*t), np.cos(2*np.pi*t)])

def circle1(t):
	return 0.7*circle0(t) + np.array([1.7, 0])

def plot_points(pts, f, color):
	plt.plot(pts[:,0], pts[:,1], f, color = color)

fig, ax = plt.subplots(figsize=(8,4))
ax.set_aspect("equal", "box")

ts = np.linspace(0,1,2000)
ks = np.linspace(0,1,6)

cs0 = np.array([circle0(t) for t in ts])
cs1 = np.array([circle1(t) for t in ts])

plot_points(cs0, '-', "tab:blue")
plot_points(cs1, '-', "tab:orange")

ck0 = np.array([circle0(t) for t in ks])
ck1 = np.array([circle1(t) for t in ks])

plot_points(ck0, 'o--', "tab:blue")
plot_points(ck1, 'o--', "tab:orange")

plt.axvline(1, color="black", alpha = 0.5)

ax.axis("off")

plt.tight_layout()
plt.savefig("linearApproxCircleIntersection.svg")
plt.show()

