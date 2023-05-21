import tkinter as tk
from tkinter import *
from tkinter.filedialog import asksaveasfile
from tkinter import filedialog
from tkinter.filedialog import askopenfilename

# from Tkinter import *

def donothing():
   print("nothing")


def open_file(): 
   fn = askopenfilename()
   f = open(fn,"r")
  
   text_box.insert(0.0,f.read())
   file_name = fn.split("/")[-1]
   name = file_name.split(".txt")
   
   
   root.title(listToString(name))
   
   f.close

   # print("open")

def overite_saved_file():
   pass

#Define the function #used to save a txt file to the pc
def save_file():
   f = asksaveasfile(initialfile = 'Untitled.txt',
    defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
   f.write(text_box.get(1.0, "end-1c"))
   f.close
   
    
   
def print_input():
   print(text_box.get(1.0, "end-1c"))

def listToString(s):
   
    # initialize an empty string
    str1 = " "
   
    # return string 
    return (str1.join(s))

root = Tk()
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=open_file)
filemenu.add_command(label="Save", command=save_file)
filemenu.add_command(label="Save as...", command=save_file)
filemenu.add_command(label="Close", command=donothing)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)

editmenu.add_separator()

editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)

menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)


text_box = tk.Text()
text_box.pack()



#goes last
# Set window size
root.geometry("500x300")
root.title("Notes")
root.config(menu=menubar)
root.mainloop()



