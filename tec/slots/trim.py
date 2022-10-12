import numpy as np
from PIL import Image

filenames = ["oha.png"]
outnames = ["oha_trimmed.png"]

for i in range(len(filenames)):
	with Image.open(filenames[i]) as inp:
		arr = np.array(inp)[5:-5,5:-5]
		out = Image.fromarray(arr)
		out.save(outnames[i])