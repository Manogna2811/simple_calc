from tkinter import *
root=Tk()
e=Entry(root,width=50,borderwidth=5)
e.grid(row=0,column=0,columnspan=5,padx=20,pady=10)
root.iconbitmap('caluculator.ico')
root.title("mini@caluculator")
root.resizable(0,0)

def button_click(number):
    current=e.get()
    e.delete(0, END)
    e.insert(0,str(current)+str(number))
def button_clear():
    e.delete(0,END)

def button_add():
   fn=e.get() 
   global f_num
   global math 
   math="addition"
   f_num = int(fn)
   e.delete(0,END)

def button_sub():
    fn=e.get()
    global f_num
    global math 
    math="substraction"
    f_num = int(fn)
    e.delete(0,END)

def button_mul():
    fn=e.get() 
    global f_num
    global math 
    math="multiply"
    f_num = int(fn)
    e.delete(0,END)

def button_div():
    fn=e.get() 
    global f_num
    global math 
    math="division"
    f_num = int(fn)
    e.delete(0,END)

def button_modulo():
    fn=e.get() 
    global f_num
    global math 
    math="modulo"
    f_num = int(fn)
    e.delete(0,END)
   

def button_equal():
    second_number=e.get()
    e.delete(0,END)
    if math=="addition":
        e.insert(0,f_num+int(second_number))   
    if math=="substraction"  :
        e.insert(0,f_num-int(second_number))
    if math=="division":
        e.insert(0,f_num/int(second_number))
    if math=="multiply":
        e.insert(0,f_num*int(second_number))      
    if math=="modulo":
        e.insert(0,f_num%int(second_number))
       

button1 = Button(root,text="1",padx=30,pady=10,command=lambda: button_click(1),fg="black",bg="HotPink4")
button2 = Button(root,text="2",padx=30,pady=10,command=lambda: button_click(2),fg="black",bg="HotPink4")
button3 = Button(root,text="3",padx=30,pady=10,command=lambda: button_click(3),fg="black",bg="HotPink4")
button4 = Button(root,text="4",padx=30,pady=10,command=lambda: button_click(4),fg="black",bg="HotPink4")
button5 = Button(root,text="5",padx=30,pady=10,command=lambda: button_click(5),fg="black",bg="HotPink4")
button6 = Button(root,text="6",padx=30,pady=10,command=lambda: button_click(6),fg="black",bg="HotPink4")
button7 = Button(root,text="7",padx=30,pady=10,command=lambda: button_click(7),fg="black",bg="HotPink4")
button8 = Button(root,text="8",padx=30,pady=10,command=lambda: button_click(8),fg="black",bg="HotPink4")
button9 = Button(root,text="9",padx=30,pady=10,command=lambda: button_click(9),fg="black",bg="HotPink4")
button0 = Button(root,text="0",padx=30,pady=10,command=lambda: button_click(0),fg="black",bg="HotPink4")
button11 = Button(root,text="+",padx=30,pady=10,command= button_add,fg="black",bg="HotPink4")
button13 = Button(root,text="/",padx=30,pady=10,command=button_div,fg="black",bg="HotPink4")
button12= Button(root,text="-",padx=30,pady=10,command=button_sub,fg="black",bg="HotPink4")
button14= Button(root,text="*",padx=30,pady=10,command=button_mul,fg="black",bg="HotPink4")
button15= Button(root,text="=",padx=30,pady=10,command=button_equal,fg="black",bg="HotPink4")
button17= Button(root,text="%",padx=30,pady=10,command=button_modulo,fg="black",bg="HotPink4")
button16= Button(root,text="clear",padx=100,pady=10,command=button_clear,fg="black",bg="HotPink4")
#put buttons on screen
button1.grid(row=3,column=1)
button2.grid(row=3,column=2)
button3.grid(row=3,column=3)
button4.grid(row=2,column=1)
button5.grid(row=2,column=2)
button6.grid(row=2,column=3)
button7.grid(row=1,column=1)
button8.grid(row=1,column=2)
button9.grid(row=1,column=3)
button0.grid(row=4,column=1)
button11.grid(row=4,column=2)
button12.grid(row=4,column=3)
button13.grid(row=1,column=4)
button14.grid(row=2,column=4)
button15.grid(row=3,column=4)
button17.grid(row=4,column=4)
button16.grid(row=5,column=1,columnspan=4)

root.mainloop()



