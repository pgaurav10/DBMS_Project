# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 11:39:48 2017

@author: Gaurav
"""
from tkinter import *
from tkinter import messagebox
import backend

def get_selected_row(event):
    global selected_tuple
    index=list1.curselection()[0]
    selected_tuple=list1.get(index)
    e1.delete(0,END)
    e1.insert(END,selected_tuple[1])
    e2.delete(0,END)
    e2.insert(END,selected_tuple[2])
    e3.delete(0,END)
    e3.insert(END,selected_tuple[3])
    e4.delete(0,END)
    e4.insert(END,selected_tuple[4])

def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    #quantity_int=int(quantity_text.get())
    #price_int=int(price_text.get())
    for row in backend.search(title_text.get(),author_text.get(),quantity_text.get(),price_text.get()):
        list1.insert(1,row)

def add_command():
    quantity_int=int(quantity_text.get())
    price_int=int(price_text.get())
    backend.insert(title_text.get(),author_text.get(),quantity_int,price_int)
    list1.delete(0,END)
    list1.insert(END,(title_text.get(),author_text.get(),quantity_int,price_int))

def delete_command():
    backend.delete(selected_tuple[0])

def update_command():
    quantity_int=int(quantity_text.get())
    price_int=int(price_text.get())
    backend.update(selected_tuple[0],title_text.get(),author_text.get(),quantity_int,price_int)

def buy_command():
    temp1=quantity_text.get()
    val1=int(temp1)
    price_int=int(price_text.get())
    if val1 == 0:
        backend.delete(selected_tuple[0])
        messagebox.showerror("ERROR!!!","Out of stock!!!")
    else:
        new_quantity=val1-1
        backend.update(selected_tuple[0],title_text.get(),author_text.get(),new_quantity,price_int)

def total_command():
    value=backend.total()
    list1.delete(0,END) 
    list1.insert(1,value)

def max_command():
    value=backend.maxval()
    list1.delete(0,END) 
    list1.insert(1,value)
    
def min_command():
    value=backend.minval()
    list1.delete(0,END) 
    list1.insert(1,value)   
    
window=Tk()

window.wm_title("BookStore")

l1=Label(window,text="Title")
l1.grid(row=0,column=0)

l2=Label(window,text="Author")
l2.grid(row=0,column=2)

l3=Label(window,text="Quantity")
l3.grid(row=1,column=0)

l4=Label(window,text="Price")
l4.grid(row=1,column=2)

title_text=StringVar()
e1=Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)

author_text=StringVar()
e2=Entry(window,textvariable=author_text)
e2.grid(row=0,column=3)

quantity_text=StringVar()
e3=Entry(window,textvariable=quantity_text)
e3.grid(row=1,column=1)

price_text=StringVar()
e4=Entry(window,textvariable=price_text)
e4.grid(row=1,column=3)

list1=Listbox(window, height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

b1=Button(window,text="View all", width=12,command=view_command)
b1.grid(row=2,column=3)

b2=Button(window,text="Search entry", width=12,command=search_command)
b2.grid(row=3,column=3)

b3=Button(window,text="Add entry", width=12,command=add_command)
b3.grid(row=4,column=3)

b4=Button(window,text="Update selected", width=12,command=update_command)
b4.grid(row=5,column=3)

b5=Button(window,text="Delete selected", width=12,command=delete_command)
b5.grid(row=6,column=3)

b6=Button(window,text="Buy",width=12,command=buy_command)
b6.grid(row=7,column=3)

b7=Button(window,text="Total",width=12,command=total_command)
b7.grid(row=8,column=0)

b8=Button(window,text="Max. Price",width=12,command=max_command)
b8.grid(row=8,column=1,columnspan=2)

b9=Button(window,text="Min. Price",width=12,command=min_command)
b9.grid(row=8,column=3)

window.mainloop()

