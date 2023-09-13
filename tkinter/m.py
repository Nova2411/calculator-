from tkinter import *
win=Tk()

win.configure(bg="#67797B")

#d4dfe1
#b6c4c7
#67797b
#054342
#052011

def click(number):
    current= e.get()
    e.delete(0, END)
    e.insert(0, str(current)+str(number))
    
def clear():
    e.delete(0, END)
    
def addition():
    num_1=e.get()
    global f_num
    global math
    math="add"
    f_num=int(num_1)
    e.delete(0, END)
    
def sub():
    num_1=e.get()
    global f_num
    global math
    math="sub"
    f_num=int(num_1)
    e.delete(0, END)
    
def multiplication():
    num_1=e.get()
    global f_num
    global math
    math="mul"
    f_num=int(num_1)
    e.delete(0, END)
    
def division():
    num_1=e.get()
    global f_num
    global math
    math="div"
    f_num=int(num_1)
    e.delete(0, END)

def func_1():
    #f=e.get()
    global var_1
    var_1 = float(e.get())


def func_2():
    #s=e.get()
    global var_2
    var_2 = float(e.get())
    #e.delete(0, END)


def func_3():
    #t=e.get()
    global var_3
    var_3 = float(e.get())
    #e.delete(0, END)

def CAGR():
    func_1()
    func_2()
    func_3()
    e.insert(0, ((var_1/var_2)**(1/var_3))-1 )

def equals():
    num_2=e.get()
    e.delete(0, END)
    if math == "add" :
        e.insert(0, f_num + int(num_2))
    if math == "sub":
        e.insert(0, f_num - int(num_2))
    if math == "mul":
        e.insert(0, f_num * int(num_2))
    if math == "div":
        e.insert(0, f_num / int(num_2))
    
e=Entry(win, width=40, borderwidth=5, bg="#B6C4C7")
e.grid(row=0 , column=0, columnspan=4)

btn1=Button(win, text="1", padx=35, pady=35, command=lambda: click(1), bg="#67797B", fg="#052011")
btn2=Button(win, text="2", padx=35, pady=35, command=lambda: click(2), bg="#67797B", fg="#052011")
btn3=Button(win, text="3", padx=35, pady=35, command=lambda: click(3), bg="#67797B", fg="#052011")
btn4=Button(win, text="4", padx=35, pady=35, command=lambda: click(4), bg="#67797B", fg="#052011")
btn5=Button(win, text="5", padx=35, pady=35, command=lambda: click(5), bg="#67797B", fg="#052011")
btn6=Button(win, text="6", padx=35, pady=35, command=lambda: click(6), bg="#67797B", fg="#052011")
btn7=Button(win, text="7", padx=35, pady=35, command=lambda: click(7), bg="#67797B", fg="#052011")
btn8=Button(win, text="8", padx=35, pady=35, command=lambda: click(8), bg="#67797B", fg="#052011")
btn9=Button(win, text="9", padx=35, pady=35, command=lambda: click(9), bg="#67797B", fg="#052011")
btn0=Button(win, text="0", padx=35, pady=35, command=lambda: click(0), bg="#67797B", fg="#052011")

btn_add=Button(win, text="+", padx=33, pady=35, command=addition, bg="#054342", fg="#67797B")
btn_sub=Button(win, text="-", padx=35, pady=35, command=sub, bg="#054342", fg="#67797B")
btn_mul=Button(win, text="x", padx=34, pady=35, command=multiplication, bg="#054342", fg="#67797B")
btn_div=Button(win, text="/", padx=35, pady=35, command=division, bg="#054342", fg="#67797B")

btn_equal=Button(win, text="=", padx=77, pady=35, command=equals, bg="#054342", fg="#67797B")
btn_clear=Button(win, text="clr", padx=32, pady=5, command=clear, bg="#052011", fg="#D4DFE1")

btn_cagr=Button(win, text="CAGR", padx=35, pady=35, command=CAGR, bg="#054342", fg="#67797B")

btn1.grid(row=1, column=0)
btn2.grid(row=1, column=1)
btn3.grid(row=1, column=2)
btn4.grid(row=2, column=0)
btn5.grid(row=2, column=1)
btn6.grid(row=2, column=2)
btn7.grid(row=3, column=0)
btn8.grid(row=3, column=1)
btn9.grid(row=3, column=2)
btn0.grid(row=4, column=0)

btn_add.grid(row=1, column=4)
btn_sub.grid(row=2, column=4)
btn_mul.grid(row=3, column=4)
btn_div.grid(row=4, column=4)

btn_cagr.grid(row=5, column=0)

btn_equal.grid(row=4, column=1, columnspan=3)
btn_clear.grid(row=0, column=4)


win.mainloop()