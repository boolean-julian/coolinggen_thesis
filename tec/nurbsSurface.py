import tecplot
import sys
import os

if '-c' in sys.argv:
	tecplot.session.connect()

# load data
datafile = os.path.join('./nurbsSurface.dat')
dataset = tecplot.data.load_tecplot(datafile)

# settings
frame = tecplot.active_frame()
frame.plot_type = tecplot.constant.PlotType.Cartesian3D

# plot
frame.plot()
tecplot.export.save_png("nurbsSurface.png", 600, supersample=3)
