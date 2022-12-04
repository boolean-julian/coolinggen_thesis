import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(10,4))
ax.set_xlim(-1, 2)
ax.set_aspect("equal", "box")
ax.axis("off")

def continuation(d1, d2, t):
	return 2*(d1-d2)*t**3 - 3*(d1-d2)*t**2 + d1

d1 = 0.5
d2 = 1

plt.axhline(d1, color = 'tab:blue', linestyle="--")
plt.axhline(d2, color = 'tab:blue', linestyle="--")

plt.axvline(0, color = 'tab:green', linestyle="--")
plt.axvline(1, color = 'tab:green', linestyle="--")

ts = np.linspace(0, 1, 100)
c3 = np.array([continuation(d1, d2, t) for t in ts])
plt.plot(ts, c3, color = 'tab:orange')

plt.show()