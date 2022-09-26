import tecplot
from tecplot.constant import *

import numpy as np
from PIL import Image
import os

# load data
filelist = [os.path.join(f'./nurbsCurveDeg{i}.dat') for i in range(1, 4)]
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
	f.plot_type = tecplot.constant.PlotType.Cartesian2D
	plots.append(f.plot())

page.delete_frame(frame)

# plot global settings
for p in plots:
	p.axes.axis_mode = AxisMode.Independent
	p.axes.x_axis.min = -0.1
	p.axes.x_axis.max = +3.1

	p.axes.y_axis.min = -0.1
	p.axes.y_axis.max = +3.1

	p.axes.x_axis.show = False
	p.axes.y_axis.show = False

# plot show settings
for p in plots:
	p.show_mesh 		= True
	p.show_scatter		= True

# fieldmap options
for p in plots:
	for i in range(1, 2*len(filelist), 2):	
		p.fieldmap(i).mesh.color = Color.Custom3
		p.fieldmap(i).mesh.line_thickness = 10
		p.fieldmap(i).scatter.show = False

	for i in range(0, 2*len(filelist), 2):
		p.fieldmap(i).mesh.line_pattern = LinePattern.Dashed
		p.fieldmap(i).mesh.line_thickness = 1
		p.fieldmap(i).mesh.color = Color.Custom6
		
		p.fieldmap(i).scatter.line_thickness = 1
		p.fieldmap(i).scatter.color = Color.Custom6

		p.fieldmap(i).scatter.symbol_type = SymbolType.Geometry
		p.fieldmap(i).scatter.symbol().shape = GeomShape.Circle
		p.fieldmap(i).scatter.fill_mode = FillMode.UseLineColor

	p.fieldmap(0).mesh.show = False;

plots[0].fieldmap(2).show = False;
plots[0].fieldmap(4).show = False;
plots[0].fieldmap(3).show = False;
plots[0].fieldmap(5).show = False;

plots[1].fieldmap(0).show = False;
plots[1].fieldmap(4).show = False;
plots[1].fieldmap(1).show = False;
plots[1].fieldmap(5).show = False;

plots[2].fieldmap(0).show = False;
plots[2].fieldmap(2).show = False;
plots[2].fieldmap(1).show = False;
plots[2].fieldmap(3).show = False;

# latex text
framelist[0].activate()
framelist[0].add_latex(r"$p = 2, \textrm{ linear}$", (75, 90), size=60, anchor=TextAnchor.Center)

framelist[1].activate()
framelist[1].add_latex(r"$p = 3, \textrm{ quadratic}$", (75, 90), size=60, anchor=TextAnchor.Center)

framelist[2].activate()
framelist[2].add_latex(r"$p = 4, \textrm{ cubic}$", (75, 90), size=60, anchor=TextAnchor.Center)

# export and trim
filename = "nurbsCurve.png"
tecplot.export.save_png(filename, width=2500, supersample=3)

border = 5
with Image.open(filename) as inp:
    arr = np.array(inp)[border:-border,border:-border]
    out = Image.fromarray(arr)
    out.save(filename)