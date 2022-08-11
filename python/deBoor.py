import numpy as np
import matplotlib.pyplot as plt

from matplotlib import rc
rc('text', usetex=True)

P = np.array([
	[-0.1, 0.2],
	[0.8, 0.0],
	[1.0, 1.0], 
	[0.7, 1.5],
	[0.2, 1.0],
	[0, 1.5],
	[-0.2, 0.5]
])

W = [1, 1, 1, 1, 1, 1, 1]
U = [0, 0, 0, 0, 0.25, 0.5, 0.75, 1, 1, 1, 1]
n = 3

ts = np.linspace(0.0, 1.0, 1000)

def phi_w(P, W):
	Pw = np.zeros((len(P), len(P[0])+1))
	for i in range(len(P)):
		for j in range(len(P[0])):
			Pw[i][j] = P[i][j] * W[i]

		Pw[i][len(P[0])] = W[i]

	return Pw

def phi_dagger(Cw):
	C = []
	for i in range(len(Cw)):
		C.append([Cw[i][0]/Cw[i][2], Cw[i][1]/Cw[i][2]])

	return np.array(C)


def getIndexAndMultiplicity(u, U, n):
	multiplicity = 0
	for k in range(len(U)):
		if U[k] == u:
			multiplicity += 1

	for k in range(n-1, len(U)-n):
		if U[k] <= u and u < U[k+1]:
			return k, multiplicity
	if u == U[len(U)-1]:
		return len(U)-n, multiplicity


def deBoor(Pw, U, n, u):
	k, m = getIndexAndMultiplicity(u, U, n)

	Ps = np.zeros((n-m+2, len(Pw), len(Pw[0])))

	Ps[0] = Pw

	for i in range(1, n-m+1):
		for j in range(k-n+i, k-m+1):
			alpha = (u - U[j]) / (U[j+n-i+1] - U[j])
			Ps[i, j] = (1-alpha) * Ps[i-1, j-1] + alpha * Ps[i-1, j]

	idk = 0
	if u == 0:
		idk = 1
	if u == 1:
		idk = 2

	return Ps[n-m, k-m+idk]

def plot_points(points, fmt = '-', color = "tab:orange", alpha = 1):
	xs = [point[0] for point in points]
	ys = [point[1] for point in points]

	plt.plot(xs, ys, fmt, color = color, linewidth=1, alpha=alpha)

def get_nurbs(Pw):
	Cw = []
	for i in range(len(ts)):
		Cw.append(deBoor(Pw, U, n, ts[i]))

	return np.array(Cw)

fig, ax = plt.subplots(figsize=(5,5))
ax.set_aspect("equal", "box")

# round 1
Pw = phi_w(P, W)
Cw = get_nurbs(Pw)
C = phi_dagger(Cw)

plot_points(P, fmt = "o--", color = "tab:blue", alpha=0.5)
plot_points(Cw)

# round 2
W[2] = 0.95
Pw = phi_w(P, W)
Cw = get_nurbs(Pw)
C = phi_dagger(Cw)

plot_points(Cw)


# round 3
W[2] = 1.05
Pw = phi_w(P, W)
Cw = get_nurbs(Pw)
C = phi_dagger(Cw)

plot_points(Cw)

plt.axis('off')
plt.tight_layout()

plt.savefig("nurbsCurveExample.svg")

plt.show()