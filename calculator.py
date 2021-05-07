from tkinter import *

root = Tk()
root.title('Simple Calculator')

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_click(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current) + str(number))

def button_clear():
    e.delete(0,END)

def button_add():
    number = e.get()
    global f_num
    global math
    math = 'add'
    f_num = int(number)
    e.delete(0,END)

def button_eq():
    sec_num = e.get()
    e.delete(0,END)

    if math == 'add': 
        e.insert(0,f_num+int(sec_num))
    if math == 'sub': 
        e.insert(0,f_num-int(sec_num))
    if math == 'mul': 
        e.insert(0,f_num*int(sec_num))
    if math == 'div': 
        e.insert(0,f_num/int(sec_num))

def button_sub():
    number = e.get()
    global f_num
    global math
    math = 'sub'
    f_num = int(number)
    e.delete(0,END)

def button_mul():
    number = e.get()
    global f_num
    global math
    math = 'mul'
    f_num = int(number)
    e.delete(0,END)

def button_div():
    number = e.get()
    global f_num
    global math
    math = 'div'
    f_num = int(number)
    e.delete(0,END)

def func(x):
    return lambda: button_click(x)

b=[]
for x in range(10):
    f = func(x)
    b.append(Button(root,text=str(x),padx=40, pady=20, command=f))

b_add = Button(root,text='+',padx=39, pady=20, command=button_add)
b_eq = Button(root,text='=',padx=89, pady=20, command=button_eq)
b_clear = Button(root,text='Clear',padx=79, pady=20, command=button_clear)

b_sub = Button(root,text='-',padx=39, pady=20, command=button_sub)
b_mul = Button(root,text='*',padx=40, pady=20, command=button_mul)
b_div = Button(root,text='/',padx=41, pady=20, command=button_div)

b_quit = Button(root,text='Exit',padx=20, pady=20, command=root.quit)

for x in range(10):
    if x==0: b[x].grid(row=4 ,column=0)
    elif x<4: b[x].grid(row=3, column=x-1)
    elif x<7: b[x].grid(row=2 ,column=x-4)
    else: b[x].grid(row=1 ,column=x-7)

b_add.grid(row=5 ,column=0)
b_eq.grid(row=5 ,column=1, columnspan=2)
b_clear.grid(row=4 ,column=1, columnspan=2)

b_sub.grid(row=6 ,column=0)
b_mul.grid(row=6 ,column=1)
b_div.grid(row=6 ,column=2)

b_quit.grid(row=0 ,column = 3)


root.mainloop()
