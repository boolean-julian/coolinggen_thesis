import matplotlib.pyplot as plt
import numpy as np
from scipy.special import comb

from matplotlib import rc
rc('text', usetex=True)

def bernstein_poly(k, n, t):
	return comb(n,k) * t**(n-k) * (1-t)**k

def bezier_curve(control_points, num_samples = 1000):
	num_control_points = len(control_points)
	x_control_points = [point[0] for point in control_points]
	y_control_points = [point[1] for point in control_points]
	
	ts = np.linspace(0, 1, num_samples)
	bernstein = [bernstein_poly(k, num_control_points-1, ts) for k in range(num_control_points)]

	x_bezier_points = np.dot(x_control_points, bernstein)
	y_bezier_points = np.dot(y_control_points, bernstein)

	bezier_points = [[x_bezier_points[i], y_bezier_points[i]] for i in range(num_samples)]

	return bezier_points

def plot_points(points, color, control = False):
	xs = [point[0] for point in points]
	ys = [point[1] for point in points]
	
	if control:
		plt.plot(xs, ys, 'o--', color=color, linewidth=2)
	else:
		plt.plot(xs, ys, color=color, linewidth=5)
		
fig, ax = plt.subplots(figsize=(10,3))

# First set
control_points = [[0,0], [1, 1]] # [[x1,y1],[x2,y2],...]
bezier_points = bezier_curve(control_points)

plot_points(bezier_points, "tab:orange")
plot_points(control_points, "tab:blue", control = True)

# Second set
control_points = [[2,0], [1, 0.5], [2,1]] # [[x1,y1],[x2,y2],...]
bezier_points = bezier_curve(control_points)

plot_points(bezier_points, "tab:orange")
plot_points(control_points, "tab:blue", control = True)

# Third set
control_points = [[2.5,0], [3.5, 0.2], [3.3, 1.1], [2.4, 0.9]] # [[x1,y1],[x2,y2],...]
bezier_points = bezier_curve(control_points)

plot_points(bezier_points, "tab:orange")
plot_points(control_points, "tab:blue", control = True)

plt.text(0.1, 0.4, r"$n = 1$", fontsize="large", ma="center")
plt.text(1.3, 0.8, r"$n = 2$", fontsize="large", ma="center")
plt.text(2.5, 0.15, r"$n = 3$", fontsize="large", ma="center")

plt.axis("off")
plt.savefig("bezierDifferentDegrees.svg")
plt.show()
