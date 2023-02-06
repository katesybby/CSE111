# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing \

import random

def main():
    
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)


    # Call the draw_sky and draw_ground functions in this file.
    draw_sky(canvas, scene_width, scene_height)
    draw_water(canvas, scene_width, scene_height)

    draw_cloud = (canvas, 300, 200)
    draw_cloud = (canvas, 100, 400)

    #draw_arc = (canvas, , )

    #draw_horizontal_gradient(canvas, 0, 0, (0, 0, 0), 200, 200, (180, 180, 255))


    #sky_height = round(scene_height / 3)
    min_diam = 30
    max_diam = 50

    for i in range(100):
        x = random.randint(0, scene_width - max_diam)
        y = random.randint(0, scene_height - max_diam)
        #y = random.randint(0, half_height)
        diameter = random.randint(min_diam, max_diam)
        draw_oval(canvas, x, y, x + diameter, y + diameter, fill="white", outline="white")

#canvas, 0, scene_height / 3, scene_width, scene_height, width=0,


    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


    # Call your drawing functions such
    # as draw_sky and draw_ground here.

# draw_line(canvas, 10, 10, 300, 400, width=5, fill='pink')     # diagonal line
# draw_square(canvas, 10, 10, 50)
# draw_square(canvas, 100, 50, 20)

# Define your functions such as
# draw_sky and draw_ground here.

def draw_sky(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, scene_height / 3, scene_width, scene_height, width=0, fill="pink")

def draw_water(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, 0, scene_width, scene_height / 3, width=0, fill="blue")
    
def draw_cloud(canvas, x, y):
    for i in range(5): #loops 5x
        #x1 = random.randint(1, scene_width)
        #y1 = random.randint(1, scene_height)
        x1 = random.randint(1, 20) + x
        y1 = random.randint(1, 20) + y
        draw_oval(canvas, x1, y1, x1 + 50, y1 + 20, fill="white", outline="white")

def draw_arc(canvas, x0, y0, x1, y1, *, start=0, extent=90, width=1, outline="black", fill=""):
    pass

def draw_horizontal_gradient(canvas, x0, y0, color0, x1, y1, color1):
    pass

# Call the main function so that
# this program will start executing.
main()