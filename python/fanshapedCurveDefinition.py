import matplotlib.pyplot as plt
import numpy as np

r = 1
d = 1.25
b = 1.5

def get_fanshaped_point(t):
	t = (t+1)%1

	quarter = 0.25
	if t == 0:
		x = r
		y = 0
	elif t < 1*quarter:
		x = r*np.cos(2*np.pi*t)
		y = r*np.sin(2*np.pi*t) + 1*(b-r)
	elif t == 1*quarter:
		x = 0
		y = b
	elif t < 2*quarter:
		x = r*np.cos(2*np.pi*t) - 2*(d-r)
		y = r*np.sin(2*np.pi*t) + 1*(b-r)
	elif t == 2*quarter:
		x = r-2*d
		y = 0
	elif t < 3*quarter:
		x = r*np.cos(2*np.pi*t) - 2*(d-r)
		y = r*np.sin(2*np.pi*t) - 1*(b-r)
	elif t == 3*quarter:
		x = 0
		y = -b
	elif t < 1:
		x = r*np.cos(2*np.pi*t)
		y = r*np.sin(2*np.pi*t) - 1*(b-r)

	return x, y

def get_circle_point(t):
	x = r*np.cos(2*np.pi*t)
	y = r*np.sin(2*np.pi*t)

	return x, y

def make_plottable(function):
	samples = 1000
	ts = np.linspace(0, 1, samples)
	fs = [function(t) for t in ts]
	xs = [f[0] for f in fs]
	ys = [f[1] for f in fs]

	return xs, ys

xf, yf = make_plottable(get_fanshaped_point)
xc, yc = make_plottable(get_circle_point)

fig, ax = plt.subplots(figsize=(5,5))
ax.set_aspect("equal", "box")

plt.plot(xf, yf, "tab:blue", label = "Outer curve")
plt.plot(xc, yc, "tab:orange", label = "Inner curve")

# Circle aligned grid
"""
plt.axhline(0, color = "gray", alpha = 0.5)
plt.axhline(r, color = "gray", alpha = 0.5)
plt.axhline(-r, color = "gray", alpha = 0.5)

plt.axvline(0, color = "gray", alpha = 0.5)
plt.axvline(r, color = "gray", alpha = 0.5)
plt.axvline(-r, color = "gray", alpha = 0.5)

# Fanshaped aligned grid
plt.axhline(-b, color = "gray", alpha = 0.5)
plt.axhline(b, color = "gray", alpha = 0.5)

plt.axvline(2*r-2*d, color = "gray", alpha = 0.5)
plt.axvline(r-2*d, color = "gray", alpha = 0.5)

plt.axhline(b-r, color = "gray", alpha = 0.5)
plt.axhline(r-b, color = "gray", alpha = 0.5)
"""

# Arrows
width = 0.005
head_width = 10*width

def make_arrow_two_sided(x, y, dx, dy, label, offset, color = "gray"):
	xm = x+dx/2
	ym = y+dy/2

	plt.arrow(xm, ym, dx/2, dy/2, width=width, head_width = head_width, length_includes_head = True, color = color)
	plt.arrow(xm, ym, -dx/2, -dy/2, width=width, head_width = head_width, length_includes_head = True, color = color)

	if dx != 0:
		phi = np.arctan(dy/dx)
	else:
		phi = np.pi/2
	phi = phi*180/np.pi

	xt = xm - np.sin(phi)*offset
	yt = ym + np.cos(phi)*offset

	plt.text(xt, yt, label, horizontalalignment='center', verticalalignment='center', rotation = phi)


def make_arrow_one_sided(x, y, dx, dy, label, offset, color = "gray"):
	xm = x+dx/2
	ym = y+dy/2

	plt.plot(x, y, 'o', color = color)
	plt.arrow(x, y, dx, dy, width=width, head_width = head_width, length_includes_head = True, color = color)
	
	if dx != 0:
		phi = np.arctan(dy/dx)
	else:
		phi = np.pi/2
	phi = phi*180/np.pi

	xt = xm - np.sin(phi)*offset
	yt = ym + np.cos(phi)*offset

	plt.text(xt, yt, label, horizontalalignment='center', verticalalignment='center', rotation = phi)




offset = 0.06
# Circle radius
make_arrow_one_sided(0, 0, r, 0, "r", offset, "tab:orange")

# Circle radius in corners of fanshaped curve
#make_arrow(0, b-r, r/np.sqrt(2), r/np.sqrt(2), "r", offset, "tab:blue")
make_arrow_one_sided(2*r-2*d, b-r, -r/np.sqrt(2), r/np.sqrt(2), "r", offset, "tab:blue")
#make_arrow(0, r-b, r/np.sqrt(2), -r/np.sqrt(2), "r", offset, "tab:blue")
#make_arrow(2*r-2*d, r-b, -r/np.sqrt(2), -r/np.sqrt(2), "r", offset, "tab:blue")

# Size of fanshaped curve
make_arrow_two_sided(r-2*d-offset, -b, 0, 2*b, "2b", offset, "tab:green")
make_arrow_two_sided(r, -b-offset, -2*d, 0, "2d", -1.3*offset, "tab:green")

# Fanshaped curve corner circle
xcc = [x + 2*r-2*d for x in xc]
ycc = [y + b-r for y in yc]
plt.plot(xcc, ycc, "--", color = "tab:blue")

plt.axis("off")
#plt.legend(loc = "upper right")


plt.savefig("fanshapedCurveDefinition.svg")


plt.show()