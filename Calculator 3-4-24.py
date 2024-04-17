from tkinter import *

def click (event):
    global scvalue
    text=event.widget.cget("text")
    if text == '=':
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            try:
                value=eval(screen.get())
            except Exception as e:
                print (e)
                value="error"
        scvalue.set(value)
        screen.update()   
    elif text =="AC":
        scvalue.set("")
        screen.update()

    elif text =="C":
        current_text = scvalue.get()
        scvalue.set(current_text[:-1])
        screen.update()
        
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()                 

root = Tk ()
root.geometry("450x620")
root.minsize(445,615)
root.maxsize(455,625)
root.title("calculator")

scvalue=StringVar()
scvalue.set("")
screen=Entry(root,textvariable=scvalue,font="lucida 40 bold")
screen.pack(fill=X,ipadx=8,pady=10,padx=10)

f=Frame(root, bg='grey')
b=Button(f,text="AC",padx=1,pady=1,font="lucida 32 bold",bg='yellow',fg='white',height=1)
b.pack(side=LEFT,padx=12,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="C",padx=2,pady=1,font="lucida 35 bold",bg='yellow',fg='white')
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="*",padx=2,pady=1,font="lucida 35 bold",bg='blue',fg='white' ,width=2)
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="/",padx=2,pady=1,font="lucida 35 bold",bg='blue',fg='white' ,width=2)
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
f.pack()

f=Frame(root, bg='grey')

b=Button(f,text="9",padx=2,pady=1,font="lucida 35 bold" ,width=2)
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text='8',padx=2,pady=1,font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text='7',padx=2,pady=1,font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="+",padx=4,pady=1,font="lucida 35 bold",bg='blue',fg='white')
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
f.pack()

f=Frame(root, bg='grey')

b=Button(f,text="4",padx=2,pady=1,font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="5",padx=2,pady=1,font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="6",padx=2,pady=1,font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="-",padx=4,pady=1,font="lucida 35 bold",bg='blue',fg='white' ,width=2)
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
f.pack()

f=Frame(root, bg='grey')

b=Button(f,text="1",padx=2,pady=1,font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="2",padx=2,pady=1,font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="3",padx=2,pady=1,font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text=".",padx=4,pady=1,font="lucida 35 bold",bg='blue',fg='white' ,width=2)
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
f.pack()

f=Frame(root, bg='grey')
b=Button(f,text="00",padx=19,pady=1,font="lucida 34 bold" ,fg='blue',width=5)
b.pack(side=LEFT,padx=16,pady=2)
b.bind("<Button-1>",click)

b=Button(f,text="0",padx=2,pady=1,font="lucida 35 bold",fg='blue')
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="=",padx=2,pady=1,font="lucida 35 bold" ,bg='lightblue',fg='white')
b.pack(side=LEFT,padx=19,pady=5)
b.bind("<Button-1>",click)
f.pack()

root.mainloop()
