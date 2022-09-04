import tkinter as tk
from function1 import main
from function2 import main1
window = tk.Tk()
window.title('human tracking')
window.geometry('200x200')

label = tk.Label(window, text='testing GUI', bg='green', font=('Arial', 12), width=15, height=2)
label.pack()

button1 = tk.Button(window, text='select a video', bg='green', width=20, height=2, command= main)
button1.pack()

button2 = tk.Button(window, text='using camera', bg='green', width=20, height=2, command= main1)
button2.pack()


window.mainloop()
