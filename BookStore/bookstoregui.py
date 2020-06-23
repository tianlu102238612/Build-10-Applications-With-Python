#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 17:14:03 2020

@author: tianlu

GUI interfaces of book store:
    Book entity:title,author,year,ISBN
    Functions: CRUD and search

"""
from tkinter import *
import bookstorebackend

def get_selected_row(event):
    try:
        #set it as global, so it can be access outrside rhe function
        global selected_tuple
        #Return the indices of currently selected item,and get the first element in tuple
        index = bookListBox.curselection()[0]
        #get the book from index
        selected_tuple = bookListBox.get(index)
        #display the selected book artibutes in each entry
        titleEntry.delete(0,END)
        titleEntry.insert(END, selected_tuple[1])
        authorEntry.delete(0,END)
        authorEntry.insert(END, selected_tuple[2])
        yearEntry.delete(0,END)
        yearEntry.insert(END, selected_tuple[3])
        isbnEntry.delete(0,END)
        isbnEntry.insert(END, selected_tuple[4])
    except  IndexError:
        pass

def view_command():
    #empty the list box first
    bookListBox.delete(0,END)
    for row in bookstorebackend.view():
        #the new row will be put in the end
        bookListBox.insert(END,row)
        
def search_command():
    bookListBox.delete(0,END)
    #get user input
    for row in bookstorebackend.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        bookListBox.insert(END,row)
    

def add_command():
    newBook = bookstorebackend.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    bookListBox.delete(0,END)
    bookListBox.insert(END,newBook)
    
def delete_command():
    bookstorebackend.delete(selected_tuple[0])

    
def update_command():
    bookstorebackend.update(selected_tuple[0],titleEntry.get(),authorEntry.get(),yearEntry.get(),isbnEntry.get())
    


window = Tk()
window.wm_title("Book Store")

titleLabel = Label(window,text="Title")
titleLabel.grid(row=0,column=0)

authorLabel = Label(window,text="Author")
authorLabel.grid(row=0,column=2)

yearLabel = Label(window,text="Year")
yearLabel.grid(row=1,column=0)

isbnLabel = Label(window,text="ISBN")
isbnLabel.grid(row=1,column=2)

title_text = StringVar()
titleEntry = Entry(window,textvariable = title_text)
titleEntry.grid(row=0,column=1)

author_text = StringVar()
authorEntry = Entry(window,textvariable = author_text)
authorEntry.grid(row=0,column=3)

year_text = StringVar()
yearEntry = Entry(window,textvariable = year_text)
yearEntry.grid(row=1,column=1)

isbn_text = StringVar()
isbnEntry = Entry(window,textvariable = isbn_text)
isbnEntry.grid(row=1,column=3)

bookListBox = Listbox(window,height=10,width=35)
bookListBox.grid(row=3,column=0,rowspan=6,columnspan=2)
bookListBox.bind('<<ListboxSelect>>',get_selected_row)

scrollBooks = Scrollbar(window)
scrollBooks.grid(row=3,column=2,rowspan=6)

bookListBox.config(yscrollcommand=scrollBooks.set)
scrollBooks.config(command = bookListBox.yview)

b1 = Button(window,text="View all",width=12,command=view_command)
b1.grid(row=3,column=3)

b2 = Button(window,text="Search",width=12,command=search_command)
b2.grid(row=4,column=3)

b3 = Button(window,text="Add New",width=12,command=add_command)
b3.grid(row=5,column=3)

b4 = Button(window,text="Update",width=12,command=update_command)
b4.grid(row=6,column=3)

b5 = Button(window,text="Delete",width=12,command=delete_command)
b5.grid(row=7,column=3)

































window.mainloop()