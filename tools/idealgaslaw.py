import matplotlib.pyplot as plt
import numpy as np

num_samples = 100

moles = 100 # mol
universal_gas_constant = 8.314 # J/(mol K)

def temperature(pressure, volume):
	return (pressure * volume) / (moles * universal_gas_constant)

pressure_atmosphere = 100000 # Pa
pressure_delta = 80000 # Pa
pressures = np.linspace(pressure_atmosphere - pressure_delta, pressure_atmosphere + pressure_delta, num_samples)
volumes = np.linspace(0.5, 10, num_samples) # m^3

X, Y = np.meshgrid(pressures, volumes)
Z = temperature(X, Y)

fig, ax = plt.subplots()

contour = plt.contour(X,Y,Z, levels = 20, colors='k')

contour.levels = [int(c) for c in contour.levels]
ax.clabel(contour, fmt=r'%r K')
ax.set_xlabel("Pressure / Pa")
ax.set_ylabel("Volume / m³")
ax.set_title("Ideal gas law isothermics")

plt.show()