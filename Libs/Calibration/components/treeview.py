from tkinter import ttk
from tkinter import *
import pyautogui, time
from tkinter import messagebox

class treeview:
    def __init__(self, master: Frame, headers: list, content: list, **kwargs) -> None:
        self.kwargs= kwargs
        self.master= master
        self.headers= headers
        self.content= content
        
        self.treeview= ttk.Treeview(master, columns= headers, show="headings")
        self.treeview.pack()
        self.treeviewBasicConfiguration()
        self.treeview.bind("<Double-Button-1>", self.treeviewSelected)
        
    def treeviewBasicConfiguration(self):
        for i in self.headers:
            self.treeview.column(i, anchor="center")
            self.treeview.heading(i,text=i)
        for i in self.content:
            self.treeview.insert("",END, values= i)
        
    def getTreeview(self) -> ttk.Treeview:
        return self.treeview
    def treeviewSelected(self,event):
        itemSelecionado= self.treeview.item(self.treeview.selection()[0])["values"]
        while True:
            messagebox.showinfo("CompassX - Calibração de Coordenadas","Você terá 5 segundos para posicionar o mouse na coordenada desejada")
            time.sleep(5)
            coordCaptured= (pyautogui.position().x, pyautogui.position().y)
            if(messagebox.askyesno("CompassX - Coordenada capturada com sucesso!","Deseja salvar essa coordenada?")):
                self.kwargs["updateCoord"](itemSelecionado[0],coordCaptured)
                break
            else:
                pass