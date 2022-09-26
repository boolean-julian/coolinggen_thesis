import tecplot
from tecplot.constant import MeshType, Color, Projection, TextAnchor

import numpy as np
from PIL import Image
import os

# load data
filelist = [os.path.join(f'./nurbsSurfaceDeg{i}.dat') for i in range(1, 4)]
dataset = tecplot.data.load_tecplot(filelist)

# frame global settings
page = tecplot.active_page()
frame = tecplot.active_frame()

size = (16, 12)
subplots = 3
framelist = [page.add_frame(position=(size[0]*i, 0), size=size) for i in range(subplots)]

plots = []
for f in framelist:
	f.activate()
	f.show_border = False
	f.plot_type = tecplot.constant.PlotType.Cartesian3D
	plots.append(f.plot())

page.delete_frame(frame)

# plot global settings
for p in plots:
	p.axes.orientation_axis.show = False
	p.axes.preserve_scale = True

# plot show settings
for p in plots:
	p.show_mesh 		= True
	p.show_edge 		= False
	p.show_shade 		= True
	p.show_contour 		= False
	p.show_scatter		= True
	p.use_translucency 	= True

# fieldmap options
for p in plots:
	for i in range(1, 2*len(filelist)+1, 2):	
		p.fieldmap(i).shade.color = Color.Custom3
		p.fieldmap(i).mesh.show = False
		p.fieldmap(i).scatter.show = False
		p.fieldmap(i).effects.surface_translucency = 10

	p.fieldmap(0).shade.show = False
	p.fieldmap(0).mesh.line_thickness = 0.5
	p.fieldmap(0).mesh.color = Color.Custom6
	p.fieldmap(0).scatter.show = False

	p.fieldmap(2).show = False
	p.fieldmap(4).show = False

plots[0].fieldmap(3).show = False;
plots[0].fieldmap(5).show = False;

plots[1].fieldmap(1).show = False;
plots[1].fieldmap(5).show = False;

plots[2].fieldmap(1).show = False;
plots[2].fieldmap(3).show = False;

# plot view options
for p in plots:
	p.view.translate(5, -3)

framelist[0].activate()
framelist[0].add_latex(r"$p = q = 2$", (75, 90), size=60, anchor=TextAnchor.Center)

framelist[1].activate()
framelist[1].add_latex(r"$p = q = 3$", (75, 90), size=60, anchor=TextAnchor.Center)

framelist[2].activate()
framelist[2].add_latex(r"$p = q = 4$", (75, 90), size=60, anchor=TextAnchor.Center)

# export and trim
filename = "nurbsSurface.png"
tecplot.export.save_png(filename, width=2500, supersample=3)

border = 5
with Image.open(filename) as inp:
    arr = np.array(inp)[border:-border,border:-border]
    out = Image.fromarray(arr)
    out.save(filename)