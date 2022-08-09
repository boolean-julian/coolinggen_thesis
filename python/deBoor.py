import numpy as np
import matplotlib.pyplot as plt

P = [
	[0.0, 0.0],
	[0.2, 0.3],
	[0.5, 0.5], 
	[1.0, 0.2],
	[1.5, 1.4],
	[2.0, 1.3],
	[3.0, 3.0]
]

W = [1, 1, 1, 1, 1, 1, 1]
U = [0, 0, 0, 0, 0.25, 0.5, 0.75, 1, 1, 1, 1]
n = 3

def phi(P, W):
	Pw = []
	for i in range(len(P)):
		Pw.append(P[i])

		for j in range(len(Pw[i])):
			Pw[i][j] *= W[i]

		Pw[i].append(W[i])

	return Pw

def phi_dagger(Cw):
	C = []
	for i in range(len(Cw)):
		C.append([Cw[i][0]/Cw[i][2], Cw[i][1]/Cw[i][2]])

	return C


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

def plot_points(points):
	xs = [point[0] for point in points]
	ys = [point[1] for point in points]

	plt.plot(xs, ys)


Pw = phi(P, W)

ts = np.linspace(0.0, 1.0, 1000)
Cw = []
for i in range(len(ts)):
	Cw.append(deBoor(Pw, U, n, ts[i]))

C = phi_dagger(Cw)

plot_points(P)
plot_points(C)
plt.show()