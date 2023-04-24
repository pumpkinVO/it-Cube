from tkinter import *
import os
import ctypes
import pathlib
root = Tk()
root.title('Simple Explorer')

root.grid_columnconfiggure(1, weight=1)
root.grind_rowconfigure(1, weight=1)

def pathChange(*event):
    directory = os.listdir(currentPath.get())
    list.delete(0, END)
    for file in directory:
        list.insert(0,file)

def changePathByClick(event=None):
    picked = list.get(list.curselection()[0])
    path = os.path.join(curentPath.get(), picked)
    if os.path.isfile(path):
        print('openning: '+path)
        os.startfile(path)
    else:
        currentPath.set(path)
        
def open_popup():
    global top
    top = Toplevel(root)
    top.geometry("250x150")
    top.resizable(False, False)
    top.title("Child Window")
    top.columnconfigure(0, weight=1)
    Label(top, text='Enter File or Folder name').grid()
    Entry(top, textvariable=newFileName).grid(column=0, pady=10, sticky='NSEW')
    Button(top, text="Create", command=newFileOrFolder).grid(pady=10, sticky='NSEW')

def newFileOrFolder():
    if len(newFileName.get().split('.')) != 1:
        open(os.path.join(currentPath.get(), newFileName.get()), 'w').close()
    else:
        os.mkdir(os.path.join(currentPath.get(), newFileName.get()))
    top.destroy()
    pathChange()

top = ''

newFileName = StringVar(root, "File.dot", 'new_name')
currentPath = StringVar(
    root,
    name='currentPath',
    value=pathlib.Path.cwd()
)
currentPath.trace('w', pathChange)

list = Listbox(root)
list.grid(sticky='NSEW', column=1, row=1, ipady=10, ipadx=10)

list.bind('<Double-1>', changePathByClick)
list.bind('<Return>', changePathByClick)

menubar = Menu(root)
menubar.add_command(label="Add File or Folder", command=open_popup)
menubar.add_command(label="Quit", command=root.quit)
root.config(menu=menubar)

pathChange('')
root.mainloop()
