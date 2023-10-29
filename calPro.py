import tkinter
import math

top=tkinter.Tk()

txtVar=tkinter.StringVar()
lblVar=tkinter.StringVar()

def btnOne():
    oldText=txtVar.get()
    if oldText=="0":
        txtVar.set("1")
    else:
        txtVar.set(oldText+"1")
def btnTwo():
    oldText=txtVar.get()
    if oldText=="0":
        txtVar.set("2")
    else:
        txtVar.set(oldText+"2")
def btnThree():
    oldText=txtVar.get()
    if oldText=="0":
        txtVar.set("3")
    else:
        txtVar.set(oldText+"3")
def btnFour():
    oldText=txtVar.get()
    if oldText=="0":
        txtVar.set("4")
    else:
        txtVar.set(oldText+"4")
def btnFive():
    oldText=txtVar.get()
    if oldText=="0":
        txtVar.set("5")
    else:
        txtVar.set(oldText+"5")
def btnSix():
    oldText=txtVar.get()
    if oldText=="0":
        txtVar.set("6")
    else:
        txtVar.set(oldText+"6")
def btnSeven():
    oldText=txtVar.get()
    if oldText=="0":
        txtVar.set("7")
    else:
        txtVar.set(oldText+"7")
def btnEight():
    oldText=txtVar.get()
    if oldText=="0":
        txtVar.set("8")
    else:
        txtVar.set(oldText+"8")
def btnNine():
    oldText=txtVar.get()
    if oldText=="0":
        txtVar.set("9")
    else:
        txtVar.set(oldText+"9")

def btnZero():
    oldText=txtVar.get()
    if oldText=="0":
        pass
    else:
        txtVar.set(oldText+"0")
def btnPlus():
    global FirstNumber
    FirstNumber = float(txtVar.get())
    txtVar.set("0")
    global Operation
    Operation = "+"
def btnMinus():
    global FirstNumber
    FirstNumber = float(txtVar.get())
    txtVar.set("0")
    global Operation
    Operation = "-"
def btnMulti():
    global FirstNumber
    FirstNumber = float(txtVar.get())
    txtVar.set("0")
    global Operation
    Operation = "*"
def btnDivide():
    global FirstNumber
    FirstNumber = float(txtVar.get())
    txtVar.set("0")
    global Operation
    Operation = "/"

def btnEqual():
    if Operation=="+":
        Result=FirstNumber+float(txtVar.get())
    if Operation=="-":
        Result=FirstNumber-float(txtVar.get())
    if Operation=="*":
        Result=FirstNumber*float(txtVar.get())
    if Operation=="/":
        Result=FirstNumber/float(txtVar.get())
    txtVar.set(Result)

def btnPlusMinus():
     txtVar.set((float(txtVar.get()))*(-1))

def btnOneByX():
    txtVar.set(1/(float(txtVar.get())))

def btnDOT():
    x = txtVar.get()
    if x.find(".") == -1:
        txtVar.set(x+".")

def btnBackSpace():
    x=txtVar.get()
    if len(x) > 1:
        txtVar.set(x[:-1])
    else:
        txtVar.set("0")
def btnCE():
    txtVar.set("0")
def btnC():
    global FirstNumber
    global Operation
    txtVar.set("0")
    FirstNumber=0
    Operation=""
def btnSqrt():
    result=math.sqrt(float(txtVar.get()))
    txtVar.set(result)
def MemorySave():
    global MemoryData
    MemoryData=txtVar.get()
    lblVar.set("M")
def MemoryRetrive():
    if lblVar.get()=="M":
        txtVar.set(MemoryData)

def MemoryClear():
    global MemoryData
    MemoryData=""
    lblVar.set("")

def MemoryPlus():
    global MemoryData
    if lblVar.get()=="M":
        MemoryData=float(MemoryData)+float(txtVar.get())
    else:
        MemoryData = 0 + float(txtVar.get())
    lblVar.set("M")
def MemoryMinus():
    global MemoryData
    if lblVar.get()=="M":
        MemoryData=float(MemoryData)-float(txtVar.get())
    else:
        MemoryData = 0 - float(txtVar.get())
    lblVar.set("M")

def ViewCommand():
    pass
def EditCommand():
    pass
def HelpCommand():
    pass
def AboutCalculator():
    HelpView=tkinter.Tk()
    HelpView.mainloop()
MenuBar=tkinter.Menu(top)

View = tkinter.Menu(MenuBar, tearoff=0)
View.add_command(label="Standard")
View.add_command(label="Scientific")
View.add_command(label="Statisics")
View.add_command(label="History")

View.add_separator()

View.add_command(label="Exit", command=top.quit)

MenuBar.add_cascade(label="View", menu=View)
#-------
Edit = tkinter.Menu(MenuBar, tearoff=0)
Edit.add_command(label="Copy")
Edit.add_command(label="Past")
Edit.add_separator()
Edit.add_command(label="History")

MenuBar.add_cascade(label="Edit", menu=Edit)
#-----
Help = tkinter.Menu(MenuBar, tearoff=0)
Help.add_command(label="View Help")
Help.add_separator()
Help.add_command(label="About Calculator", command=AboutCalculator)

MenuBar.add_cascade(label="Help", menu=Help)

top.config(menu=MenuBar)

Memory=tkinter.Label(top,textvariable=lblVar, width=4,text="")
txt=tkinter.Entry(top, textvariable=txtVar, width=30)
txtVar.set("0")
SQRT=tkinter.Button(top,width=4,text="Sqrt",command=btnSqrt)

SEVEN=tkinter.Button(top,width=4,text="7",command=btnSeven)
EIGHT=tkinter.Button(top,width=4,text="8",command=btnEight)
NINE=tkinter.Button(top,width=4,text="9",command=btnNine)
DIVIDE=tkinter.Button(top,width=4,text="/", command=btnDivide)
PERCENT=tkinter.Button(top,width=4,text="%")

FOUR=tkinter.Button(top,width=4,text="4",command=btnFour)
FIVE=tkinter.Button(top,width=4,text="5",command=btnFive)
SIX=tkinter.Button(top,width=4,text="6",command=btnSix)
MUL=tkinter.Button(top,width=4,text="*", command=btnMulti)
ONEBYX=tkinter.Button(top,width=4,text="1/x", command=btnOneByX)

ONE=tkinter.Button(top,width=4,text="1",command=btnOne)
TWO=tkinter.Button(top,width=4,text="2",command=btnTwo)
THREE=tkinter.Button(top,width=4,text="3",command=btnThree)
MINUS=tkinter.Button(top,width=4,text="-", command=btnMinus)
EQUAL=tkinter.Button(top,width=4,height=3,text="=",command=btnEqual)

ZERO=tkinter.Button(top,width=9,text="0",command=btnZero)
DOT=tkinter.Button(top,width=4,text=".",command=btnDOT)
PLUS=tkinter.Button(top,width=4,text="+",command=btnPlus)

Memory.grid(row=0,column=0)
txt.grid(row=0,column=1, columnspan=4)
SEVEN.grid(row=3,column=0)
EIGHT.grid(row=3,column=1)
NINE.grid(row=3,column=2)
DIVIDE.grid(row=3,column=3)
PERCENT.grid(row=3,column=4)

FOUR.grid(row=4,column=0)
FIVE.grid(row=4,column=1)
SIX.grid(row=4,column=2)
MUL.grid(row=4,column=3)
ONEBYX.grid(row=4,column=4)


ONE.grid(row=5,column=0)
TWO.grid(row=5,column=1)
THREE.grid(row=5,column=2)
MINUS.grid(row=5,column=3)
EQUAL.grid(row=5,column=4, rowspan=2)
ZERO.grid(row=6,column=0, columnspan=2)
DOT.grid(row=6,column=2)
PLUS.grid(row=6,column=3)

top.mainloop()

