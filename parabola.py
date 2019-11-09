import tkinter as tk
from math import sqrt


def parabola(canv, size):
    for x in range(-size, size+1):
        y = x**2 / (size / 2)
        plot(canv, x, -y)


def circle(canv, radius, g, h, color='red'):
    canv.create_oval(g + radius, h + radius, g - radius, h - radius, outline=color, width=2)
    # for x in range(g * 50, (g + radius) * 50):
    #     x /= 50
    #     y = h + (sqrt(radius ** 2 - ((x - g) ** 2)))
    #     plot(canv, x, - y)
    #     plot(canv, x, - (2 * h - y))
    #     plot(canv, 2 * g - x, - y)
    #     plot(canv, 2 * g - x, - (2 * h - y))


def draw_axes(canv):
    canv.update()
    x_origin = canv.winfo_width()/2
    y_origin = canv.winfo_height()/2
    canv.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    canv.create_line(-x_origin, 0, x_origin, 0, fill='black')
    canv.create_line(0, y_origin, 0, -y_origin, fill='black')


def plot(canv, x, y):
    canv.create_line(x, y, x + 1, y + 1, fill='red', width=2)


window = tk.Tk()
window.title('Parabola')
window.geometry('640x480')

canvas = tk.Canvas(window, width=640, height=480)
canvas.grid(row=0, column=0)

draw_axes(canvas)
parabola(canvas, 100)
circle(canvas, 50, 50, 50, 'blue')
circle(canvas, 20, 10, 40, 'yellow')
circle(canvas, 20, -100, -30)

window.mainloop()
