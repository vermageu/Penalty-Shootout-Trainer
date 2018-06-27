from tkinter import *

def onclick(numbers):
    global operator
    operator += str(numbers)
    text_input.set(operator)

def onclear():
    global operator
    operator = ""
    text_input.set(operator)

def onequals():
    global operator
    val=str(eval(operator))
    text_input.set(val)
    operator=""

cal = Tk()
cal.title("Calculator")
operator=""
text_input = StringVar()

txtDisplay = Entry(cal,font=('arial',20,'bold'), textvariable=text_input,bd=30,insertwidth=4,bg='powder blue',justify='right').grid(columnspan=4)

b7 = Button(cal,padx=16,pady=16,bd=10,fg="black",font=('arial',10,'bold'),text="7",bg="blue",command=lambda:onclick(7)).grid(row=1,column=2)
b8 = Button(cal,padx=16,pady=16,bd=10,fg="black",font=('arial',10,'bold'),text="8",bg="red",command=lambda:onclick(8)).grid(row=1,column=1)
b9 = Button(cal,padx=16,pady=16,bd=10,fg="black",font=('arial',10,'bold'),text="9",bg="light green",command=lambda:onclick(9)).grid(row=1,column=0)
badd = Button(cal,padx=16,pady=16,bd=10,fg="black",font=('arial',10,'bold'),text="+",bg="light yellow",command=lambda:onclick("+")).grid(row=1,column=3)

b6 = Button(cal,padx=16,pady=16,bd=10,fg="black",font=('arial',10,'bold'),text="6",bg="yellow",command=lambda:onclick(6)).grid(row=2,column=0)
b5 = Button(cal,padx=16,pady=16,bd=10,fg="black",font=('arial',10,'bold'),text="5",bg="violet",command=lambda:onclick(5)).grid(row=2,column=1)
b4 = Button(cal,padx=16,pady=16,bd=10,fg="black",font=('arial',10,'bold'),text="4",bg="orange",command=lambda:onclick(4)).grid(row=2,column=2)
bsub = Button(cal,padx=16,pady=16,bd=10,fg="black",font=('arial',10,'bold'),text="-",bg="pink",command=lambda:onclick("-")).grid(row=2,column=3)

b3 = Button(cal,padx=16,pady=16,bd=10,fg="black",font=('arial',10,'bold'),text="3",bg="cyan",command=lambda:onclick(3)).grid(row=3,column=0)
b2 = Button(cal,padx=16,pady=16,bd=10,fg="black",font=('arial',10,'bold'),text="2",bg="light green",command=lambda:onclick(2)).grid(row=3,column=1)
b1 = Button(cal,padx=16,pady=16,bd=10,fg="black",font=('arial',10,'bold'),text="1",bg="gold",command=lambda:onclick(1)).grid(row=3,column=2)
bmul = Button(cal,padx=16,pady=16,bd=10,fg="black",font=('arial',10,'bold'),text="*",bg="grey",command=lambda:onclick("*")).grid(row=3,column=3)

b0 = Button(cal,padx=16,pady=16,bd=10,fg="black",font=('arial',10,'bold'),text="0",bg="purple",command=lambda:onclick(0)).grid(row=4,column=0)
bc = Button(cal,padx=16,pady=16,bd=10,fg="black",font=('arial',10,'bold'),text="C",bg="white",command=onclear).grid(row=4,column=1)
beq = Button(cal,padx=16,pady=16,bd=10,fg="black",font=('arial',10,'bold'),text="=",bg="orange",command=onequals).grid(row=4,column=2)
bdiv = Button(cal,padx=16,pady=16,bd=10,fg="black",font=('arial',10,'bold'),text="/",bg="sky blue",command=lambda:onclick("/")).grid(row=4,column=3)

cal.mainloop()

