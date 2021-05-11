from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Easy Image Viewer")

frame=LabelFrame(root,text = ";)",padx=10,pady=10)
frame.grid(padx=20,pady=20)

#read images

LoI = ['ATD','pm','Poznan','sarbsko','wyżły','Tatry_kwiecień19',
       'zakopianka','opactwo_w_Tyńcu']
path = "K:\\Zdjęcia\\TW\\vol 5\\"
for x in range(len(LoI)):
    LoI[x]=ImageTk.PhotoImage(Image.open(path+LoI[x]+'.JPG'))
#print(LoI)

#def functions
def back(im_nr):
    global label
    global b_forward
    global b_back

    label.grid_forget()
    label = Label(image=LoI[im_nr])
    b_forward = Button(root, text=">>",command=lambda: forward(im_nr+1))
    b_back = Button(root,text="<<",command=lambda: back(im_nr-1))

    if im_nr == 0: b_back = Button(root, text="<<",
                                               state=DISABLED)
    update_status(im_nr)
    update_et()
    
def forward(im_nr):
    global label
    global b_forward
    global b_back

    label.grid_forget()
    label = Label(image=LoI[im_nr])
    b_forward = Button(root, text=">>",command=lambda: forward(im_nr+1))
    b_back = Button(root,text="<<",command=lambda: back(im_nr-1))
    if im_nr == len(LoI)-1: b_forward = Button(root, text=">>",
                                               state=DISABLED)
    update_status(im_nr)
    update_et()

def update_status(nr):
    global status
    status = Label(root,text='Image {} of {}'.format(nr+1,len(LoI)),bd=1,relief=SUNKEN,
               anchor=W)
def update_et():
    status.grid(row=0,column=0,columnspan=30,sticky=W+E)
    label.grid(row=2, column=0, columnspan=30)
    b_forward.grid(row=1,column=2)
    b_back.grid(row=1, column=0)

    
#create label and button

status = Label(root,text='Image {} of {}'.format(1,len(LoI)),bd=1,relief=SUNKEN,
               anchor=W)
status.grid(row=0,column=0,columnspan=30,sticky=W+E)

label = Label(image=LoI[0])
label.grid(row=2, column=0, columnspan=30)

b_back = Button(root,text="<<",command=lambda: back(),state=DISABLED)
b_exit = Button(root,text='exit',command=root.quit)
b_forward=Button(root, text=">>",command=lambda: forward(1))

b_back.grid(row=1, column=0)
b_exit.grid(row=1,column=1)
b_forward.grid(row=1,column=2)

root.mainloop()
