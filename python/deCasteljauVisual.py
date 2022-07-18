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


colors = ["tab:blue", "tab:orange", "tab:green"]
def plot_all_points(pointlist, t):
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
	for i in range(len(pointlist)):
		xs = [point[0] for point in pointlist[i]]
		ys = [point[1] for point in pointlist[i]]
		
		if len(xs) == 1:
			plt.plot(xs, ys, '.', color="tab:red")

fig, ax = plt.subplots(figsize=(4,4))
ax.set_aspect("equal", "box")

ts = np.linspace(0.05, 0.95, 20)

"""
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
"""

t3 = 0.6
control_points3 = np.array([[0.6,1], [1, 0.1], [1.35, 0.3], [1.65, 1]])
points3 = casteljau_complete(control_points3, t3)
plot_all_points(points3, t3)
for t in ts:
	plot_curve_point(casteljau_complete(control_points3, t))

#plt.text(0.05, 0.5, r"$t_1 = 0.5$")
#plt.text(0.41, 0.3, r"$t_2 = 0.4$")
#plt.text(1.2, 0.4, r"$t = 0.6$")

xoff = 0.045
yoff = 0.045
fontsize = 12
plt.text(*(points3[0][0] + [-xoff, -yoff]), r"$P^{(0)}_0$", color = colors[0], ha="center", va="center", fontsize=fontsize)
plt.text(*(points3[0][1] + [-xoff, -yoff]), r"$P^{(0)}_1$", color = colors[0], ha="center", va="center", fontsize=fontsize)
plt.text(*(points3[0][2] + [+xoff, -yoff]), r"$P^{(0)}_2$", color = colors[0], ha="center", va="center", fontsize=fontsize)
plt.text(*(points3[0][3] + [+xoff, -yoff]), r"$P^{(0)}_3$", color = colors[0], ha="center", va="center", fontsize=fontsize)

plt.text(*(points3[1][0] + [-xoff, -yoff]), r"$P^{(1)}_0$", color = colors[1], ha="center", va="center", fontsize=fontsize)
plt.text(*(points3[1][1] + [+xoff, -yoff]), r"$P^{(1)}_1$", color = colors[1], ha="center", va="center", fontsize=fontsize)
plt.text(*(points3[1][2] + [+xoff, -yoff]), r"$P^{(1)}_2$", color = colors[1], ha="center", va="center", fontsize=fontsize)

plt.text(*(points3[2][0] + [-xoff, -yoff]), r"$P^{(2)}_0$", color = colors[2], ha="center", va="center", fontsize=fontsize)
plt.text(*(points3[2][1] + [+2*xoff, -yoff]), r"$P^{(2)}_1$", color = colors[2], ha="center", va="center", fontsize=fontsize)

plt.text(*(points3[3][0] + [-0*xoff, +1.5*yoff]), r"$P^{(3)}_0$", color = "tab:red", ha="center", va="center", fontsize=fontsize)


plt.axis('off')
plt.tight_layout()

plt.savefig("deCasteljauVisual.svg")

plt.show()