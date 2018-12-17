# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 15:58:43 2018

@author: Helder
"""

import tkinter as tk

class jan():
    def __init__(self):
        
        self.wdw = tk.Tk()
        self.wdw.title("Teste Label")
        
        self.txtVar = tk.StringVar()
        self.txtVar.set("blablabla")
        
        self.labelTexto = tk.Label(self.wdw,textvariable = self.txtVar,relief= tk.FLAT)
        self.labelTexto.grid(row = 1, column = 1)




if __name__ == "__main__":

    janela = jan()
    janela.wdw.mainloop()