import numpy as np
from PIL import Image

filenames = ["51.png", "52.png", "71.png", "72.png", "73.png", "101.png", "102.png", "103.png", "104.png"]
outnames = ["61.png", "62.png", "81.png", "82.png", "83.png", "111.png", "112.png", "113.png", "114.png"]

for i in range(len(filenames)):
	with Image.open(filenames[i]) as inp:
		arr = np.array(inp)[5:-5,5:-5]
		out = Image.fromarray(arr)
		out.save(outnames[i])