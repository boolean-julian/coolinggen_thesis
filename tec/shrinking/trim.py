import numpy as np
from PIL import Image

filenames = ["01.png", "02.png", "03.png"]
outnames = ["11.png", "12.png", "13.png"]

for i in range(len(filenames)):
	with Image.open(filenames[i]) as inp:
		arr = np.array(inp)[200:-240,400:-350]
		out = Image.fromarray(arr)
		out.save(outnames[i])