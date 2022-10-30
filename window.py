import codecs
import json
import pygame
from tkinter import *
from version_info import print_version
import time as time_controller
from tkinter import ttk


#json_file = codecs.open(".\\assets\\project_data.json", "r+")
#with json:
#    data = json.read(json_file)
editor = Tk()
editor.geometry("1000x700")
editor.state('zoomed')
editor.title("Scratch 2 Offline Editor written in Python 3.10.8")
# create styling
styl = ttk.Style()
styl.configure('TSeparator', background='grey')
w = Canvas(editor, width=1500, height=1000)
w.create_rectangle(10, 5, 1490, 40, fill="grey", outline = 'grey')
w.create_rectangle(800, 50, 1490, 790, fill="lightgrey", outline = 'lightgrey')
w.create_rectangle(500, 50, 790, 790, fill="lightgrey", outline = 'lightgrey')
w.create_rectangle(10, 50, 490, 500, fill="white", outline = 'grey')
w.create_rectangle(10, 510, 490, 790, fill="white", outline = 'grey')
w.pack()
#ttk.Separator(    master=editor,    orient=VERTICAL,    style='TSeparator',    class_= ttk.Separator,    takefocus= 1,    cursor='man'    ).pack(fill=Y, pady=10, expand=True)
print_version()
time_controller.sleep(1)
print("Starting editor . . .")
time_controller.sleep(1)
is_editor_open = True
editor.mainloop()
is_editor_open = False
print("Editor exited")
time_controller.sleep(1)
print("Thanks for using the Scratch 2 Offline Editor written in Python 3.10.8.\nWe hope you have a nice day! "
      "😃\nScratch will appreciate this... err... maybe.")
time_controller.sleep(1)
print("Aborting . . .")
time_controller.sleep(1)
