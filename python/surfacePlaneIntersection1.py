import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from matplotlib import rc
rc('text', usetex=True)

def rotate(x, y, z, theta):
	xr = x
	yr = np.cos(theta)*y - np.sin(theta)*z
	zr = np.sin(theta)*y + np.cos(theta)*z

	return xr, yr, zr

# Draw sphere
us = np.linspace(0, 1, 64)
vs = np.linspace(0, 1, 64)

xs = np.outer(np.sin(np.pi*us), np.cos(2*np.pi*vs))
ys = np.outer(np.sin(np.pi*us), np.sin(2*np.pi*vs))
zs = np.outer(np.cos(np.pi*us), np.ones_like(us))


# draw circle
tc = np.linspace(0, 1, 1000)
xc = np.cos(2*np.pi*tc)*0.79
yc = np.sin(2*np.pi*tc)*0.79
zc = np.zeros_like(tc)+0.6

theta = np.pi/8
xc, yc, zc = rotate(xc, yc, zc, theta)

# draw plane
up = np.linspace(0, 1, 64)
vp = np.linspace(0, 1, 64)

xp = 2.5*np.outer(us, np.ones_like(vs))-1.25
yp = 2.5*np.outer(np.ones_like(us), vs)-1.25
zp = np.outer(np.zeros_like(us), np.zeros_like(vs))+0.6

xp, yp, zp = rotate(xp, yp, zp, theta)

# plot
fig = plt.figure(figsize=(8,2.8))

# sub 1
ax = fig.add_subplot(131, projection='3d')
ax.set_box_aspect(aspect = (1.25,1.25,1))
ax.axis("off")
ax.view_init(30, -50)
ax.plot_wireframe(xs, ys, zs, rstride=4, cstride=4, linewidth=0.5)
ax.plot(xc, yc, zc, color="tab:orange", linewidth = 3)
ax.plot_wireframe(xp, yp, zp, rstride=16, cstride=16, linewidth=0.5, color = "grey")

ax = fig.add_subplot(132, projection='3d')
ax.set_box_aspect(aspect = (1.25,1.25,1))
ax.axis("off")
ax.view_init(90, 200)
ax.plot_wireframe(xs, ys, zs, rstride=4, cstride=4, linewidth=0.5)
ax.plot(xc, yc, zc, color="tab:orange", linewidth = 3)
ax.plot_wireframe(xp, yp, zp, rstride=16, cstride=16, linewidth=0.5, color = "grey")

ax = fig.add_subplot(133, projection='3d')
ax.set_box_aspect(aspect = (1.25,1.25,1))
ax.axis("off")
ax.view_init(-5, 30)
ax.plot_wireframe(xs, ys, zs, rstride=4, cstride=4, linewidth=0.5)
ax.plot(xc, yc, zc, color="tab:orange", linewidth = 3)
ax.plot_wireframe(xp, yp, zp, rstride=16, cstride=16, linewidth=0.5, color = "grey")



plt.tight_layout()
filenames = ["surfacePlaneIntersection1_whole.png"]
plt.savefig(filenames[0], bbox_inches='tight', dpi = 500)

from PIL import Image

outnames = ["surfacePlaneIntersection1_cropped.png"]

for i in range(len(filenames)):
	with Image.open(filenames[i]) as inp:
		arr = np.array(inp)[100:-200,150:-150]
		out = Image.fromarray(arr)
		out.save(outnames[i])