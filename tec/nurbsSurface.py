import logging
import tecplot
import sys

logging.basicConfig(level=logging.DEBUG)

if '-c' in sys.argv:
	tecplot.session.connect()

tecplot.new_layout()

frame = tecplot.active_frame()
frame.add_text("Hello, World!", position = (36, 50), size = 34)
tecplot.export.save_png("nurbsSurface.png", 600, supersample=3)
