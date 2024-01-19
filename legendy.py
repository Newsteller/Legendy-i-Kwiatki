import tkinter
import data_service

from tkinter import *
from data_service import get_game_item_object

root = Tk()
root.geometry("500x500")
root.title("Legendy i Kwiatki")
root.iconbitmap("logo.ico")

frame = Frame(root)
frame.pack()

buttonframe = Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

btn1 = Button(buttonframe, text="+", font=('arial', 18))
btn1.grid(row=0, column=0, sticky=W+E)

btn2 = Button(buttonframe, text="+", font=('arial', 18))
btn2.grid(row=0, column=1, sticky=W+E)

btn3 = Button(buttonframe, text="+", font=('arial', 18))
btn3.grid(row=0, column=2, sticky=W+E)

buttonframe.pack(fill='x', padx='20')

# anotherbutton = Button(root, text='Text')
# anotherbutton.place(x=200, y=100, height=100, width=100)

root.mainloop()




# layout = [
#     sg.Column
#     [sg.Text('Some text on Row 1')],
#     [sg.Text('Enter something on Row 2'), sg.InputText(), sg.InputText()],
#     [sg.Button('Ok'), sg.Button('Cancel')]
# ]

# window = sg.Window('Legendy i Kwiatki', layout)

# item_1 = get_game_item_object("https://www.warofdragons.com/artifact_info.php?artikul_id=3514")
# item_2 = get_game_item_object("https://www.warofdragons.com/artifact_info.php?artikul_id=3518")
# item_3 = get_game_item_object("https://www.warofdragons.com/artifact_info.php?artikul_id=3500")

# while True:
#     event, values = window.read()
#     if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
#         break
#     print('You entered ', values[0])

# window.close()



