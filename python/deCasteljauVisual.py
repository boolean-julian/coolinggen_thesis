import matplotlib.pyplot as plt
import numpy as np

from matplotlib import rc
rc('text', usetex=True)


def casteljau_step(points, t):
	result = [(1-t) * points[i] + t * points[i+1] for i in range(len(points)-1)]
	return np.array(result)

def casteljau_complete(control_points, t):
	pointlist = [control_points]
	for i in range(len(control_points)-1):
		pointlist.append(casteljau_step(pointlist[-1], t))

	return pointlist



def plot_all_points(pointlist, t):
	colors = ["tab:blue", "tab:orange", "tab:green"]

	for i in range(len(pointlist)):
		xs = [point[0] for point in pointlist[i]]
		ys = [point[1] for point in pointlist[i]]
			
		if len(xs) == 1:
			plt.plot(xs, ys, 'o', color="tab:red")
		else:
			plt.plot(xs, ys, '.-', color=colors[i])

		"""
		if i > 0:
			for j in range(len(xs)):
				plt.text(xs[j], ys[j], f"t = {t}")
		"""

def plot_curve_point(pointlist):
	colors = ["tab:blue", "tab:orange", "tab:green"]

	for i in range(len(pointlist)):
		xs = [point[0] for point in pointlist[i]]
		ys = [point[1] for point in pointlist[i]]
			
		if len(xs) == 1:
			plt.plot(xs, ys, '.', color="tab:red")

fig, ax = plt.subplots(figsize=(8,4))
ax.set_aspect("equal", "box")

ts = np.linspace(0.1, 0.9, 20)

t1 = 0.5
control_points1 = np.array([[0,0], [0,1]])
points1 = casteljau_complete(control_points1, t1)
plot_all_points(points1, t1)

t2 = 0.4
control_points2 = np.array([[0.25,0], [0.5,1], [0.75,0]])
points2 = casteljau_complete(control_points2, t2)
plot_all_points(points2, t2)
for t in ts:
	plot_curve_point(casteljau_complete(control_points2, t))

t3 = 0.6
control_points3 = np.array([[0.75,1], [1, 0], [1.25, 0], [1.5, 1]])
points3 = casteljau_complete(control_points3, t3)
plot_all_points(points3, t3)
for t in ts:
	plot_curve_point(casteljau_complete(control_points3, t))

plt.text(0.05, 0.5, r"$t_1 = 0.5$")
plt.text(0.41, 0.3, r"$t_2 = 0.4$")
plt.text(1.05, 0.4, r"$t_3 = 0.6$")

plt.axis('off')

plt.savefig("deCasteljauVisual.svg")

plt.show()