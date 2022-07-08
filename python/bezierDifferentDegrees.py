import matplotlib.pyplot as plt
import numpy as np
from scipy.special import comb

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
		
fig, ax = plt.subplots()

control_points = [[0.1,0], [0,0.9], [1,1]] # [[x1,y1],[x2,y2],...]
bezier_points = bezier_curve(control_points)

plot_points(bezier_points, "tab:orange")
plot_points(control_points, "tab:blue", control = True)

control_points = [[0.4,0.1], [0.8, 0.1], [1, 0.5], [0.7, 0.8]] # [[x1,y1],[x2,y2],...]
bezier_points = bezier_curve(control_points)

plot_points(bezier_points, "tab:orange")
plot_points(control_points, "tab:blue", control = True)

control_points = [[0.2,0.25], [0.6, 0.75]] # [[x1,y1],[x2,y2],...]
bezier_points = bezier_curve(control_points)

plot_points(bezier_points, "tab:orange")
plot_points(control_points, "tab:blue", control = True)

plt.text(0.08, 0.7, "n = 3", fontsize="large", ma="center")
plt.text(0.28, 0.5, "n = 2", fontsize="large", ma="center")
plt.text(0.7, 0.4, "n = 1", fontsize="large", ma="center")

plt.axis("off")
ax.margins(0.02)

#plt.show()
plt.savefig("bezierDifferentDegrees.svg")