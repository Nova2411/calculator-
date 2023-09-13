import tkinter as tk
root = tk.Tk()

e_1 = tk.Entry(root)
e_1.pack()
e_2 = tk.Entry(root)
e_2.pack()
e_3 = tk.Entry(root)
e_3.pack()

var_1 = 0
var_2 = 0
var_3 = 0


def func_1():
    global var_1
    var_1 = e_1.get()


def func_2():
    global var_2
    var_2 = e_2.get()


def func_3():
    global var_3
    var_3 = e_3.get()


def store_all():
    func_1()
    func_2()
    func_3()
    print(var_1)
    print(var_2)
    print(var_3)


b = tk.Button(root, text="get", width=10, command=store_all)
b.pack()

root.mainloop()