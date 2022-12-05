import numpy as np
import matplotlib.pyplot as plt

def linear_interpolation(t, start, end):
	scale = end-start
	shift = start

	return scale*t + shift

def sigmoid(t, s):
	return 1/(1 + np.exp(-s*t))

def sigmoid_interpolation(t, start, end, s):
	scale = (end-start)
	shift = start

	return scale*sigmoid(t-0.5, s) + shift


ts = np.linspace(0, 1, 1000)

start = 4
end = 10

linear = linear_interpolation(ts, start, end)
sigmoid = sigmoid_interpolation(ts, start, end, 15)

plt.plot(ts, linear, label = "linear interpolation")
plt.plot(ts, sigmoid, label = "sigmoid interpolation")

plt.axhline(start, linestyle="--", color = "tab:red")
plt.axhline(end, linestyle="--", color = "tab:red")

plt.show()