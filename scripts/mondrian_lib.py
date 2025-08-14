"""
Script to create an image similar to the paintings of Piet Mondrian artwork of Composition in White, Blue and Black.
"""

#import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib
import random
from math import ceil

# Force matplotlib to not use any Xwindows backend.
matplotlib.use('agg')

# Define the colors
# mondrian_set_2 = {"white": "#cdced1", "gray": "#7b8081", "black": "#1f2726", "red": "#bc4432", "yellow": "#dbb653", "blue": "#244372"}
white = "#cdced1"
gray = "#7b8081"
black = "#1f2726"
red = "#bc4432"
blue = "#244372"
yellow = "#dbb653"

# Define the objects
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 1000
LINE_WIDTH = 20

def paint_artwork(objects, filename="composite_objects"):
    """
    Draws the objects to a png file
    """
    # Create a figure and axis
    fig, ax = plt.subplots()
    for object in objects:
        object.draw(ax)

    ax.set_xlim(0, CANVAS_WIDTH)
    ax.set_ylim(0, CANVAS_HEIGHT)
    ax.set_aspect('equal', adjustable='box')
    ax.set_xticks([])
    ax.set_yticks([])

    # Save as png
    plt.savefig(filename)
    return

# Define a class for colored objects
class MondrianObject:

    def __init__(self, type="square", params={}):

        if len(params) == 0:
            if type == "square":
                color = random.choices([red, blue, yellow], weights=[1, 1, 1])[0] # Get a random color
                l = random.randint(2*LINE_WIDTH, CANVAS_WIDTH//2)
                w, h = l, l
                zorder = 1
            elif type == "rectangle":
                color = random.choice([red, blue, yellow])
                w = random.randint(2*LINE_WIDTH, CANVAS_WIDTH//2)
                h = random.randint(2*LINE_WIDTH, CANVAS_HEIGHT//2)
                zorder = 1
            elif type == "row":
                color = black
                w = random.randint(LINE_WIDTH, CANVAS_WIDTH)
                h = LINE_WIDTH
                zorder = 2
            elif type == "column":
                color = black
                w = LINE_WIDTH
                h = random.randint(LINE_WIDTH, CANVAS_HEIGHT)
                zorder = 2
            else:
                raise ValueError(f"Invalid type: {type}")
            # Randomly place the object in the canvas
            x = random.randint(ceil(w/2), CANVAS_WIDTH - ceil(w/2))
            y = random.randint(ceil(h/2), CANVAS_HEIGHT - ceil(h/2))
        else:
            # Not random: Unpack the parameters. If not provided, use default values.
            color = params.get("color", black)
            w = params.get("width", CANVAS_WIDTH//4)
            h = params.get("height", CANVAS_HEIGHT//4)
            zorder = params.get("zorder", 1)
            x = params.get("x", CANVAS_WIDTH//2)
            y = params.get("y", CANVAS_HEIGHT//2)
        # Set the attributes of the object
        self.type = type
        self.color = color
        self.center = (x, y)
        self.width = w
        self.height = h
        self.zorder = zorder

    def intersects(self, other):
        x1, y1 = self.center
        w1, h1 = self.width, self.height
        x2, y2 = other.center
        w2, h2 = other.width, other.height
        # They should be at most one line CANVAS_WIDTH apart
        intersect_x = abs(x1 - x2) < (w1 + w2)/2 + LINE_WIDTH
        intersect_y = abs(y1 - y2) < (h1 + h2)/2 + LINE_WIDTH
        return intersect_x and intersect_y

    def intersects_with_all(self, objects):
        """
        Checks if the objects intersects with any other object in the list.
        """
        for other in objects:
            skip = (self.type in ["row", "column"] and other.type in ["row", "column"])
            intersect = self.intersects(other)
            if not skip and intersect:
                return True
        return False

    def __str__(self):
        return f"ColoredSquare(type={self.type}, color={self.color}, center={self.center}, CANVAS_WIDTH={self.width}, CANVAS_HEIGHT={self.height})"

    def draw(self, ax):
        x0 = self.center[0] - self.width/2
        y0 = self.center[1] - self.height/2
        ax.add_patch(patches.Rectangle((x0, y0), self.width, self.height, facecolor=self.color, zorder=self.zorder, linewidth=0))