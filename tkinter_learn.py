import tkinter
import os
window = tkinter.Tk()
window.title('Screen demo')
window.geometry('640x480-20-200')
window['padx'] = 5
label = tkinter.Label(window, text='Tkinter Screen Demo')
label.grid(row=0, column=0, columnspan=3)

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=3)
window.columnconfigure(3, weight=3)
window.columnconfigure(4, weight=3)
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=10)
window.rowconfigure(2, weight=1)
window.rowconfigure(3, weight=3)
window.rowconfigure(4, weight=3)

fileList = tkinter.Listbox(window)
fileList.grid(row=1, column=0, rowspan=2, sticky='nesw')
fileList.config(border=2, relief='sunken')
for zone in os.listdir('/Windows/System32'):
    fileList.insert(tkinter.END, zone)

fileScroll = tkinter.Scrollbar(window, orient=tkinter.VERTICAL, command=fileList.yview)
fileScroll.grid(row=1, column=1, rowspan=2, sticky='nsw')
fileList['yscrollcommand'] = fileScroll.set

optionFrame = tkinter.LabelFrame(window, text='File Details')
optionFrame.grid(row=1, column=2, sticky='ne')

optionVal = tkinter.IntVar()
optionVal.set(3)
button1 = tkinter.Radiobutton(optionFrame, text='File name', value=1, variable=optionVal)
button2 = tkinter.Radiobutton(optionFrame, text='Path', value=2, variable=optionVal)
button3 = tkinter.Radiobutton(optionFrame, text='Timestamp', value=3, variable=optionVal)
button1.grid(row=0, column=0, sticky='w')
button2.grid(row=1, column=0, sticky='w')
button3.grid(row=2, column=0, sticky='w')

resultLabel = tkinter.Label(window, text='Result')
resultLabel.grid(row=2, column=2, sticky='nw')
result = tkinter.Entry(window)
result.grid(row=2, column=2, sticky='sw')

timeFrame = tkinter.LabelFrame(window, text='Time')
timeFrame.grid(row=3, column=0, sticky='new')
hourSpinner = tkinter.Spinbox(timeFrame, width=3, values=tuple(range(0, 24)))
minuteSpinner = tkinter.Spinbox(timeFrame, width=3, from_=0, to=59)
secondSpinner = tkinter.Spinbox(timeFrame, width=3, from_=0, to=59)
hourSpinner.grid(row=0, column=0)
tkinter.Label(timeFrame, text=':').grid(row=0, column=1)
minuteSpinner.grid(row=0, column=2)
tkinter.Label(timeFrame, text=':').grid(row=0, column=3)
secondSpinner.grid(row=0, column=4)
timeFrame['padx'] = 36

dateFrame = tkinter.LabelFrame(window, text='Date')
dateFrame.grid(row=4, column=0, sticky='new')
tkinter.Label(dateFrame, text='Day').grid(row=0, column=0, sticky='w')
tkinter.Label(dateFrame, text='Month').grid(row=0, column=1, sticky='w')
tkinter.Label(dateFrame, text='Year').grid(row=0, column=2, sticky='w')

daySpinner = tkinter.Spinbox(dateFrame, width=5, values=tuple(range(1, 32)))
monthSpinner = tkinter.Spinbox(dateFrame, width=5, values=('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
yearSpinner = tkinter.Spinbox(dateFrame, width=5, from_=2000, to=2099)
daySpinner.grid(row=1, column=0)
monthSpinner.grid(row=1, column=1)
yearSpinner.grid(row=1, column=2)
dateFrame['padx'] = 36

okButton = tkinter.Button(window, text='OK').grid(row=4, column=3, sticky='e')
cancelButton = tkinter.Button(window, text='Cancel', command=window.destroy).grid(row=4, column=4, sticky='w')

window.mainloop()
print(optionVal.get())
print(monthSpinner)
