import numpy as np
import matplotlib.pyplot as plt

axisSupport = np.array([0,0])
axisDirection = np.array([0,1])


def bernsteinPoly(k, n, t):
	comb = np.math.factorial(n)/(np.math.factorial(k)*np.math.factorial(n-k))
	return comb * t**(n-k) * (1-t)**k

def bezierCurve(control_points, num_samples = 100):
	num_control_points = len(control_points)
	x_control_points = [point[0] for point in control_points]
	y_control_points = [point[1] for point in control_points]
	
	ts = np.linspace(0, 1, num_samples)
	bernstein = [bernsteinPoly(k, num_control_points-1, ts) for k in range(num_control_points)]

	x_bezier_points = np.dot(x_control_points, bernstein)
	y_bezier_points = np.dot(y_control_points, bernstein)

	bezier_points = [[x_bezier_points[i], y_bezier_points[i]] for i in range(num_samples)]

	return np.array(bezier_points)

def plotAxis():
	points = np.array([axisSupport, axisSupport+axisDirection])
	plt.plot(*points.T)

def plotPoints(points):
	plt.plot(*points.T, 'x')

endPoint = axisSupport + axisDirection
controlPoints0 = [axisSupport, np.array([0.5,0.2]), endPoint]
curvePoints0 = bezierCurve(controlPoints0)

controlPoints1 = [axisSupport, np.array([0.3, -0.3]), np.array([0.3, 1.3]), endPoint]
curvePoints1 = bezierCurve(controlPoints1)

plotAxis()
plotPoints(curvePoints0)
plotPoints(curvePoints1)

plt.show()