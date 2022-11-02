import matplotlib.pyplot as plt
import numpy as np

def plot_points(points):
	xs = points[:,0]
	ys = points[:,1]

	plt.plot(xs, ys, 'x')

def curve_between_3_points(A, B, C, transition, t):
	if t < transition:
		return (transition-t)/transition * A + t/transition * B
	else:
		return (1-t)/(1-transition)*B + (t-transition)/(1-transition)*C

A = np.array([1,1])
B = np.array([2,2])
C = np.array([3,1])

vt = 0.8
ts = [0, vt, 1]

ps = np.array([curve_between_3_points(A, B, C, vt, t) for t in ts])
plot_points(ps)

plt.show()