import numpy as np
import matplotlib.pyplot as plt
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

# Intersection
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

def _intersect(f1, f1start, f1end, f2, f2start, f2end, depth, intersections):
	samples = 100
	maxdepth = 4
	atol = 1e-8

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

	if f == 'og':
		ax.plot(xs, ys, 'o', color = "tab:green")
	elif f == 'tb--':
		ax.plot(xs, ys, alpha=0.5, color="tab:blue")
	elif f == 'to--':
		ax.plot(xs, ys, alpha=0.5, color="tab:orange")
	else:
		ax.plot(xs, ys, f)

## Curve def
radius = 0.1

def gamma1(t):
	pt = np.array([t, 0.04*np.sin(3*np.pi*t)])
	rt = rotate_point(pt, np.pi/4)
	return rt

def gamma2(t):
	pt = np.array([-0.04*np.sin(3*np.pi*t), 1-t])
	rt = rotate_point(pt, np.pi/4)
	return rt

def draw_circle(ax, radius, center):
	ts = np.linspace(0, 1, 1000)

	xs = radius * np.cos(2*np.pi*ts) + center[0]
	ys = radius * np.sin(2*np.pi*ts) + center[1]

	ax.plot(xs, ys, "tab:green")


fig, ax = plt.subplots(1, 3, figsize=(8,2))
for a in ax:
	a.set_aspect("equal", "box")
	a.axis("off")

ts = np.linspace(0, 1, 1000)
p1 = np.array([gamma1(t) for t in ts])
p2 = np.array([gamma2(t) for t in ts])

radii = [0.1, 0.2, 0.3]
for i in range(len(radii)):
	radius = radii[i]

	def offset1(t):
		return offset(gamma1, radius, t)

	def offset2(t):
		return offset(gamma2, radius, t)

	o1 = np.array([offset1(t) for t in ts])
	o2 = np.array([offset2(t) for t in ts])

	idx = intersect(offset1, offset2)
	center = offset1(idx[0,0])

	plot_points(ax[i], p1)
	plot_points(ax[i], p2)
	plot_points(ax[i], o1, "tb--")
	plot_points(ax[i], o2, "to--")
	plot_points(ax[i], [center], 'og')
	draw_circle(ax[i], radius, center)

	ax[i].text(*(p1[-1]), r"$\gamma_1$")
	ax[i].text(*(p2[0]), r"$\gamma_2$")

	ax[i].text(*(o1[-1]), r"$O^{{\gamma_1}}_{{{r}}}$".format(r = radii[i]))
	ax[i].text(*(o2[0]), r"$O^{{\gamma_2}}_{{{r}}}$".format(r = radii[i]))

plt.tight_layout()
plt.savefig("filletConstruction1.svg")
plt.show()



## second image
fig, ax = plt.subplots(1,4, figsize=(8,1))
for a in ax:
	a.set_aspect("equal", "box")
	a.axis("off")

plot_points(ax[0], p1)
plot_points(ax[0], p2)
ax[0].text(*(p1[-1]), r"$\gamma_1$")	
ax[0].text(*(p2[0]), r"$\gamma_2$")

for i in range(len(radii)):
	radius = radii[i]

	def offset1(t):
		return offset(gamma1, radius, t)

	def offset2(t):
		return offset(gamma2, radius, t)

	o1 = np.array([offset1(t) for t in ts])
	o2 = np.array([offset2(t) for t in ts])

	idx = intersect(offset1, offset2)
	center = offset1(idx[0,0])

	def circle(t):
		pt = np.array([np.cos(2*np.pi*t), np.sin(2*np.pi*t)])
		pt = radius * pt + center
		return pt

	cs = np.array([circle(t) for t in ts])
	
	distance = 1000
	jbest1 = 0
	kbest1 = 0
	for j in range(0, len(p1), 2):
		for k in range(0, len(cs), 2):
			if norm(cs[k] - p1[j]) < distance:
				distance = norm(cs[k] - p1[j])
				jbest1 = j
				kbest1 = k

	distance = 1000
	jbest2 = 0
	kbest2 = 0
	for j in range(0, len(p2), 2):
		for k in range(0, len(cs), 2):
			if norm(cs[k] - p2[j]) < distance:
				distance = norm(cs[k] - p2[j])
				jbest2 = j
				kbest2 = k

	plot_points(ax[i+1], p1[jbest1:])	
	plot_points(ax[i+1], p2[:jbest2])
	plot_points(ax[i+1], cs[kbest2:kbest1])

	ax[i+1].text(*(p1[-1]), r"$\overline{\gamma_1}$")	
	ax[i+1].text(*(p2[0]), r"$\overline{\gamma_2}$")
	
	ax[i+1].text(*(cs[kbest1]), r"$\phi_{{{d}}}^{{\gamma_1, \gamma_2}}$".format(d=radii[i]), va = "top", ha = "left")

plt.tight_layout()
plt.savefig("filletConstruction2.svg")
plt.show()