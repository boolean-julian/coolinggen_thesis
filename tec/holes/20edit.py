import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as img

from matplotlib import rc
rc('text', usetex=True)

filenames = ["20.png", "21.png"]
outnames = ["20edit.png", "21edit.png"]

for i in range(len(filenames)):
	with Image.open(filenames[i]) as inp:
		arr = np.array(inp)[500:-500,5:-5]

		out = Image.fromarray(arr)
		out.save(outnames[i])

filenames = ["22.png"]
outnames = ["22edit.png"]

for i in range(len(filenames)):
	with Image.open(filenames[i]) as inp:
		arr = np.array(inp)[450:-350,20:-20]

		out = Image.fromarray(arr)
		out.save(outnames[i])
