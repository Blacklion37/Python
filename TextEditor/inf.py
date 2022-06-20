from sqlite3 import Row
from tkinter import *
import os
from tkinter.tix import COLUMN

class inf(Toplevel):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.title("О нас")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.geometry('400x225')
        self.resizable(False, False)
        
        self.image_about = PhotoImage(file="./Kaito.png")

        self.lbl_about = Label(self, image=self.image_about)
        self.lbl_about.pack(fill = BOTH, expand=True)
        
        
        
        #opts = { 'ipadx': 10, 'ipady': 10, 'fill': BOTH }

        self.lbl_text = Label(self.lbl_about, text='ФИО: Питателев Артём Владимирович', font='Impact 12', background='Yellow', foreground='Green', justify = CENTER)
        #self.lbl_text.pack(side=TOP, **opts)
        self.lbl_text.place(x=200, y=40, anchor="c")

        self.lbl_text_2 = Label(self.lbl_about, text='Группа: 208', font='Impact 12', background='Yellow', foreground='Green', justify = CENTER)
        #self.lbl_text_2.pack(side=TOP, **opts)
        self.lbl_text_2.place(x=200, y=90, anchor="c")

        self.lbl_text_3 = Label(self.lbl_about, text='e-mail: parmit1944@gmail.com', font='Impact 12', background='Yellow', foreground='Green', justify = CENTER)
        #self.lbl_text_3.pack(side=TOP, **opts)
        self.lbl_text_3.place(x=200, y=160, anchor="c")
        self.lbl_text_4 = Label(self.lbl_about, text='ИВПЭК 2022', font='Impact 12', background='Yellow', foreground='Green', justify = CENTER)
        #self.lbl_text_3.pack(side=TOP, **opts)
        self.lbl_text_4.place(x=200, y=210, anchor="c")
        
