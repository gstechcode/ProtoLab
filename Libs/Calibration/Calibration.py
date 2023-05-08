from Libs.variables import *
from Libs.autoload import *
from tkinter import *
from tkinter import messagebox
import os, json, time, pyautogui

class Calibration: 
    def __init__(self):
        self.__coords__()
        if(self.calib == True):
            self.root= Tk()
            self.root.config(padx="30px", pady="30px")
            self.root.title("ProtLab - Calibração de Coords")
            frame= Frame(self.root)
            frame.pack()
            self.label= Label(frame, text=f"Coords Quad: {self.obj['quad'][0]},{self.obj['quad'][0]}", font="Arial 15")
            self.label.pack(pady="30px", padx="10px", side="left")
            self.btn= Button(frame, text="Alterar", command= self.changeCoord, bg="green", fg="white", relief="flat", font="Arial 15")
            self.btn.pack(pady="30px", side="left")
            self.root.mainloop()
    def changeCoord(self):
        messagebox.showinfo("ProtoLab", "Você terá 5 segundos para selecionar a coordenada nova.")
        time.sleep(5)
        coord= (pyautogui.position().x,pyautogui.position().y)
        op= messagebox.askyesno("ProtoLab - Adicionar coordenada", "Adicionar coordenada nova?")
        if(op):
            self.obj["quad"]= coord
            arq= open(os.getcwd() + "/Resources/Databases/protocoords.json","w")
            arq.write(json.dumps(self.obj))
            arq.close()
            self.label["text"]= f"Coords Quad: {self.obj['quad'][0]},{self.obj['quad'][0]}"
        else:
            messagebox.showwarning("ProtoLab - Coordenada não adicionada","A coordenada não foi alterada")
    def __coords__(self):
        if(os.path.exists(os.getcwd() + "/Resources/Databases/protocoords.json")):
            arq= open(os.getcwd() + "/Resources/Databases/protocoords.json","r")
            self.obj= json.loads(arq.readlines()[0])
            arq.close()
            try:
                self.obj["quad"]
            except KeyError:
                obj= {
                    "quad": (0,0)
                }
                arq= open(os.getcwd() + "/Resources/Databases/protocoords.json","w")
                arq.write(json.dumps(obj))
                arq.close()
        else:
            self.obj= {
                "quad": (0,0)
                }
            arq= open(os.getcwd() + "/Resources/Databases/protocoords.json","w")
            arq.write(json.dumps(self.obj))
            arq.close()
        
        self.calib= False        
        if(self.obj["quad"] == [0,0] or self.obj["quad"] == (0,0)):
            messagebox.showerror("ProtoLab - Coordenadas não calibradas", "Suas coordenadas não estão calibradas, por favor calibre-as.")
            self.calib= True
        