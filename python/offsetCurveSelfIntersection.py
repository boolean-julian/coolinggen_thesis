import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc
rc('text', usetex=True)


# Basic operations
def rotate_point(point, phi, origin = np.array([0,0])):
	shifted = point - origin
	rotated = np.array([[np.cos(phi),-np.sin(phi)],[np.sin(phi),np.cos(phi)]]) @ shifted

	return rotated + origin

def grad(gamma, t):
	eps = 0.001
	if t+eps > 1:
		eps = -eps

	return (gamma(t+eps)-gamma(t))/eps

def normal(point):
	return np.array([-point[1], point[0]])

def norm(point):
	return np.sqrt(point[0]**2 + point[1]**2)

# Basic offset
def offset(gamma, distance, t):
	p = gamma(t)
	n = normal(grad(gamma, t))
	n = n/norm(n)

	return p+distance*n

# Intersection algos
samples = 100
maxdepth = 4
atol = 1e-8
def check_2d_intersection(astart, aend, bstart, bend):
	adirection = aend - astart
	bdirection = bend - bstart

	d = bstart - astart
	dx = d[0]
	dy = d[1]

	det = bdirection[0] * adirection[1] - bdirection[1] * adirection[0]
	if det == 0:
		return False

	ta = dy * bdirection[0] - dx * bdirection[1]
	ta /= det

	tb = dy * adirection[0] - dx * adirection[1]
	tb /= det

	if 0 <= ta and ta <= 1 and 0 <= tb and tb <= 1:
		return True

	return False

def get_piecewise_linear_interpolation(f, samples, lo, hi):
	ns = np.linspace(lo, hi, samples+1)
	return np.array([f(n) for n in ns])

def _self_intersect(f1, f1start, f1end, f2, f2start, f2end, depth, intersections):
	g1 = get_piecewise_linear_interpolation(f1, samples, f1start, f1end)
	g2 = get_piecewise_linear_interpolation(f2, samples, f2start, f2end)

	for i in range(samples):
		for j in range(i+2, samples):
			g1s = g1[i]
			g1e = g1[i+1]

			g2s = g2[j]
			g2e = g2[j+1]

			if (check_2d_intersection(g1s, g1e, g2s, g2e)):
				g1start = (f1end - f1start) * i/samples + f1start
				g1end = (f1end - f1start) * (i+1)/samples + f1start
				
				g2start = (f2end - f2start) * j/samples + f2start				
				g2end = (f2end - f2start) * (j+1)/samples + f2start

				_intersect(f1, g1start, g1end, f2, g2start, g2end, depth+1, intersections)

def self_intersect(f1):
	intersections = []
	_self_intersect(f1, 0, 1, f1, 0, 1, 0, intersections)
	return np.array(intersections)

def _intersect(f1, f1start, f1end, f2, f2start, f2end, depth, intersections):
	g1 = get_piecewise_linear_interpolation(f1, samples, f1start, f1end)
	g2 = get_piecewise_linear_interpolation(f2, samples, f2start, f2end)

	f1midpoint = 0.5*(f1start+f1end)
	f2midpoint = 0.5*(f2start+f2end)
	if np.linalg.norm(f1(f1midpoint) - f2(f2midpoint)) <= atol:
		intersections.append((f1midpoint, f2midpoint))
		#print("Point found at depth", depth)
		return

	if depth >= maxdepth:
		#print("Maximum depth reached! Returning zilch.")
		return

	for i in range(samples):
		for j in range(samples):
			g1s = g1[i]
			g1e = g1[i+1]

			g2s = g2[j]
			g2e = g2[j+1]

			if (check_2d_intersection(g1s, g1e, g2s, g2e)):
				g1start = (f1end - f1start) * i/samples + f1start
				g1end = (f1end - f1start) * (i+1)/samples + f1start
				
				g2start = (f2end - f2start) * j/samples + f2start				
				g2end = (f2end - f2start) * (j+1)/samples + f2start

				_intersect(f1, g1start, g1end, f2, g2start, g2end, depth+1, intersections)


def intersect(f1, f2):
	intersections = []
	_intersect(f1, 0, 1, f2, 0, 1, 0, intersections)
	return np.array(intersections)


# Drawing
def plot_points(ax, points, f = "-"):
	xs = [p[0] for p in points]
	ys = [p[1] for p in points]

	if f == 'ro':
		ax.plot(xs, ys, f, alpha=0.5)
	else:
		ax.plot(xs, ys, f)

# Curve defs
def gamma(t):
	base_freq = 2*np.pi*t
	osci_freq = 16*base_freq
	osci_ampl = 0.02

	circle 		= np.array([1.2*np.cos(base_freq), np.sin(base_freq)])
	oscillation = np.array([np.cos(osci_freq), np.sin(osci_freq)])
	oscillation *= osci_ampl

	return circle+oscillation

def gamma2(t):
	freq = 5.2*np.pi
	amp = 0.04
	point = np.array([t, amp*np.sin(freq*t - 1.1 * np.pi)])
	
	phi = np.pi/12
	rotated = rotate_point(point, phi)

	return rotated

# Problem statement
ts = np.linspace(0, 1, 1000)
ps = [gamma2(t) for t in ts]
ds = [-0.2, 0.2]

os = [[offset(gamma2, d, t) for t in ts] for d in ds]

def o0(t):
	return offset(gamma2, ds[0], t)

def o1(t):
	return offset(gamma2, ds[1], t)

fig, ax = plt.subplots(1, 2, figsize=(10,3))

ax[0].set_aspect("equal", "box")
ax[1].set_aspect("equal", "box")

plot_points(ax[0], ps)
plot_points(ax[0], os[0])
plot_points(ax[0], os[1], "tab:purple")

"""
fontsize = 18
ax[0].text(*ps[-1], r"$\gamma$", va="top", ha="left", fontsize=fontsize)
for i in range(len(ds)):
	ax[0].text(*(os[i])[-1], r"$O^\gamma_{{{d}}}$".format(d=ds[i]), va="top", ha="left", fontsize=fontsize)
"""

# Set theoretic operators
def intervals_overlap(arr, i, j):
	a = arr[i]
	b = arr[j]

	return a[1] >= b[0] and b[1] >= a[0]

def union_interval(arr, i, j):
	a = arr[i]
	b = arr[j]

	c = np.array([min(a[0], b[0]), max(a[1], b[1])])
	return c

def remove_duplicates(arr):
	shape = arr.shape[1]
	return np.unique(arr).reshape((-1, shape))

def remove_overlap(arr):
	for i in range(len(arr)):
		for j in range(i+1, len(arr)):
			if (intervals_overlap(arr, i, j)):
				arr[i] = union_interval(arr, i, j)
				arr[j] = union_interval(arr, i, j)

	arr = remove_duplicates(arr)
	return arr

def get_offset_trim_indices(offset):
	intersection_params = self_intersect(offset)
	intersection_params = remove_overlap(intersection_params);	

	indices = [0]
	for i in range(len(intersection_params)):
		indices.append(intersection_params[i,0])
		indices.append(intersection_params[i,1])
	indices.append(1)

	return indices

# Draw result
def plot_trimmed_curve(offset, f = "-", invert=False):
	idx = get_offset_trim_indices(offset)

	pointlist = []
	for i in range(0, len(idx), 2):
		pointlist.append([])
		ts = np.linspace(idx[i], idx[i+1], 1000)
		pointlist[-1].append([offset(t) for t in ts])

	pointlist = np.array(pointlist)
	numparts = pointlist.shape[0]
	pointlist = pointlist.reshape((numparts*1000, 2))

	plot_points(ax[1], pointlist, f)


i0 = self_intersect(o0)
i0 = remove_overlap(i0)

i1 = self_intersect(o1)
i1 = remove_overlap(i1)

p0 = [o0(i0[i,0]) for i in range(len(i0))]
plot_points(ax[0], p0, 'ro')

p1 = [o1(i1[i,0]) for i in range(len(i1))]
plot_points(ax[0], p1, 'ro')

plot_points(ax[1], ps)
plot_trimmed_curve(o0)
plot_trimmed_curve(o1, "tab:purple")

ax[0].axis("off")
ax[1].axis("off")

fs = 16
"""
ax[0].text(0.3, 0.35, r"$O^\gamma_{-0.2}$", fontsize = fs, color = "tab:purple")
ax[0].text(0, -0.05, r"$\gamma$", fontsize = fs, color = "tab:blue")
ax[0].text(0.4, -0.18, r"$O^\gamma_{0.2}$", fontsize = fs, color = "tab:orange")


ax[1].text(0.3, 0.35, r"$\overline{O}^\gamma_{-0.2}$", fontsize = fs, color = "tab:purple")
ax[1].text(0, -0.05, r"$\gamma$", fontsize = fs, color = "tab:blue")
ax[1].text(0.4, -0.18, r"$\overline{O}^\gamma_{0.2}$", fontsize = fs, color = "tab:orange")
"""

g0 = [offset(gamma2, -0.1, t) for t in ts]
g1 = [offset(gamma2, 0.1, t) for t in ts]

for i in range(2):
	plot_points(ax[i], g0, "tab:green")
	plot_points(ax[i], g1, "tab:red")

# Write
plt.tight_layout()

extent0 = ax[0].get_window_extent().transformed(fig.dpi_scale_trans.inverted())
extent1 = ax[1].get_window_extent().transformed(fig.dpi_scale_trans.inverted())

plt.savefig('offsetCurveSelfIntersection0.svg', bbox_inches=extent0)
plt.savefig('offsetCurveSelfIntersection1.svg', bbox_inches=extent1)



plt.show()
