import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc
rc('text', usetex=True)

def triangle(s):
	freq = 1.5
	m = 0
	for i in range(10):
		n = 2*i+1
		m += (-1)**i * n**(-2) * np.sin(2*np.pi*n*freq*s)

	return np.abs(6/(np.pi**2)*m)-0.05*s

def sine(s):
	return 0.2*np.cos(1.3*np.pi*s)+0.4+0.05*s


def get_intersections(arr1, arr2):	
	distances = np.zeros((len(arr1), len(arr2)))
	for i in range(len(arr1)):
		for j in range(len(arr2)):
			distances[i, j] = np.sqrt((arr1[i] - arr2[j])**2 + (ts[i] - ts[j])**2)

	argmins = [[],[]]
	for i in range(1,len(arr1)-1):
		for j in range(1,len(arr2)-1):
			if (distances[i+1,j] > distances[i,j] and distances[i-1,j] > distances[i,j] and distances[i,j+1] > distances[i,j] and distances[i,j-1] > distances[i,j]):
				argmins[0].append(i)
				argmins[1].append(j)

	ind1 = np.array(argmins[0], dtype=int)
	ind2 = np.array(argmins[1], dtype=int)

	
	print(ind1, ind2)
	print(distances[ind1,ind2])

	tolerance = 0.0025
	for i in range(len(ind1)):
		if distances[ind1[i], ind2[i]] > tolerance:
			ind1[i] = -1
			ind2[i] = -1
	ind1 = ind1[ind1 >= 0]
	ind2 = ind2[ind2 >= 0]

	for i in range(len(ind1)-1):
		if ind1[i+1] -1 <= ind1[i] and ind1[i] <= ind1[i+1] + 1:
			ind1[i] = -1
			ind2[i] = -1

		if ind2[i+1] -1 <= ind2[i] and ind2[i] <= ind2[i+1] + 1:
			ind1[i] = -1
			ind2[i] = -1

	ind1 = ind1[ind1 >= 0]	
	ind2 = ind2[ind2 >= 0]
	

	print(ind1, ind2)
	print(distances[ind1,ind2])


	return ind1, ind2


### SINGLETON INTERSECTIONS

ts = np.linspace(0, 1, 1000)
tria = triangle(ts)
sine = sine(ts)

tria_indices, sine_indices = get_intersections(tria, sine)


fig, ax = plt.subplots(1, 4, figsize = (12, 3))
ax = ax.reshape((2,2))

ax[0,0].plot(tria, ts, label=r"$\gamma_1$")
ax[0,0].plot(sine, ts, label=r"$\gamma_2$")

ax[0,0].plot(tria[tria_indices], ts[tria_indices], 'ro', label="$V(\gamma_1, \gamma_2)$")

#ax[0].plot(sine[sine_indices], ts[sine_indices], 'ro')

for i in range(len(tria_indices)):
	if (i%2 != 0):
		dx = -0.02
		dy = -0.01
		va = "top"
		ha = "right"

	else:
		dx = 0.03
		dy = -0.01
		va = "top"
		ha = "left"



	s = r'$\gamma_1(s_{{{n}}}) = \gamma_2(t_{{{n}}})$'.format(n=i)

	ax[0,0].text(tria[tria_indices[i]]+dx, ts[tria_indices[i]]+dy, s, va=va, ha=ha)

ax[0,1].plot(ts[tria_indices], ts[sine_indices], 'ro')
ax[0,1].set_xlabel(r"$s$ of $\gamma_1(s)$")
ax[0,1].set_ylabel(r"$t$ of $\gamma_2(t)$")

for i in range(len(tria_indices)):

	s = r'$(s_{{{n}}}, t_{{{n}}})$'.format(n=i)
	
	if i < 2:
		dx = 0.02
		dy = 0.01
		va = "bottom"
		ha = "left"
	else:
		dx = -0.02
		dy = -0.01
		va = "top"
		ha = "right"
		

	ax[0,1].text(ts[tria_indices[i]]+dx, ts[sine_indices[i]]+dy, s, va=va, ha=ha)


### INTERVAL INTERSECTIONS

c1points = [(0,0), (0.5,0.3), (0.5,0.7), (1, 1)]
c2points = [(1,0), (0.5,0.3), (0.5,0.7), (0, 1)]

def drawpoints(points, a, color, dashmid=False):
	xs = [point[0] for point in points]
	ys = [point[1] for point in points]


	for i in range(len(xs)-1):
		if i == 1 and dashmid:
			a.plot(xs[i:i+2], ys[i:i+2], '--', color=color)
		else:
			a.plot(xs[i:i+2], ys[i:i+2], '-', color=color)

def drawdelimiter(point, direction, width, height, a):
	xs = point[0]
	ys = point[1]

	direction = direction/np.linalg.norm(direction)

	dx = +height*direction[0]
	dy = +height*direction[1]

	nx = -width*direction[1]
	ny = +width*direction[0]

	points = [(xs-nx+dx, ys-ny+dy), (xs-nx, ys-ny), (xs+nx, ys+ny), (xs+nx+dx, ys+ny+dy)]
	drawpoints(points, a, 'r', False)

width = 0.03
height = 0.01
drawpoints(c1points, ax[1,0], "tab:orange", False)
drawpoints(c2points, ax[1,0], "tab:blue", True)
drawdelimiter(c1points[1], (0,+1), width, height, ax[1,0])
drawdelimiter(c2points[2], (0,-1), width, height, ax[1,0])


dx = 0.05
ax[1,0].text(c1points[1][0]+dx, c1points[1][1]+dy, r"$\gamma_1(s_1) = \gamma_2(t_2)$")
ax[1,0].text(c1points[2][0]+dx, c2points[2][1]+dy, r"$\gamma_1(s_2) = \gamma_2(t_1)$")



width = 0.01
height = 0.003

ipoints = [(0.3,0.7), (0.7,0.3)]
direction2 = (ipoints[0][0] - ipoints[1][0], ipoints[0][1] - ipoints[1][1])
direction1 = (ipoints[1][0] - ipoints[0][0], ipoints[1][1] - ipoints[0][1])
drawpoints(ipoints, ax[1,1], "tab:red", False)
drawdelimiter(ipoints[0], direction1, width, height, ax[1,1])
drawdelimiter(ipoints[1], direction2, width, height, ax[1,1])

dx = 0.02
ax[1,1].text(ipoints[0][0]+dx, ipoints[0][1]+dy, r"$(s_1, t_2)$")

dx = -0.1
ax[1,1].text(ipoints[1][0]+dx, ipoints[1][1]+dy, r"$(s_2, t_1)$")


ax[1,1].set_xlabel(r"$s$ of $\gamma_1(s)$")
ax[1,1].set_ylabel(r"$t$ of $\gamma_2(t)$")


ax[0,1].set_aspect("equal", "box")
ax[1,1].set_aspect("equal", "box")

ax[0,0].axis("off")
ax[1,0].axis("off")

ax[0,0].set_title("(A)", loc="left", weight="bold")
#ax[0,1].set_title("(A2)", loc="left", weight="bold")
ax[1,0].set_title("(B)", loc="left", weight="bold")
#ax[1,1].set_title("(B2)", loc="left", weight="bold")


plt.tight_layout()

plt.savefig("curveIntersectionConnectedness.svg")
plt.show()


