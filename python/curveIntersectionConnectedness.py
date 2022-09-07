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


ts = np.linspace(0, 1, 1000)
tria = triangle(ts)
sine = sine(ts)

tria_indices, sine_indices = get_intersections(tria, sine)


fig, ax = plt.subplots(1, 2, figsize = (16, 9))

ax[0].plot(tria, ts, label=r"\gamma_1(s)")
ax[0].plot(sine, ts)

ax[0].plot(tria[tria_indices], ts[tria_indices], 'ro')
#ax[0].plot(sine[sine_indices], ts[sine_indices], 'ro')

for i in range(len(tria_indices)):
	if (i%2 != 0):
		dx = -0.02
		dy = -0.01
		va = "top"
		ha = "right"

	else:
		dx = 0.02
		dy = -0.01
		va = "top"
		ha = "left"



	s = r'$\gamma_1(s_{{{n}}}) = \gamma_2(t_{{{n}}})$'.format(n=i)

	ax[0].text(tria[tria_indices[i]]+dx, ts[tria_indices[i]]+dy, s, va=va, ha=ha)

ax[0].axis("off")

ax[1].plot(ts[tria_indices], ts[sine_indices], 'ro')
ax[1].set_xlabel(r"$s$ of $\gamma_1(s)$")
ax[1].set_ylabel(r"$t$ of $\gamma_2(t)$")

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
		

	ax[1].text(ts[tria_indices[i]]+dx, ts[sine_indices[i]]+dy, s, va=va, ha=ha)

plt.show()