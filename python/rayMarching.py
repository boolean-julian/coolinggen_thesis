import numpy as np
import matplotlib.pyplot as plt

from matplotlib import rc
rc('text', usetex=True)

fig, ax = plt.subplots(figsize=(12,7))
ax.set_aspect("equal", "box")

samples = int(5e4)
ts = np.linspace(0,1,samples)

fontsize = 20

def curve(t):
	t = 2*t-1
	return (t, t/1.5*np.sin(2*np.pi*t)*np.sin(2*np.pi*t))

def ray(a, b, t):
	return (a[0]+t*b[0], a[1]+t*b[1])

def distance(curve, point):
	distances = np.zeros(len(curve[0]))

	for k in range(len(curve[0])):
		numpyCurvePoint = np.array([curve[0][k], curve[1][k]])
		numpyStatPoint = np.array([point[0], point[1]])

		distances[k] = np.linalg.norm(numpyCurvePoint - numpyStatPoint)

	kbest = np.argmin(distances)
	return distances[kbest]

def draw_circle(center, radius):
	if radius > 0.001:
		ts = np.linspace(0, 1, int(1e3))

		xs = radius * np.cos(2*np.pi*ts)
		ys = radius * np.sin(2*np.pi*ts)

		xs = xs + center[0]
		ys = ys + center[1]

		plt.plot(xs, ys, color="tab:green", linewidth=1)
	
	plt.plot(center[0], center[1], '.', color="tab:green")


def visualize_ray_marching(a, b, cp):
	# normalized direction
	n = b/np.linalg.norm(b)

	# one step of ray marching visualized?
	safedist = 0
	center = a

	collision = False
	while not collision:

		center = center + safedist*n
		safedist = distance(cp, center)
		
		if safedist > 1e-4:
			draw_circle(center, safedist)
		else:
			plt.plot(*center, 'o', color = "tab:purple", label = r"$R_{A,B}(s^*)$")
			plt.text(center[0]-0.01, center[1], r"$R_{A,B}(s^*)$", ha = "left", va = "top", fontsize = fontsize, color = "tab:purple", rotation = -30)

			collision = True


# curve def
cp = curve(ts)
plt.plot(*cp, label = r"$\gamma$", color = "tab:blue", linewidth=2)

# ray def
a = np.array((-0.82, 0))
b = np.array((1.82, 0.5))
plt.arrow(*a, *b, head_width = 0.02, edgecolor="tab:orange", facecolor = "tab:orange", label = r"$R_{A,B}$", width = 0.003)

# ray marching
visualize_ray_marching(a, b, cp)

# labels
plt.text(a[0], a[1]-0.01, r"$R_{A,B}$", ha = "right", va = "top", fontsize = fontsize, color = "tab:orange")

place = int(0.36*samples)
plt.text(cp[0][place], cp[1][place]-0.01, r"$\gamma$", ha = "right", va = "top", fontsize = fontsize, color = "tab:blue")


# plot
#plt.legend()
plt.axis('off')
plt.tight_layout()

plt.savefig("rayMarching.svg")
plt.show()