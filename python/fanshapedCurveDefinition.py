import matplotlib.pyplot as plt
import numpy as np

from matplotlib import rc
rc('text', usetex=True)

r = 1
d = 1.25
b = 1.5


def get_fanshaped_point(t):
	t = (t+1)%1

	if t == 0:
		x = r
		y = 0
	elif t < 0.25:
		x = r*np.cos(2*np.pi*t)
		y = r*np.sin(2*np.pi*t) + 1*(b-r)
	elif t == 0.25:
		x = 0
		y = b
	elif t < 0.5:
		x = r*np.cos(2*np.pi*t) - 2*(d-r)
		y = r*np.sin(2*np.pi*t) + 1*(b-r)
	elif t == 0.5:
		x = r-2*d
		y = 0
	elif t < 0.75:
		x = r*np.cos(2*np.pi*t) - 2*(d-r)
		y = r*np.sin(2*np.pi*t) - 1*(b-r)
	elif t == 0.75:
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

def make_plottable(function, lo, hi):
	samples = 1000
	ts = np.linspace(lo, hi, samples)
	fs = [function(t) for t in ts]
	xs = [f[0] for f in fs]
	ys = [f[1] for f in fs]

	return xs, ys


# fan shape
dt = .0001
xf1, yf1 = make_plottable(get_fanshaped_point, 0.00+dt, 0.25-dt)
xf2, yf2 = make_plottable(get_fanshaped_point, 0.25+dt, 0.50-dt)
xf3, yf3 = make_plottable(get_fanshaped_point, 0.50+dt, 0.75-dt)
xf4, yf4 = make_plottable(get_fanshaped_point, 0.75+dt, 1.00-dt)

xg1, yg1 = make_plottable(get_fanshaped_point, 0.00+0., 0.00+dt)
xg2, yg2 = make_plottable(get_fanshaped_point, 0.25-dt, 0.25+dt)
xg3, yg3 = make_plottable(get_fanshaped_point, 0.50-dt, 0.50+dt)
xg4, yg4 = make_plottable(get_fanshaped_point, 0.75-dt, 0.75+dt)
xg5, yg5 = make_plottable(get_fanshaped_point, 1.00-dt, 1.00+0.)



# Circle
xc, yc = make_plottable(get_circle_point, 0, 1)

# Fanshaped curve corner circle
xcc = [x + 2*r-2*d for x in xc]
ycc = [y + b-r for y in yc]


fig, ax = plt.subplots(figsize=(5,5))
ax.set_aspect("equal", "box")



plt.plot(xcc, ycc, "--", color = "tab:green")

plt.plot(xf1, yf1, "tab:blue", label = "Outer curve")
plt.plot(xf2, yf2, "tab:blue", label = "Outer curve")
plt.plot(xf3, yf3, "tab:blue", label = "Outer curve")
plt.plot(xf4, yf4, "tab:blue", label = "Outer curve")

plt.plot(xg1, yg1, linestyle="dotted", color="tab:blue", label = "Outer curve")
plt.plot(xg2, yg2, linestyle="dotted", color="tab:blue", label = "Outer curve")
plt.plot(xg3, yg3, linestyle="dotted", color="tab:blue", label = "Outer curve")
plt.plot(xg4, yg4, linestyle="dotted", color="tab:blue", label = "Outer curve")
plt.plot(xg5, yg5, linestyle="dotted", color="tab:blue", label = "Outer curve")

plt.plot(*get_fanshaped_point(0.00), 'o', color = "tab:blue")
plt.plot(*get_fanshaped_point(0.25), 'o', color = "tab:blue")
plt.plot(*get_fanshaped_point(0.50), 'o', color = "tab:blue")
plt.plot(*get_fanshaped_point(0.75), 'o', color = "tab:blue")

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
make_arrow_one_sided(0, 0, r, 0, r"$r$", offset, "tab:orange")

# Circle radius in corners of fanshaped curve
#make_arrow(0, b-r, r/np.sqrt(2), r/np.sqrt(2), "r", offset, "tab:blue")
make_arrow_one_sided(2*r-2*d, b-r, -r/np.sqrt(2), r/np.sqrt(2), r"$r$", offset, "tab:blue")
#make_arrow(0, r-b, r/np.sqrt(2), -r/np.sqrt(2), "r", offset, "tab:blue")
#make_arrow(2*r-2*d, r-b, -r/np.sqrt(2), -r/np.sqrt(2), "r", offset, "tab:blue")

# Size of fanshaped curve
make_arrow_two_sided(r-2*d-offset, -b, 0, 2*b, r"$2b$", offset, "tab:green")
make_arrow_two_sided(r, -b-offset, -2*d, 0, r"$2d$", -1.3*offset, "tab:green")


plt.axis("off")
#plt.legend(loc = "upper right")

plt.tight_layout()
plt.savefig("fanshapedCurveDefinition.svg")
plt.show()