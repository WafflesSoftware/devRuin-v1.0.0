from tkinter import *
import tkinter.ttk as ttk
import tkinter.scrolledtext as scrolled_text
from tkinter import messagebox
import os


file_name = 0

name = 0


def run_config():
    messagebox.showerror("devRuin 1.0.0", "This feature coming soon...")


def run_debug():
    messagebox.showerror("devRuin 1.0.0", "This feature coming soon...")


def run_normal():
    os.system(f"{name}")
    print()
    print("Process finished.")
    print()


def save2():
    global name

    name = file_name.get()

    btn_run.place(x=100, y=3)

    btn_run_debug.place(x=195, y=3)

    btn_run_config.place(x=290, y=3)

    w_file = open(file_name.get(), "w")
    w_file.write(scr_text_code.get("1.0", "end"))
    w_file.close()


def save():
    global file_name

    save_file = Tk()
    save_file.geometry("300x50")
    save_file.title("Save file")

    file_name = ttk.Entry(save_file)
    file_name.pack()

    btn_save_inf = ttk.Button(save_file, text="SAVE", width=40, command=save2)
    btn_save_inf.pack()

    save_file.mainloop()


root = Tk()
root.geometry("800x600")
root.title("devRuin 1.0.0")

print("Terminal:")
print()
print("No process running.")
print()

menu_bar = Menu(root)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Save", command=save)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

scr_text_code = scrolled_text.ScrolledText(root, width=100, height=30, font="Helvetica 10")
scr_text_code.pack()

lbl_frame_tools = ttk.LabelFrame(root, text="Tools", width=705, height=50)
lbl_frame_tools.place(x=40, y=500)

btn_save = ttk.Button(lbl_frame_tools, text="Save", command=save)
btn_save.place(x=5, y=3)

btn_run = ttk.Button(lbl_frame_tools, text="Run Code", command=run_normal)

btn_run_debug = ttk.Button(lbl_frame_tools, text="Debug Code", command=run_debug)

btn_run_config = ttk.Button(lbl_frame_tools, text="Run Configs", command=run_config)

root.config(menu=menu_bar)
root.mainloop()
