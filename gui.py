import tkinter as tk
from tkinter import *
import datetime
from pynput.keyboard import Key, Listener
import os

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Logger")
        self.pack()
        self.create_widgets()
    
    def create_widgets(self):
        #self.datetimelabel = tk.Label(self)
        #self.datetimelabel["text"] = str(now.strftime("%d-%m-%y %H:%M"))
        #self.datetimelabel.pack(fill=X)
        self.label1 = tk.Label(self, text="Enter your log")
        self.label1.pack(fill=X)
        self.text = tk.Entry(self)
        self.text.pack(fill=X)
        self.text.focus_set()
        self.text.bind('<Return>', self.log)
        #self.button = tk.Button(text="Log", command=self.log)
        #self.button.pack(fill=X)
        
    
    def log(self, event=' '):
        content = str(now.strftime("%d-%m-%y %H:%M"))+" -->"+self.text.get() + "\n" +"-"*20 +"\n"
        file = open("/home/anuroop/keylogger.txt", "a")
        file.write(str(content))
        file.close()
        self.master.destroy()





now = datetime.datetime.now()
def on_press(key):
    if key == Key.f9:
        root = tk.Tk()
        app = Application(master=root)
        app.mainloop()
    pass
def on_release(key):
    pass
    #if key == Key.esc:
    #    return False

with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
