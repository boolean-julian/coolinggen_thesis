import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as img

from matplotlib import rc
rc('text', usetex=True)

filenames = ["00.png", "01.png"]
outnames = ["00edit.png", "01edit.png"]

for i in range(len(filenames)):
	with Image.open(filenames[i]) as inp:
		arr = np.array(inp)[50:-50,5:-1600]

		out = Image.fromarray(arr)
		out.save(outnames[i])


fs = 20

for f in outnames:
	fig, ax = plt.subplots(figsize=(6,11))

	image = img.imread(f)
	plt.imshow(image)

	plt.text(580, 200, r"$B(u_B, v_B)$", color = "blue", fontsize = fs)
	plt.text(580, 2400, r"$C(u_C, v_C)$", color = "blue", fontsize = fs)
	plt.text(940, 1300, r"$F_2(u, v_\textrm{transition})$", color = "red", fontsize = fs)

	plt.text(1150, 260, r"$f_B$", fontsize = fs);
	plt.text(960, 2360, r"$f_C$", fontsize = fs);

	ax.axis("off")

	plt.tight_layout()
	plt.savefig(f)

	#plt.show()


outnames = ["00edit.png", "01edit.png"]
for i in range(len(outnames)):
	with Image.open(outnames[i]) as inp:
		arr = np.array(inp)[100:-50,:]

		out = Image.fromarray(arr)
		out.save(outnames[i])