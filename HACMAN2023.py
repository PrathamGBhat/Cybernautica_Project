import tkinter as tk
from tkinter import *

'''def Username1():
    input_text=Username.get()
    canvas.create_rectangle(577,72,302,56, fill='white',text=input_text)'''

window=tk.Tk()
window.geometry('1440x1024')
canvas= tk.Canvas(window, width=1440, height=1024)

rectangle=canvas.create_rectangle(0,0,1440,1024,fill='white')

Outreach=canvas.create_rectangle(19,96,875,270,fill='#D9D9D9')
'''Transactions=canvas.create_rectangle(1134,868,283,96,fill='#D9D9D9')
View_Inventory=canvas.create_rectangle(323,860,777,121,fill='#D9D9D9')
Change_Username=canvas.create_rectangle(-26,532,630,141,fill='#D9D9D9')
Change_Password=canvas.create_rectangle(55,693,467,102,fill='#D9D9D9')
Bio=canvas.create_rectangle(681,602,723,194,fill='#D9D9D9')
Education=canvas.create_rectangle(903,405,501,126,fill='#D9D9D9')
Registered=canvas.create_rectangle(905,188,499,677,fill='#D9D9D9')
Contact=canvas.create_rectangle(1019,298,387,63,fill='#D9D9D9')
Username=canvas.create_rectangle(577,72,302,56,fill='#D9D9D9')'''


profile=canvas.create_oval(99,103,401,409,fill='White')
frame=tk.Frame(window, width=1440, height=1024)

Username=tk.Entry(window, width=30)
Username.pack()
canvas.pack()
window.mainloop()