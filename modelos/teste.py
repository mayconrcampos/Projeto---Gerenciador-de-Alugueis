from tkinter import *

root = Tk()

root.geometry("800x600")

labelframe = LabelFrame(root, text="This is a LabelFrame")
labelframe.place(relx=0.001, rely=0.001, relwidth=0.99, relheight=0.3)
 
left = Label(labelframe, text="Inside the LabelFrame")
left.place(relx=0.4, rely=0.01)
 
root.mainloop()