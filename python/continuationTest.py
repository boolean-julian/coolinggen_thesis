import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc
rc('text', usetex=True)

fig, ax = plt.subplots(figsize=(6,4))
ax.set_xlim(-0.5, 1.5)
ax.set_aspect("equal", "box")
ax.axis("off")

def continuation(d1, d2, t):
	return 2*(d1-d2)*t**3 - 3*(d1-d2)*t**2 + d1

d1 = 1
d2 = 0

plt.axhline(d1, color = 'tab:blue', linestyle="--")
plt.axhline(d2, color = 'tab:green', linestyle="--")


plt.text(-0.33, d1+0.05, r"$d_1$", color = "tab:blue", fontsize=25)
plt.text(1.2, d2-0.15, r"$d_2$", color = "tab:green", fontsize=25)
plt.text(0.55, 0.55, r"$f(t)$", color = "tab:orange", fontsize=25)

plt.axvline(0, color = 'black')
plt.axvline(1, color = 'black')

ts = np.linspace(0, 1, 100)
c3 = np.array([continuation(d1, d2, t) for t in ts])
plt.plot(ts, c3, '--', color = 'tab:orange')

plt.savefig("alignmentOffset.svg")
plt.show()