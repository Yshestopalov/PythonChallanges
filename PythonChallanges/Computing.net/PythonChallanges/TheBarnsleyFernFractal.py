# The Barnsley Fern - www.101computing.net/the-barnsley-fern-fractal

# --- Imports ---
import turtle, random

# --- Setup ---
BG_COLOR = "#000000"
PEN_COLOR = "#bfff00"
NUMBER_OF_DOTS = 25000
SCALE = 380

def setup():
    # window
    window = turtle.Screen()
    window.bgcolor(BG_COLOR)

    # pen
    pen = turtle.Turtle()
    pen.tracer(0)
    pen.speed(0)
    pen.penup()
    pen.color(PEN_COLOR)
    pen.hideturtle()

    return pen

# --- Process ---
def draw_fern_fractal(pen, number_of_dots, scale):
    x = 0.5
    y = 0.0
    for i in range(number_of_dots):
        r = random.randint(0, 50)
        if r <= 1:
            tempx = 0.5
            tempy = 0.16 * y
        elif r <= 8:
            tempx = 0.2 * x - 0.26 * y + 0.400
            tempy = 0.23 * x + 0.22 * y - 0.045
        elif r <= 15:
            tempx = -0.15 * x + 0.28 * y + 0.575
            tempy = 0.26 * x + 0.24 * y - 0.086
        else:
            tempx = 0.85 * x + 0.04 * y + 0.075
            tempy = -0.04 * x + 0.850 * y + 0.180
        x, y = tempx, tempy
        pen.setpos(x * scale - scale // 2, y * scale - scale // 2)
        pen.dot(1)

# --- Output ---
pen = setup()
draw_fern_fractal(pen, NUMBER_OF_DOTS, SCALE)

# Update
screen = pen.getscreen()
screen.update()
