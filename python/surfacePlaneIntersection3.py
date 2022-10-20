import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

import numpy as np
from matplotlib import rc
rc('text', usetex=True)

up = np.linspace(0, 1, 64)
vp = np.linspace(0, 1, 64) 

xp = np.outer(up, np.ones_like(vp))*4-1
yp = np.outer(np.ones_like(up), vp)*4-1
zp = np.outer(np.zeros_like(up), np.zeros_like(vp))

Qnorm = np.array((0,0,-1))
Qproj = np.array((0,0,0))

S = np.array((1, 1, 0))
N = np.array((0, 0, -1.2))

fig = plt.figure(figsize=(8, 5))

ax = fig.add_subplot(111, projection='3d')
ax.set_box_aspect(aspect = (1,1,0.5))
ax.axis("off")

ax.plot_wireframe(xp, yp, zp, rstride=16, cstride=16, linewidth=0.8, color = "tab:orange")

ax.plot(*Qproj, 'ro')
dx = np.array((0, 0, +0.15))
ax.text(*(Qproj+dx), r"$Q_\textrm{proj}$")

ax.plot(*Qnorm, 'ro')
dx = np.array((-0.2, 0, -0.05))
ax.text(*(Qnorm+dx), r"$Q$")

ax.plot(*[[Qnorm[i], Qproj[i]] for i in range(len(Qnorm))], '--', color = "tab:blue")

ax.plot(*S, 'o', color = "tab:orange")
dx = np.array((0, 0, 0.15))
ax.text(*(S+dx), r"$S$")

#ax.quiver(*S, *N, color = "tab:orange")
ax.plot(*[[S[i], S[i]+N[i]] for i in range(len(S))], '-', color = "tab:orange")

ptri = np.array((+0.12, 0, 0.2))
mtri = np.array((-0.12, 0, 0.2))

triangle = [[S+N-dx, S+N+ptri, S+N+mtri]]
ax.add_collection(Poly3DCollection(triangle, facecolors="tab:orange"))

dx = np.array((0.08, 0, 0))
ax.text(*(S+0.38*N+dx), r"$N$")

ax.text(xp[-1,0], yp[-1,0], zp[-1,0]+0.15, r"$P_{S,N}$")

ax.plot(*[[S[i], Qnorm[i]] for i in range(len(S))], '--', color = "tab:blue")

#ax.set_xlim((-0.5, 3))
#ax.set_ylim((-2, 3))
#ax.set_zlim((-0.2, -0.25))

ax.view_init(30, 115, 180)
plt.tight_layout()

filenames = ["surfacePlaneIntersection3.png"]
plt.savefig(filenames[0], bbox_inches='tight', dpi = 500)

from PIL import Image

outnames = ["surfacePlaneIntersection3_cropped.png"]

for i in range(len(filenames)):
	with Image.open(filenames[i]) as inp:
		arr = np.array(inp)[700:-300,250:-200]
		out = Image.fromarray(arr)
		out.save(outnames[i])