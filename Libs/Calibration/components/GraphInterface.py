from tkinter import *


class GraphInterface:
    def __init__(self, title="Application", geometry="500x500", bg="#ccc") -> None:
        self.title= title
        self.bg= bg
        self.geometry= geometry
    def run(self) -> Tk:
        self.display= Tk()
        self.display.title(self.title)
        self.display.config(bg=self.bg,pady="30px")
        self.display.geometry(self.geometry)
        return self.display