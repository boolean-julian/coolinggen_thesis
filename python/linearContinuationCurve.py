import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(5,5))
ax.set_aspect("equal", "box")
ax.axis("off")

def gamma1(t):
	return np.array([0.1*np.sin(2*np.pi*t), t])

def gamma2(t):
	return np.array([t, 0.1*np.sin(2*np.pi*t)])

def plot_points(points, c, f = "-"):
	xs = points[:,0]
	ys = points[:,1]

	plt.plot(xs, ys, f, color = c, lw = 2)

def gradient(curve, t):
	dt = 1e-10
	return 0.5/dt * (curve(t+dt) - curve(t-dt))

def lin_cont(curve, s, sign, t):
	grad = sign*gradient(curve, s)
	grad = grad/np.linalg.norm(grad)

	return curve(s)+t*grad

ts = np.linspace(0.2, 1, 1000)
g1 = np.array([gamma1(t) for t in ts])
g2 = np.array([gamma2(t) for t in ts])

ss = np.linspace(0, 0.5, 100)
c1 = np.array([lin_cont(gamma1, 0.2, -1, s) for s in ss])
c2 = np.array([lin_cont(gamma2, 0.2, -1, s) for s in ss])

plot_points(g1, "tab:blue")
plot_points(g2, "tab:orange")
plot_points(c1, "tab:blue", "--")
plot_points(c2, "tab:orange", "--")

plt.tight_layout()

plt.savefig("linearContinuationCurve.svg")
plt.show()
