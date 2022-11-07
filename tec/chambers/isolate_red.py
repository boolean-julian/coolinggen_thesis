import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

image = np.asarray(Image.open("walls.png"))

for i in range(len(image)):
	for j in range(len(image[0])):
		tol = 10
		if image[i,j,1] - tol < image[i,j,0] and image[i,j,0] < image[i,j,1] + tol:
			image[i,j] = np.array([255,255,255])

image = image[780:1050]
image = image[:,280:550]

I = Image.fromarray(np.uint8(image))
I.save("only_walls.png")

fig, ax = plt.subplots(figsize=(5,5))
ax.imshow(image)
plt.show()