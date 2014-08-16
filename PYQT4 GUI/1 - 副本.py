from tkinter import *
root = Tk()

ff=LabelFrame(root,height=60,width=280,text='hahaha')
ff.pack()

Radiobutton(ff,text = 'python').pack()
Radiobutton(ff,text = 'tkinter').pack()
Radiobutton(ff,text = 'widget').pack()
root.mainloop()