from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

root=Tk()
root.title("Radio Buttons")

frame=LabelFrame(root,text = "Radio Button", padx=15,pady=15)
frame.pack(padx=20,pady=20)
frame1=LabelFrame(root,text = "...",padx=10,pady=10)

'''
def click(val):
    global label
    label.pack_forget()
    label=Label(frame1,text="Congratulation! You checked option {}".format(val))
    label.pack()
'''
def func(val):
    response = messagebox.askquestion("Congratulation!",
                "You checked option {}. Would you like to continue?".format(val))
    #showinfo, showerror, showwarning,askquestion,askokcancel,askyesno
    if response == 'no':
        root.destroy()
    


        
r=IntVar()
L=[('Option 1',1),
   ('Option 2',2),
   ('Option 3',3),
   ('Option 4',4),
   ('Option 5',5)
    ]
for x,y in L:
    Radiobutton(frame,text=x,variable=r,value=y).pack(anchor=W)


button = Button(root,text = "Accept",command=lambda: func(r.get()))
button.pack()
frame1.pack(padx=15,pady=15)
label = Label(frame1)


mainloop()
