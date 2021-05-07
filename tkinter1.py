from tkinter import *

root = Tk()

e = Entry(root,width=50,bg='lightblue')
e.pack()
e.get()
e.insert(0,'Enter name: ')

def click():
    hello = 'Hello '+e.get()
    mylabel = Label(root,text=hello,bg='lightblue',fg='hotpink',
                    padx=50,borderwidth=3)
    mylabel.pack()

button = Button(root,text='enter name: ',padx=50,pady=30,
                command=click,bg='lightblue',fg='hotpink')
button.pack()

root.mainloop()
