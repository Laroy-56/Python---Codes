import tkinter as tk
import math
import random

root = tk.Tk()
root.title("Smooth Moving Hexagon")

WIDTH, HEIGHT = 800, 600
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

# Hexagon properties
x, y = WIDTH // 2, HEIGHT // 2
radius = 50
dx, dy = 4, 3   # movement speed
color = "cyan"

def get_hexagon_points(x, y, r):
    points = []
    for i in range(6):
        angle = math.radians(60 * i)
        px = x + r * math.cos(angle)
        py = y + r * math.sin(angle)
        points.extend([px, py])
    return points

hexagon = canvas.create_polygon(get_hexagon_points(x, y, radius), fill=color)

def update():
    global x, y, dx, dy

    x += dx
    y += dy

    # Bounce off walls
    if x - radius <= 0 or x + radius >= WIDTH:
        dx *= -1
        change_color()
    if y - radius <= 0 or y + radius >= HEIGHT:
        dy *= -1
        change_color()

    canvas.coords(hexagon, get_hexagon_points(x, y, radius))
    root.after(16, update)  # ~60 FPS

def change_color():
    global color
    color = f"#{random.randint(0, 0xFFFFFF):06x}"
    canvas.itemconfig(hexagon, fill=color)

update()
root.mainloop()