"""
Script to create an image similar to the paintings of Piet Mondrian artwork of Composition in White, Blue and Black.
"""

from mondrian_lib import MondrianObject, paint_artwork, red, blue

# Creating manually 2 objects
mo1 = MondrianObject(type="square", params={"color": red, "width": 600, "height": 100, "zorder": 1, "x": 500, "y": 500})
mo2 = MondrianObject(type="square", params={"color": blue, "width": 200, "height": 600, "zorder": 2, "x": 500, "y": 500})

paint_artwork([mo1, mo2], "manual_art.png")