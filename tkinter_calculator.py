import tkinter


def press(num):
    global equation, shift
    try:
        if num == '=':
            result_window.delete('all')
            result_window.create_text(10, 32, fill='blue', text=('{:.12f}'.format(eval(equation)).rstrip('.0')), font=('Purisa', 20), anchor='w')
            equation = ''
            shift = 0
        elif num == 'C':
            result_window.delete('all')
            equation = ''
            shift = 0
        elif num == 'CE':
            if equation == '':
                result_window.delete('all')
            else:
                equation = list(equation)
                equation.pop()
                equation = ''.join(map(str, equation))
                result_window.delete('all')
                shift = 0
                result_window.create_text(10 + shift, 32, fill='blue', text=equation, font=('Purisa', 20), anchor='w')
        else:
            result_window.delete('all')
            equation += num
            result_window.create_text(10, 32, fill='blue', text=equation, font=('Purisa', 20), anchor='w')
    except (SyntaxError, ZeroDivisionError):
        result_window.create_text(10, 32, fill='red', text='Wrong input!', font=('Purisa', 30), anchor='w')
        equation = ''


window = tkinter.Tk()
window.title('Calculator')
window.geometry('300x350-100-200')
window['padx'] = 10
window['pady'] = 15

# window configuration
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)
window.columnconfigure(3, weight=1)
window.columnconfigure(4, weight=1)
window.columnconfigure(5, weight=1)
window.rowconfigure(0, weight=10)
window.rowconfigure(1, weight=1)
window.rowconfigure(2, weight=1)
window.rowconfigure(3, weight=1)
window.rowconfigure(4, weight=1)
window.rowconfigure(5, weight=1)
result_window = tkinter.Canvas(window)
result_window.grid(row=0, column=0, columnspan=4, sticky='nsew')
result_window.configure(bd=3, background='white', height=50, relief='groove')

# buttons

signs = ['1', '2', '3', '*', '4', '5', '6', '-', '7', '8', '9', '+']
sign = 0
tkinter.Button(window, text='0', relief='raised', width=6, height=2, font=5, command=lambda: press('0'))\
    .grid(row=5, column=0, sticky='nw')
tkinter.Button(window, text='=', relief='raised', width=14, height=2, font=5, command=lambda: press('='))\
    .grid(row=5, column=1, sticky='nsw', columnspan=2)
tkinter.Button(window, text='/', relief='raised', width=6, height=2, font=5, command=lambda: press('/'))\
    .grid(row=5, column=3, sticky='nsw')
tkinter.Button(window, text='1', relief='raised', width=6, height=2, font=5, command=lambda: press('1'))\
    .grid(row=4, column=0, sticky='nw')
tkinter.Button(window, text='2', relief='raised', width=6, height=2, font=5, command=lambda: press('2'))\
    .grid(row=4, column=1, sticky='nw')
tkinter.Button(window, text='3', relief='raised', width=6, height=2, font=5, command=lambda: press('3'))\
    .grid(row=4, column=2, sticky='nw')
tkinter.Button(window, text='*', relief='raised', width=6, height=2, font=5, command=lambda: press('*'))\
    .grid(row=4, column=3, sticky='nsw')
tkinter.Button(window, text='4', relief='raised', width=6, height=2, font=5, command=lambda: press('4'))\
    .grid(row=3, column=0, sticky='nw')
tkinter.Button(window, text='5', relief='raised', width=6, height=2, font=5, command=lambda: press('5'))\
    .grid(row=3, column=1, sticky='nw')
tkinter.Button(window, text='6', relief='raised', width=6, height=2, font=5, command=lambda: press('6'))\
    .grid(row=3, column=2, sticky='nw')
tkinter.Button(window, text='-', relief='raised', width=6, height=2, font=5, command=lambda: press('-'))\
    .grid(row=3, column=3, sticky='nsw')
tkinter.Button(window, text='7', relief='raised', width=6, height=2, font=5, command=lambda: press('7'))\
    .grid(row=2, column=0, sticky='nw')
tkinter.Button(window, text='8', relief='raised', width=6, height=2, font=5, command=lambda: press('8'))\
    .grid(row=2, column=1, sticky='nw')
tkinter.Button(window, text='9', relief='raised', width=6, height=2, font=5, command=lambda: press('9'))\
    .grid(row=2, column=2, sticky='nw')
tkinter.Button(window, text='+', relief='raised', width=6, height=2, font=5, command=lambda: press('+'))\
    .grid(row=2, column=3, sticky='nsw')
tkinter.Button(window, text='C', relief='raised', width=6, height=2, font=5, command=lambda: press('C'))\
    .grid(row=1, column=0, sticky='nw')
tkinter.Button(window, text='CE', relief='raised', width=6, height=2, font=5, command=lambda: press('CE'))\
    .grid(row=1, column=1, sticky='nw')

equation = ''
shift = 0
# window size constrains
window.update()
window.minsize(250, 300)
window.maxsize(300, 350)
tkinter.mainloop()
