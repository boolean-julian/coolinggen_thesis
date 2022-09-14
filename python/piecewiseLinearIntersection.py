import numpy as np
import matplotlib.pyplot as plt

samples = 3
maxdepth = 10
atol = 0.01


def gamma1(t):
	return np.array([np.cos(2*np.pi*t), np.sin(2*np.pi*t)])

def gamma2(t):
	return np.array([0.05*np.cos(20*np.pi*t)+0.9*np.cos(2*np.pi*t)-1, -0.05*np.sin(20*np.pi*t)+0.9*np.sin(2*np.pi*t)])

def plot_points(ax, points, color, fmt = "-"):
	ax.plot(points[0], points[1], fmt, color = color)

ts = np.linspace(0,1,1000)
g1 = gamma1(ts)
g2 = gamma2(ts)

def get_piecewise_linear_interpolation(f, samples, lo, hi):
	ns = np.linspace(lo, hi, samples+1)
	return f(ns)

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

hasplotted = [False]*maxdepth
d1 = ["A", "B", "C", "D", "E", "F"]
d2 = ["A", "G", "H", "I", "J", "K"]
def _intersect(f1, f1start, f1end, f2, f2start, f2end, depth, intersections):
	g1 = get_piecewise_linear_interpolation(f1, samples, f1start, f1end)
	g2 = get_piecewise_linear_interpolation(f2, samples, f2start, f2end)

	def plot_iteration():
		if not hasplotted[depth]:
			plot_points(ax[d1[depth]], gamma1(np.linspace(f1start, f1end, 1000)), "tab:blue")
			plot_points(ax[d1[depth]], gamma2(np.linspace(f2start, f2end, 1000)), "tab:orange")

			plot_points(ax[d1[depth]], g1, "tab:blue", '.')		
			plot_points(ax[d1[depth]], g2, "tab:orange", '.')

			plot_points(ax[d1[depth]], g1[:,[0,samples]], "red", '--')
			plot_points(ax[d1[depth]], g2[:,[0,samples]], "red", '--')
			
			hasplotted[depth] = True

		elif hasplotted[depth]:
			plot_points(ax[d2[depth]], gamma1(np.linspace(f1start, f1end, 1000)), "tab:blue")
			plot_points(ax[d2[depth]], gamma2(np.linspace(f2start, f2end, 1000)), "tab:orange")

			plot_points(ax[d2[depth]], g1, "tab:blue", '.')		
			plot_points(ax[d2[depth]], g2, "tab:orange", '.')

			plot_points(ax[d2[depth]], g1[:,[0,samples]], "red", '--')
			plot_points(ax[d2[depth]], g2[:,[0,samples]], "red", '--')
	
	plot_iteration()

	f1midpoint = 0.5*(f1start+f1end)
	f2midpoint = 0.5*(f2start+f2end)
	if np.linalg.norm(gamma1(f1midpoint) - gamma2(f2midpoint)) <= atol:
		intersections.append(gamma1(f1midpoint))
		print("Point found at depth", depth)
		return

	if depth >= maxdepth:
		print("Maximum depth reached! Returning zilch.")
		return

	for i in range(samples):
		for j in range(samples):
			g1s = g1[:,i]
			g1e = g1[:,i+1]

			g2s = g2[:,j]
			g2e = g2[:,j+1]

			if (check_2d_intersection(g1s, g1e, g2s, g2e)):
				g1start = (f1end - f1start) * i/samples + f1start
				g1end = (f1end - f1start) * (i+1)/samples + f1start
				
				g2start = (f2end - f2start) * j/samples + f2start				
				g2end = (f2end - f2start) * (j+1)/samples + f2start

				_intersect(f1, g1start, g1end, f2, g2start, g2end, depth+1, intersections)


def intersect(f1, f2):
	intersections = []
	_intersect(f1, 0, 1, f2, 0, 1, 0, intersections)
	return np.array(intersections).T

fig, ax = plt.subplot_mosaic(
	"""
	AABCDEFLL
	AAGHIJKLL
	""",
	
	figsize=(9,3)
)

for a in ax:
	ax[a].axis("off")
	ax[a].set_aspect("equal", "box")

intersections = intersect(gamma1, gamma2)
plot_points(ax["L"], gamma1(ts), "tab:blue")
plot_points(ax["L"], gamma2(ts), "tab:orange")
plot_points(ax["L"], intersections, "red", 'o')

print(intersections)

plt.tight_layout()
plt.savefig("piecewiseLinearIntersection.svg")
#plt.show()