import numpy as np
from PIL import Image

filenames = ["51.png", "52.png", "53.png"]
outnames = ["61.png", "62.png", "63.png"]

for i in range(len(filenames)):
	with Image.open(filenames[i]) as inp:
		arr = np.array(inp)[5:-5,5:-5]
		out = Image.fromarray(arr)
		out.save(outnames[i])