import tkinter
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
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)
window.rowconfigure(2, weight=1)
window.rowconfigure(3, weight=1)
window.rowconfigure(4, weight=1)
window.rowconfigure(5, weight=1)
result = tkinter.Entry(window).grid(row=0, column=0, columnspan=4, sticky='new')

r = ['1', '2', '3', '*', '4', '5', '6', '-', '7', '8', '9', '+', '0',  '/', '=']
k = 0
tkinter.Label(window, text='C', relief='raised', width=6, height=1, font=5).grid(row=1, column=0, sticky='nsw')
tkinter.Label(window, text='CE', relief='raised', width=6, height=1, font=5).grid(row=1, column=1, sticky='nsw')
for i in range(3, 0, -1):
    for j in range(4):
        tkinter.Label(window, text=r[k], relief='raised', width=6, height=1, font=5).grid(row=i+1, column=j, sticky='nsw')
        k += 1
tkinter.Label(window, text=r[-3], relief='raised', width=6, height=1, font=5).grid(row=5, column=0, sticky='nsw')
tkinter.Label(window, text=r[-1], relief='raised', width=13, height=1, font=5)\
    .grid(row=5, column=1, sticky='nsw', columnspan=2)
tkinter.Label(window, text=r[-2], relief='raised', width=6, height=1, font=5).grid(row=5, column=3, sticky='nsw')
tkinter.mainloop()