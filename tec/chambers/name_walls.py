import matplotlib.pyplot as plt
from PIL import Image

from matplotlib import rc
rc('text', usetex=True)

image = Image.open("walls.png")

fig, ax = plt.subplots(figsize=(10,10))

ax.axis("off")
ax.imshow(image)

def labeled_point(x, y, dx, dy, text, c = "red"):
	ax.plot(x, y, 'o', color = c)
	ax.text(x+dx, y+dy, text, fontsize=18, color = c)

def label(x, y, text):
	ax.text(x, y, text, fontsize = 18)

labeled_point(301, 842, -15, -15, r"$$p_1^+$$")
labeled_point(421, 792, -20, -15, r"$$p_2^+$$")

labeled_point(302, 1029, -20, 30, r"$$p_1^-$$")
labeled_point(528, 903, 5, 20, r"$$p_2^-$$")

label(730, 100, r"$$P^{(v_i)}_\textrm{stream}$$")
label(620, 620, r"$$S^{(v_i)}_\textrm{stream}$$")

labeled_point(302, 935, 10, 35, r"$$c^{(v_i)}(w_1)$$", c="blue")
labeled_point(479, 854, -110, 10, r"$$c^{(v_i)}(w_2)$$", c="blue")

def labeled_arrow(xs, ys, xt, yt, dx, dy, text, c = "blue"):
	ax.arrow(xs, ys, xt-xs, yt-ys, head_width=13, length_includes_head=True, edgecolor=c, facecolor=c,  ls = "--")
	ax.text(xs+dx, ys+dy, text, fontsize=18, color = c)


labeled_arrow(100, 600, 302, 935, 0, -5, r"$$\omega_1 = \frac{{\pi}}{{2}}$$")
labeled_arrow(800, 800, 479, 854, 5, 0, r"$$\omega_2 = \frac{{\pi}}{{2}}$$")



plt.tight_layout()
#plt.show()
plt.savefig("walls_labeled.svg")