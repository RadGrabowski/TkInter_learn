import numpy as np
from math import sin, cos, radians
import tkinter as tk
import time


def opening_bracket(x, y):
    global canvas
    canvas.create_line(10 + x, 30 + y, 20 + x, 30 + y, fill='black')
    canvas.create_line(10 + x, 30 + y, 10 + x, 120 + y, fill='black')
    canvas.create_line(10 + x, 120 + y, 20 + x, 120 + y, fill='black')


def closing_bracket(x, y):
    canvas.create_line(150 + x, 30 + y, 140 + x, 30 + y, fill='black')
    canvas.create_line(150 + x, 30 + y, 150 + x, 120 + y, fill='black')
    canvas.create_line(150 + x, 120 + y, 140 + x, 120 + y, fill='black')


def show_matrix(m, shux, shuy):
    piy = 45
    for num in range(4):
        pix = 30
        for num2 in range(4):
            canvas.create_text(pix + shux, piy + shuy, fill='black', text=m[num][num2])
            pix += 33
        piy += 20


def print_result():
    global canvas
    canvas.delete('all')
    try:
        d = int(distanceEntry.get())
        a = radians(int(angleEntry.get()))
        d2 = int(distanceEntry2.get())
        a2 = radians(int(angleEntry2.get()))
        rot = rotVal.get()
        trans = transVal.get()
        trans2 = transVal2.get()
        first_matrix = calculate(rot, trans, d, a)
        second_matrix = calculate(rot, trans2, d2, a2)
        final_matrix = np.around(np.dot(first_matrix, second_matrix), decimals=3)
        opening_bracket(0, 0)
        show_matrix(first_matrix, 0, 0)
        closing_bracket(0, 0)
        canvas.create_text(160, 73, fill='black', text='x', font=5)
        opening_bracket(160, 0)
        show_matrix(second_matrix, 160, 0)
        closing_bracket(160, 0)
        canvas.create_text(320, 73, fill='black', text='=', font=5)
        opening_bracket(320, 0)
        show_matrix(final_matrix, 320, 0)
        closing_bracket(320, 0)
        canvas.create_text(80, 140, fill='darkblue', text='A1', font=5)
        canvas.create_text(240, 140, fill='darkblue', text='A2', font=5)
        canvas.create_text(400, 140, fill='darkblue', text='T', font=5)
    except ValueError:
        canvas.create_text(280, 80, fill='red', text='Wrong distance input!', font=('Purisa', 40))


def calculate(r, t, p, q):
    if t == 1:
        trans_array = np.array([[1, 0, 0, p],
                                [0, 1, 0, 0],
                                [0, 0, 1, 0],
                                [0, 0, 0, 1]])
    elif t == 2:
        trans_array = np.array([[1, 0, 0, 0],
                                [0, 1, 0, p],
                                [0, 0, 1, 0],
                                [0, 0, 0, 1]])
    elif t == 3:
        trans_array = np.array([[1, 0, 0, 0],
                                [0, 1, 0, 0],
                                [0, 0, 1, p],
                                [0, 0, 0, 1]])
    if r == 1:
        rot_array = np.array([[1, 0, 0, 0],
                              [0, cos(q), -sin(q), 0],
                              [0, sin(q), cos(q), 0],
                              [0, 0, 0, 1]])
    elif r == 2:
        rot_array = np.array([[cos(q), 0, sin(q), 0],
                              [0, 1, 0, 0],
                              [-sin(q), 0, cos(q), 0],
                              [0, 0, 0, 1]])
    elif r == 3:
        rot_array = np.array([[cos(q), -sin(q), 0, 0],
                              [sin(q), cos(q), 0, 0],
                              [0, 0, 1, 0],
                              [0, 0, 0, 1]])
    result_array = np.around(np.dot(rot_array, trans_array), decimals=3)
    return result_array


window = tk.Tk()
window.title('Rotations and translations calculator')
window.geometry('580x400-20-200')
window['padx'] = 5
window['pady'] = 15

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=5)
window.columnconfigure(2, weight=1)
window.columnconfigure(3, weight=5)
window.columnconfigure(4, weight=1)
window.columnconfigure(5, weight=5)
window.columnconfigure(7, weight=1)
window.rowconfigure(0, weight=1)
window.rowconfigure(2, weight=2)

rotationFrame = tk.LabelFrame(window, text='Rotation')
rotationFrame.grid(row=0, column=0, sticky='ns', rowspan=2)
translationFrame = tk.LabelFrame(window, text='First translation')
translationFrame.grid(row=0, column=2, sticky='nsew', rowspan=2)
translationFrame2 = tk.LabelFrame(window, text='Second translation')
translationFrame2.grid(row=2, column=2, sticky='sew', rowspan=2)

rotVal = tk.IntVar()
rotVal.set(1)
button1 = tk.Radiobutton(rotationFrame, text='Around x axis', value=1, variable=rotVal)
button2 = tk.Radiobutton(rotationFrame, text='Around y axis', value=2, variable=rotVal)
button3 = tk.Radiobutton(rotationFrame, text='Around z axis', value=3, variable=rotVal)
button1.grid(row=0, column=0, sticky='w')
button2.grid(row=1, column=0, sticky='w')
button3.grid(row=2, column=0, sticky='w')

transVal = tk.IntVar()
transVal.set(1)
button4 = tk.Radiobutton(translationFrame, text='Along x axis', value=1, variable=transVal)
button5 = tk.Radiobutton(translationFrame, text='Along y axis', value=2, variable=transVal)
button6 = tk.Radiobutton(translationFrame, text='Along z axis', value=3, variable=transVal)
button4.grid(row=0, column=0, sticky='w')
button5.grid(row=1, column=0, sticky='w')
button6.grid(row=2, column=0, sticky='w')
transVal2 = tk.IntVar()
transVal2.set(1)
button7 = tk.Radiobutton(translationFrame2, text='Along x axis', value=1, variable=transVal2)
button8 = tk.Radiobutton(translationFrame2, text='Along y axis', value=2, variable=transVal2)
button9 = tk.Radiobutton(translationFrame2, text='Along z axis', value=3, variable=transVal2)
button7.grid(row=0, column=0, sticky='w')
button8.grid(row=1, column=0, sticky='w')
button9.grid(row=2, column=0, sticky='w')

distanceFrame = tk.LabelFrame(window, text='Distance 1')
distanceFrame.grid(row=0, column=4, sticky='swe')
distanceEntry = tk.Entry(distanceFrame, width=5)
distanceEntry.grid(row=0, column=0)
angleFrame = tk.LabelFrame(window, text='Angle 1')
angleFrame.grid(row=1, column=4, sticky='nwe')
angleEntry = tk.Spinbox(angleFrame, width=5, values=(-180, -90, -60, -45, -30, 0, 30, 45, 60, 90, 180))
angleEntry.grid(row=1, column=0)

distanceFrame2 = tk.LabelFrame(window, text='Distance 2')
distanceFrame2.grid(row=2, column=4, sticky='swe')
distanceEntry2 = tk.Entry(distanceFrame2, width=5)
distanceEntry2.grid(row=0, column=0)
angleFrame2 = tk.LabelFrame(window, text='Angle 1')
angleFrame2.grid(row=3, column=4, sticky='nwe')
angleEntry2 = tk.Spinbox(angleFrame2, width=5, values=(-180, -90, -60, -45, -30, 0, 30, 45, 60, 90, 180))
angleEntry2.grid(row=1, column=0)

startButton = tk.Button(window, text="Let's go!", command=print_result).grid(row=3, column=6, sticky='sw')
canvas = tk.Canvas(window, height=150)
canvas.grid(row=4, column=0, columnspan=9, sticky='sew')
# canvas.configure(background='green')
imag = tk.PhotoImage(file='rotate-3d-images1.png')
imgLabel = tk.Label(window, image=imag).grid(row=0, column=7, rowspan=4, sticky='e')

window.mainloop()
