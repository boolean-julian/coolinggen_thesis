import numpy as np
import matplotlib.pyplot as plt

from matplotlib import rc
rc('text', usetex=True)

fig, ax = plt.subplots(figsize = (2,2))
ax.set_aspect("equal", "box")
ax.axis("off")

width = 0.005
head_width = 30*width

def make_arrow_two_sided(x, y, dx, dy, label, offset, color = "gray"):
	xm = x+dx/2
	ym = y+dy/2

	plt.arrow(xm, ym, dx/2, dy/2, width=width, head_width = head_width, length_includes_head = True, color = color)
	plt.arrow(xm, ym, -dx/2, -dy/2, width=width, head_width = head_width, length_includes_head = True, color = color)

	if dx != 0:
		phi = np.arctan(dy/dx)
	else:
		phi = np.pi/2
	phi = phi*180/np.pi

	xt = xm - np.sin(phi)*offset
	yt = ym + np.cos(phi)*offset

	plt.text(xt, yt, label, horizontalalignment='center', verticalalignment='center', rotation = phi)


def make_arrow_one_sided(x, y, dx, dy, label, offset, color = "gray"):
	xm = x+dx/2
	ym = y+dy/2

	plt.plot(x, y, 'o', color = color)
	plt.arrow(x, y, dx, dy, width=width, head_width = head_width, length_includes_head = True, color = color)
	
	if dx != 0:
		phi = np.arctan(dy/dx)
	else:
		phi = np.pi/2
	phi = phi*180/np.pi

	xt = xm - np.sin(phi)*offset
	yt = ym + np.cos(phi)*offset

	plt.text(xt, yt, label, horizontalalignment='center', verticalalignment='center', rotation = phi)



def plot_points(points, color):
	xs = points[:,0]
	ys = points[:,1]

	plt.plot(xs, ys, color=color)

def plot_point(point, color):
	plt.plot(*point, 'o', color = color)


def curve1(t):
	return np.array([2*t-1, 1])

def curve2(t):
	return np.array([-1, 2*t-1])

def circle(t):
	return np.array([np.cos(2*np.pi*t), np.sin(2*np.pi*t)])

ts = np.linspace(0, 1, 1000)

cp1 = np.array([curve1(t) for t in ts])
cp2 = np.array([curve2(t) for t in ts])

midpoint = np.array([0,0])

make_arrow_two_sided(-1, 1.15, 1, 0, r"$r$", 0.15)
make_arrow_two_sided(-1.15, 1, 0, -1, r"$r$", 0.15)

plot_points(cp1, "tab:blue")
plot_points(cp2, "tab:orange")

plt.plot([-1,0], [0,1], "--", color="grey")
plt.plot([-1,0], [0,0], "--", color="tab:orange")
plt.plot([0,0], [0,1], "--", color="tab:blue")

make_arrow_one_sided(-1, 1, 1, -1, "", 0.05, color = "green")

plot_point(midpoint, "tab:green")

cp3 = np.array([circle(t) for t in ts])
plot_points(cp3, "tab:green")

plt.tight_layout()

plt.savefig("rightAngleFillet.svg")
plt.show()