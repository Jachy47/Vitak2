import turtle

screen = turtle.Screen()
canvas = screen.getcanvas()   # Tkinter canvas
t = turtle.Turtle()
t.speed(0)
t.penup()

drawing = False

def start_draw(event):
    global drawing
    drawing = True
    x = event.x - screen.window_width() / 2
    y = screen.window_height() / 2 - event.y
    t.goto(x, y)
    t.pendown()

def draw(event):
    if drawing:
        x = event.x - screen.window_width() / 2
        y = screen.window_height() / 2 - event.y
        t.goto(x, y)

def stop_draw(event):
    global drawing
    drawing = False
    t.penup()

# Bind Tkinter událostí
canvas.bind("<ButtonPress-1>", start_draw)
canvas.bind("<B1-Motion>", draw)
canvas.bind("<ButtonRelease-1>", stop_draw)

turtle.done()
