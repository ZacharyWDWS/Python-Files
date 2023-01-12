# -*- coding: utf-8 -*-
"""
    FULL DISCLOSURE: This is not my original code. I found the code on 
    StackOverflow and made some modifications for ease of reading.
    
    This script will produce an image of the available named colors 
    provided in MatPlotLib.
    
    NOTE: Color names are CASE SENSISTIVE
    
    Note that you can also specify color in RGB or RGBA form using float values,
    RBG or RBGA using hex values, names from the xkcd color survey (prefixed
    with xkcd: ), and a few other forms.
    
"""
import matplotlib.pyplot as plt
from matplotlib import colors as namedColors


colors = dict(namedColors.BASE_COLORS, **namedColors.CSS4_COLORS)

# Sort colors by hue, saturation, value and name.
by_hsv = sorted((tuple(namedColors.rgb_to_hsv(namedColors.to_rgba(color)[:3])), name)
                for name, color in colors.items())
sorted_names = [name for hsv, name in by_hsv]

# Create a grid for the color display - 4 columns, evenly divided
colorCount = len(sorted_names)
colCount   = 4
rowCount   = colorCount // colCount

# Define a "space" for creating the image
fig, ax = plt.subplots(figsize=(12, 10))


# Get height and width of plot area
X, Y = fig.get_dpi() * fig.get_size_inches()
# Use height & width to determine sizing of entries in chart
h = Y / (rowCount + 1)
w = X / colCount

# Iterate through the group of color names
for each, name in enumerate(sorted_names):
    row = each % rowCount              # Determine row placement
    col = each // rowCount             # Determine column placement
    y = Y - (row * h) - h

    # Set position for placing color 'swatch' and name
    xi_line = w * (col + 0.05)
    xf_line = w * (col + 0.25)
    xi_text = w * (col + 0.3)
    
    # Set color name in position
    ax.text(xi_text, y, name, fontsize=(h * 0.8),
            horizontalalignment='left',
            verticalalignment='center')
    # Set color 'swatch' in position
    ax.hlines(y + h * 0.1, xi_line, xf_line,
              color=colors[name], linewidth=(h * 0.8))
# end iteration

# Set bounds of chart
ax.set_xlim(0, X)
ax.set_ylim(0, Y)
ax.set_axis_off()

# Create the actual image
fig.subplots_adjust(left=0, right=1,
                    top=1, bottom=0,
                    hspace=0, wspace=0)

# 'Write' plot to output
plt.show()
