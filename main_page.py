import tkinter
import gui_util

from gui_util import setup_root, save_window_position, load_window_position

from tkinter import *

class MyGUI:
    def __init__(self):
        self.root = Tk()
        setup_root(self)

        self.frame = Frame(self.root)
        self.frame.pack()

        self.addbutton = Button(self.frame, text="+", padx="30", pady="30", command=self.choose_item)
        self.addbutton.pack()


        self.root.protocol('WM_DELETE_WINDOW', self.on_closing)
        load_window_position(self.root, 'window_position.config')
        self.root.mainloop()

    def on_closing(self):
        save_window_position(self.root, 'window_position.config')
        self.root.destroy()

    def choose_item(self):
        

MyGUI()