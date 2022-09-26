import tecplot
import sys
import os

if '-c' in sys.argv:
	tecplot.session.connect()

# load data
datafile = os.path.join('./nurbsSurface.dat')
dataset = tecplot.data.load_tecplot(datafile)
#dataset.delete_zones

# settings
frame = tecplot.active_frame()
#frame.show_border
#frame.active_zones(*zones) #Returns or sets the active Zones.
#https://www.tecplot.com/docs/pytecplot/api/tecplot.data.html#zones

frame.plot_type = tecplot.constant.PlotType.Cartesian3D

"""
plot.fieldmap(newzone).show = True
plot.fieldmap(newzone).contour.show = True
plot.fieldmap(newzone).contour.flood_contour_group = plot.contour(0)
plot.fieldmap(newzone).edge.show = True
plot.fieldmap(newzone).edge.line_thickness = .4
plot.fieldmap(newzone).edge.color = Color.Orange
"""


# plot
frame.plot()
tecplot.export.save_png("nurbsSurface.png", 600, supersample=3)
