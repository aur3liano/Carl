# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 10:18:43 2020

@author: Justin Paul
"""

def main():
    import tkinter as tk
    
    class Lbl_Clk_Exp():
        def __init__(self):
            self.set_up_gui()
    
        def edit(self, event):
            print(event.char)
        
        def prep(self, event):
            
            if event.widget.notclicked:
                event.widget.notclicked = False
                event.widget.config(bg='light blue')
                event.widget.focus_set()  # give keyboard focus to the label
                event.widget.bind('<Key>', self.edit)
            else:
                event.widget.notclicked = True
                event.widget.config(bg='black')
                event.widget.focus_set()  # give keyboard focus to the label
                event.widget.bind('<Key>', self.edit)
                
        def set_up_gui(self):
            root = tk.Tk()
            frame = tk.Frame(root)
            frame.pack()
            
            example = tk.Label(frame, text='Click me')
            example.pack()
            example.bind('<Button-1>', self.prep)
            example.notclicked = True
    
    my_exmaple = Lbl_Clk_Exp()
    tk.mainloop()
    
    return(1)

main()

'''

import tkinter as tk
root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

def edit(event):
    print(event.char)

def prep(event):
    
    if event.widget.notclicked:
        event.widget.notclicked = False
        event.widget.config(bg='light blue')
        event.widget.focus_set()  # give keyboard focus to the label
        event.widget.bind('<Key>', edit)
    else:
        event.widget.notclicked = True
        event.widget.config(bg='black')
        event.widget.focus_set()  # give keyboard focus to the label
        event.widget.bind('<Key>', edit)

example = tk.Label(frame, text='Click me')
example.pack()
example.bind('<Button-1>', prep)
example.notclicked = True
tk.mainloop()

'''