import ac
import acsys

from BlueprintLib.ac_gl_utils import Point
from BlueprintLib.ac_gl_utils import Line
from BlueprintLib.ac_gl_utils import Triangle
from BlueprintLib.ac_gl_utils import Quad

class MyDrawable:
    """Example drawable class design.
    
    Args:
        cfg (obj:Config)
        session (obj:Session)
        color (tuple): r,g,b,a on a 0-1 scale.

    General layout I follow is using the following methods:
    - update: For updating the render queue if needed for a complex drawable object
    - draw: For drawing the object on the app window.
    
    If using the drawables list in the app window object, it will call .draw() on all object in the drawables list.
    """
    def __init__(self, cfg, session, color):
        self.cfg = cfg
        self.session = session
        self.color = color

    def update(self, data):
        # Updating the data for the drawable object

    def draw(self):
        # Add this method to the draw method of the app window object.
        set_color(self.color)

        # Example of drawing a quad
        # ac.glBegin(acsys.GL.Quads)
        # ac.glVertex2f(x1,y1)
        # ac.glVertex2f(x2,y2)
        # ac.glVertex2f(x3,y3)
        # ac.glVertex2f(x4,y4)
        # ac.glEnd()        


def set_color(rgba):
    """Apply RGBA color for GL drawing.

    Agrs:
        rgba (tuple): r,g,b,a on a 0-1 scale.
    """
    ac.glColor4f(rgba[0], rgba[1], rgba[2], rgba[3])
