import matplotlib.pyplot as plt
import matplotlib.markers as markers
import numpy as np

from matplotlib import rc
rc('text', usetex=True)

## General settings
fig, ax1 = plt.subplots(figsize=(5,5))
ax2 = ax1.twinx()

ax1.set_title(r"Comparison of $y_1$ and $y_2$ conditions")

color1 = "tab:orange"
color2 = "tab:blue"

ax1.set_ylabel(r'$y_1$', color = color1)
ax1.tick_params(axis='y', labelcolor = color1)

ax2.set_ylabel(r'$y_2$', color = color2)
ax2.tick_params(axis='y', labelcolor = color2)

ax1.set_xlabel(r'$x$')

## Data
x1 = np.array([0, 0.25, 0.5, 0.6, 0.9])
y1 = np.array([0, 0.10, 0.3, 0.65, 0.85])

x2 = np.array([0, 0.1, 0.3, 0.8])
y2 = np.array([0.8, 0.3, 0.1, 0])

## Plot data as scatter and line
s1 = ax1.scatter(x1, y1, marker = "D", color = color1)
ax1.plot(x1, y1, '--', marker = "*", color = color1)

s2 = ax2.scatter(x2, y2, color = color2)
ax2.plot(x2, y2, '--', color = color2)

## Legend
ax1.legend([s1, s2], [r"$y_1$", r"$y_2$"], loc = 'upper center')

plt.tight_layout()
plt.show()