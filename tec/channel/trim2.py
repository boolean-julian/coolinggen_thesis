import numpy as np
from PIL import Image

filenames = ["1.png", "2.png", "3.png", "4.png", "5.png"]
outnames = ["01.png", "02.png", "03.png", "04.png", "05.png"]

for i in range(len(filenames)):
	with Image.open(filenames[i]) as inp:
		arr = np.array(inp)[5:-5,5:-5]
		out = Image.fromarray(arr)
		out.save(outnames[i])