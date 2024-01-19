import tkinter
import gui_util

from gui_util import setup_root, save_window_position, load_window_position

from tkinter import *
from tkinter import messagebox

class MyGUI:
    def __init__(self):
        self.root = Tk()
        setup_root(self)

        self.menubar = Menu(self.root)
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label='Close', command=self.on_closing)
        self.filemenu.add_separator()
        self.filemenu.add_command(label='Close', command=self.on_closing)

        self.actionmenu = Menu(self.menubar, tearoff=0)
        self.actionmenu.add_command(label='Action', command=self.show_message)

        self.menubar.add_cascade(menu=self.filemenu, label='File')
        self.menubar.add_cascade(menu=self.actionmenu, label='Action')

        self.root.config(menu=self.menubar)

        self.label = Label(self.root, text='message', font=('Arial', 18))
        self.label.pack(padx=10, pady=10)

        self.textbox = Text(self.root, height=5, font=('Arial', 18))
        self.textbox.pack(padx=10, pady=10)

        self.check_state = IntVar()

        self.check = Checkbutton(self.root, text='Test',  font=('Arial', 18), variable=self.check_state)
        self.check.pack(padx=10, pady=10)

        self.button = Button(self.root, text='Test',  font=('Arial', 18), command=self.show_message)
        self.button.pack(padx=10, pady=10)

        self.root.protocol('WM_DELETE_WINDOW', self.on_closing)
        load_window_position(self.root, 'window_position.config')
        self.root.mainloop()
    
    def show_message(self):
        print(self.check_state.get())
        if (self.check_state.get() == 0):
            print(self.textbox.get('1.0', END))
        else:
            messagebox.showinfo(title='message', message=self.textbox.get('1.0', END))

    def on_closing(self):
        if (messagebox.askyesno(title='Quit?', message='If you want to quit?')):
            save_window_position(self.root, 'window_position.config')
            self.root.destroy()

MyGUI()