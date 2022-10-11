import matplotlib.pyplot as plt
import matplotlib.image as img

fc = "white"

fig, ax = plt.subplots(figsize=(8,8))
image = img.imread("wu_naca_s2.png")



hide = dict(facecolor=fc, edgecolor='none', boxstyle='round,pad=0.1')
bbox = dict(facecolor=fc, edgecolor='none', boxstyle='round,pad=0.')

hide = [(590,830), (130, 160), (80, 520), (30, 540), (100, 530), (20, 650), (40, 710), (180,910), (230, 910), (10, 300), (400, 40), (30, 940)]
for h in hide:
	ax.text(*h, "x", color = fc, bbox = bbox, fontsize = 17)

positions = [(320, 113), (803, 255), (299, 588), (635, 643)]
for p in positions:
	ax.text(*p, "x", bbox = bbox, weight="bold", fontsize=18)


ax.axis("off")

plt.imshow(image)
plt.tight_layout()

plt.savefig("renamed_wu_naca_s2.png")
plt.show()
