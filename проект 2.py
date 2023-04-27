from tkinter import *
import os
import ctypes
import pathlib

ctypes.windll.shcore.SetProcessDpiAwareness(True)


def path_change(*event):
    directory = os.listdir(current_path.get())
    list.delete(0, END)

    for file in directory:
        list.insert(0, file)


def change_path_by_click(event=None):
    picked = list.get(list.curselection()[0])
    path = os.path.join(current_path.get(), picked)

    if os.path.isfile(path):
        os.startfile(path)
    else:
        current_path.set(path)


def go_back(event=None):
    new_path = pathlib.Path(current_path.get()).parent
    current_path.set(new_path)


def window_new_file_or_folder():
    global new_window
    new_window = Toplevel(root)
    new_window.geometry("250x150")
    new_window.resizable(0, 0)
    new_window.title("Новый файл/папка")

    new_window.columnconfigure(0, weight=1)

    Ladel(new_window, text='Введите название нового файла/папки').grid()
    Entry(new_window, textvariable=new_file_name).grid(column=0, pady=10, stiky=NSEW)
    Button(new_window, text="Создать", command=new_file_or_folder).grid(pady=10, sticky=NSEW)


def new_file_or_folder():
    if len(new_file_name.get().split('.')) !=1:
        open(os.path.join(current_path.get(), new_file_name.get()), 'w').close()
    else:
        os.mkdir(os.path.join(current_path.get(), new_file_name.get()))

    new_window.destroy()
    path_change()


root = Tk()
root.title('Проводник файлов')
root.geometry('400x250')

root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(1, weight=1)

new_window = ''

new_file_name = StringVar(root, "Блокнот.txt", 'new_name')
current_path = StringVar(root, name='current_path', value=pathlib.Path.cmd())

current_path.trace('w', path_change)

Button(root, text='Назад', command=go_back).grid(sticky=NSEW, column=0, row=0)

root.bind("<Alt-left>", go_back)

Button(root, text='Создать', command=window_new_file_or_folder).grid(sticky=NSEW, column=0, row=1)

Entry(root, textvariable=current_path).grid(sticky=NSEW, column=1, row=0, ipady=10, ipadx=10)

List = listbox(root)
List.grid(stiky=NSEW, column=1, row=1, ipady=10, ipadx=10)

list.bind('<Double-1>', change_path_by_click)
list.bind('<Return>', change_path_by_click)

path_change('')
root.mainloop()
