import matplotlib.pyplot as plt
import numpy as np

xn = 5
xlo = 0
xhi = 1

yn = 5
ylo = 0
yhi = 1

radius = 0.08

def draw_circle(center, radius):
	ts = np.linspace(0, 2*np.pi, 1000)

	xs = radius * np.cos(ts) + center[0]
	ys = radius * np.sin(ts) + center[1]

	plt.plot(xs, ys, "-", color = "black", lw=0.8)

def draw_aligned():
	for i in range(xn):
		for j in range(yn):
			xc = (xhi - xlo) * i/(xn-1) + xlo
			yc = (yhi - ylo) * j/(yn-1) + ylo

			center = np.array([xc, yc])
			draw_circle(center, radius)

def draw_staggered():
	for i in range(xn):
		for j in range(yn):

			xc = (xhi - xlo) * i/(xn-1) + xlo
			if i % 2 == 0:
				yc = (yhi - ylo) * j/(yn-1) + ylo
			elif (j+0.5 < yn-1):
				yc = (yhi - ylo) * (j+0.5)/(yn-1) + ylo

			center = np.array([xc, yc])
			draw_circle(center, radius)

fig, ax = plt.subplots(figsize=(5,5))
ax.set_aspect("equal", "box")
ax.axis("off")
ax.set_xlim(xlo-2*radius, xhi+2*radius)
ax.set_ylim(ylo-2*radius, yhi+2*radius)
draw_aligned()
plt.tight_layout()
plt.savefig("alignedstaggered_aligned.svg")
plt.show()

fig, ax = plt.subplots(figsize=(5,5))
ax.set_aspect("equal", "box")
ax.axis("off")
ax.set_xlim(xlo-2*radius, xhi+2*radius)
ax.set_ylim(ylo-2*radius, yhi+2*radius)
draw_staggered()
plt.tight_layout()
plt.savefig("alignedstaggered_staggered.svg")
plt.show()
