import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import numpy as np
from matplotlib import rc
rc('text', usetex=True)

# Draw surface
us = np.linspace(0, 1, 64)
vs = np.linspace(0, 1, 64)

xs = np.outer(us, np.ones_like(vs))*2-1
ys = np.outer(np.ones_like(us), vs)*2-1
zs = xs*xs + ys*ys

# Draw tangent plane
up = np.linspace(0, 1, 64)
vp = np.linspace(0, 1, 64)

xp = np.outer(up, np.ones_like(vp))*2-1
yp = np.outer(np.ones_like(up), vp)*2-1
zp = np.outer(np.zeros_like(up), np.zeros_like(vp))

# Draw intersection plane
ui = np.linspace(0, 1, 64)
vi = np.linspace(0, 1, 64)

xi = np.outer(ui, np.ones_like(vi))*2-1
zi = np.outer(np.ones_like(ui), vi)*2-1
yi = np.outer(np.zeros_like(ui), np.zeros_like(vi))

# Normals
origin = (0,0,0)
n_tangent = (0,0,-1)
n_plane = (0,1,0)

n_line = np.cross(n_tangent, n_plane)

# Intersection close line
ts = np.linspace(-1, 1, 5)
xl = origin[0] + ts * n_line[0]
yl = origin[1] + ts * n_line[1]
zl = origin[2] + ts * n_line[2]


# Intersection
tc = np.linspace(0, 1, 100)
xc = 2*tc-1
yc = np.zeros_like(tc)
zc = xc*xc

# Plot
fig = plt.figure(figsize=(10, 5))

# Sub 1
ax = fig.add_subplot(121, projection='3d')
ax.set_box_aspect(aspect = (1,1,np.sqrt(2)))
ax.axis("off")

ax.plot_wireframe(xs, ys, zs, rstride=16, cstride=16, linewidth=0.8, color = "tab:blue")
ax.plot_wireframe(xp, yp, zp, rstride=16, cstride=16, linewidth=0.8, color = "tab:orange")
ax.quiver(*origin, *n_tangent, color = "tab:orange", lw=2)

ax.plot_wireframe(xi, yi, zi, rstride=16, cstride=16, linewidth=0.8, color = "tab:green")
ax.quiver(*origin, *n_plane, color="tab:green", lw=2)

ax.plot(xl, yl, zl, "black")

ax.plot(xc, yc, zc, "--", color = "black")
ax.plot(*origin, 'ro')

ax.view_init(30, 215, 180)

# Sub 3
ax = fig.add_subplot(122, projection='3d')
ax.set_box_aspect(aspect = (1,1,np.sqrt(2)))
ax.axis("off")

ax.plot_wireframe(xs, ys, zs, rstride=16, cstride=16, linewidth=0.8, color = "tab:blue")
ax.plot_wireframe(xp, yp, zp, rstride=16, cstride=16, linewidth=0.8, color = "tab:orange")
ax.quiver(*origin, *n_tangent, color = "tab:orange", lw=2)

ax.plot_wireframe(xi, yi, zi, rstride=16, cstride=16, linewidth=0.8, color = "tab:green")
ax.quiver(*origin, *n_plane, color="tab:green", lw=2)

ax.plot(xl, yl, zl, "black")

ax.plot(xc, yc, zc, "--", color = "black")
ax.plot(*origin, 'ro')

ax.view_init(30, 145, 180)

plt.tight_layout()
plt.savefig("argh2.svg")
plt.show()

"""
for a in range(360):
	ax.view_init(30, a, 180)
	plt.draw()
	plt.pause(.001)
"""