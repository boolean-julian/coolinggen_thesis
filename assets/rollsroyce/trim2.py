import numpy as np
from PIL import Image

filenames = ["2022-12-06 23_13_31-crop-right-colorized-tec.png"]
outnames = ["11.png"]

for i in range(len(filenames)):
	with Image.open(filenames[i]) as inp:
		arr = np.array(inp)[5:-100,5:-5]
		out = Image.fromarray(arr)
		out.save(outnames[i])