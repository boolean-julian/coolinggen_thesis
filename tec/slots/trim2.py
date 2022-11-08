import numpy as np
from PIL import Image

filenames = ["01.png", "02.png", "04.png", "05.png", "06.png", "07.png", "08.png"]
outnames = ["11.png", "12.png", "14.png", "15.png", "16.png", "17.png", "18.png"]

for i in range(len(filenames)):
	with Image.open(filenames[i]) as inp:
		arr = np.array(inp)[5:-5,5:-5]
		out = Image.fromarray(arr)
		out.save(outnames[i])