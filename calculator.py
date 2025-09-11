from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Calculator")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky="N W E S")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

result = IntVar()
inp1 = IntVar()
inp2 = IntVar()
op = StringVar()
nmp = IntVar()
opv1 = IntVar()
opv2 = StringVar()

def add(*args):
    inp2.set(inp1.get())
    op.set("add")
    opv2.set("+")
    inp1.set(0)
def sub(*args):
    inp2.set(inp1.get())
    op.set("sub")
    opv2.set("-")
    inp1.set(0)
def into(*args):
    inp2.set(inp1.get())
    op.set("into")
    opv2.set("x")
    inp1.set(0)
def div(*args):
    inp2.set(inp1.get())
    op.set("div")
    opv2.set("/")
    inp1.set(0)
def ans(*args):
    opv1.set(inp1.get())
    print(op.get())
    if op.get() == "add":
        result.set(inp2.get()+inp1.get())
        inp1.set(0)
    elif op.get() == "sub":
        result.set(inp2.get()-inp1.get())
        inp1.set(0)
    elif op.get() == "into":
        result.set(inp2.get()*inp1.get())
        inp1.set(0)
    elif op.get() == "div":
        result.set(inp2.get()/inp1.get())
        inp1.set(0)

def clear(*args):
    result.set(int(result.get()-result.get()))
    inp2.set(inp2.get()-inp2.get())
    opv1.set(opv1.get()-opv1.get())
def numpad1(*args):
    nmp.set(1)
    if inp1.get() == 0:
        inp1.set(inp1.get()+nmp.get())
    else:
        inp1.set(inp1.get()*10+nmp.get())

def numpad2(*args):
    nmp.set(2)
    if inp1.get() == 0:
        inp1.set(inp1.get()+nmp.get())
    else:
        inp1.set(inp1.get()*10+nmp.get())

def numpad3(*args):
    nmp.set(3)
    if inp1.get() == 0:
        inp1.set(inp1.get()+nmp.get())
    else:
        inp1.set(inp1.get()*10+nmp.get())

def numpad4(*args):
    nmp.set(4)
    if inp1.get() == 0:
        inp1.set(inp1.get()+nmp.get())
    else:
        inp1.set(inp1.get()*10+nmp.get())

def numpad5(*args):
    nmp.set(5)
    if inp1.get() == 0:
        inp1.set(inp1.get()+nmp.get())
    else:
        inp1.set(inp1.get()*10+nmp.get())

def numpad6(*args):
    nmp.set(6)
    if inp1.get() == 0:
        inp1.set(inp1.get()+nmp.get())
    else:
        inp1.set(inp1.get()*10+nmp.get())

def numpad7(*args):
    nmp.set(7)
    if inp1.get() == 0:
        inp1.set(inp1.get()+nmp.get())
    else:
        inp1.set(inp1.get()*10+nmp.get())

def numpad8(*args):
    nmp.set(8)
    if inp1.get() == 0:
        inp1.set(inp1.get()+nmp.get())
    else:
        inp1.set(inp1.get()*10+nmp.get())

def numpad9(*args):
    nmp.set(9)
    if inp1.get() == 0:
        inp1.set(inp1.get()+nmp.get())
    else:
        inp1.set(inp1.get()*10+nmp.get())

def numpad0(*args):
    nmp.set(0)
    if inp1.get() == 0:
        inp1.set(inp1.get()+nmp.get())
    else:
        inp1.set(inp1.get()*10+nmp.get())

ttk.Entry(mainframe, textvariable=inp1).grid(column=0, row=0)
ttk.Label(mainframe, textvariable=opv1).grid(column=1, row=0, sticky=W)
ttk.Label(mainframe, textvariable=opv2).grid(column=1, row=0, sticky=E)
ttk.Label(mainframe, textvariable=inp2).grid(column=2, row=0)
ttk.Label(mainframe, text="=").grid(column=3, row=0)
ttk.Label(mainframe, textvariable=result).grid(column=4, row=0)

ttk.Button(mainframe, text="+", command=add).grid(column=0 , row=1)
ttk.Button(mainframe, text="-", command=sub).grid(column=0 , row=2)
ttk.Button(mainframe, text="x", command=into).grid(column=0 , row=3)
ttk.Button(mainframe, text="/", command=div).grid(column=0, row=4)
ttk.Button(mainframe, text="1", command=numpad1).grid(column=1 , row=1)
ttk.Button(mainframe, text="4", command=numpad4).grid(column=1 , row=2)
ttk.Button(mainframe, text="7", command=numpad7).grid(column=1 , row=3)
ttk.Button(mainframe, text="Clear", command=clear).grid(column=1 , row=4)
ttk.Button(mainframe, text="2", command=numpad2).grid(column=2 , row=1)
ttk.Button(mainframe, text="5", command=numpad5).grid(column=2 , row=2)
ttk.Button(mainframe, text="8", command=numpad8).grid(column=2 , row=3)
ttk.Button(mainframe, text="0", command=numpad0).grid(column=2 , row=4)
ttk.Button(mainframe, text="3", command=numpad3).grid(column=3 , row=1)
ttk.Button(mainframe, text="6", command=numpad6).grid(column=3 , row=2)
ttk.Button(mainframe, text="9", command=numpad9).grid(column=3 , row=3)
ttk.Button(mainframe, text="=", command=ans).grid(column=3 , row=4)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.mainloop()
