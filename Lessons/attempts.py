from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing
    
    # add more functions here

import random

def main():
    scene_width = 800
    scene_height = 500

    canvas = start_drawing("Scene", scene_width, scene_height)

    draw_sky(canvas, scene_width, scene_height)
    draw_water(canvas, scene_width, scene_height)

    draw_cloud = (canvas, 300, 200)
    draw_cloud = (canvas, 100, 400)

    draw_horizontal_gradient(canvas, 0, 0, (0, 0, 0), 200, 200, (180, 180, 255))




    finish_drawing(canvas)

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
        draw_oval(canvas, x1, y1, x1 + 50, y1 + 20, fill="light blue", outline="light blue")



def draw_horizontal_gradient(canvas, x0, y0, color0, x1, y1, color1):
    

main()

'''
def draw_square(canvas, x, y, width):
    x = 100
    y = 100
    width = 50
    draw_line(canvas, x, y, x + width, y)
    draw_line(canvas, x + width, y, x + width, y + width)
    draw_line(canvas, x, y + width, x, y)
    draw_line(canvas, x + width, y + width, x, y + width)
'''


def draw_star(canvas, x, y, size)
    for i in range(5):
        pass

def draw_stars(canvas, x, y):

    size = 25
    height = 25
    space = 10


    for row in range (9):
        if row % 2 == 0:
            for i in range(6):
                draw_star(canvas, x + i * (size + space), y, size)
        else:
            for i in range(5):
                draw_star(canvas, x + + i * (size + space / 2), y, size)
        y -= height

# in main
draw_stars(canvas, x, y)
