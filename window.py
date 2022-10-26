import codecs
import json
import pygame
import tkinter as tk
from version_info import print_version
import time as time_controller

json_file = codecs.open("assets\\project_data.json", "r+")
with json:
    data = json.read(json_file)
window = tk.Tk()
window.title("Scratch 2 Offline Editor written in Python 3.10.8")
print_version()
time_controller.sleep(2)
print("Starting editor . . .")
time_controller.sleep(6)
is_window_open = True
window.mainloop()
is_window_open = False
print("Editor exited")
time_controller.sleep(2)
print("Thanks for using the Scratch 2 Offline Editor written in Python 3.10.8.\nWe hope you have a nice day! "
      "😃\nScratch will appreciate this... err... maybe.")
time_controller.sleep(2)
print("Aborting . . .")
time_controller.sleep(6)
