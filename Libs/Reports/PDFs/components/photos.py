import win32api
import win32gui
import pyautogui
from Libs.variables import *
import os, json
from tkinter import *
from tkinter import messagebox
from PIL import Image
import time

dc = win32gui.GetDC(0)

class photos(object):
    def runPhotos(self):
        self.profile()
        self.FT()
        self.PG()
        self.AF()
        self.FM()
        self.DPC()
        self.DH()
        self.POEF()
        self.INC()
        self.TM()
        self.PSGCF()
        self.ATMLEFT()
        self.ATMRIGHT()
        self.RIGHTMETR()
        self.LEFTMETR()
        self.PANRAD()
        self.RIGHTRAD()
        self.LEFTRAD()
        pass
    def messagebox(self, title: str, texto: str):
        i= Tk()
        i.title(title)
        i.iconbitmap(os.getcwd() + "/CompassX.ico")
        i.config(bg="orange", padx="30px", pady="30px")
        label= Label(i, text= texto, font="Arial 14", bg="orange", fg="white")
        label.pack(pady="20px")
        btn= Button(i, text="OK", font="Arial 14", bg="green", fg="white", relief="flat",command= i.destroy)
        btn.pack()
        i.mainloop()
    def profile(self):
        self.messagebox("Foto de Perfil","Faça o ajuste para fazer a captura da foto de perfil do paciente")
        self.quad()
        pyautogui.screenshot(os.getcwd() + "/Resources/Images/temp/profile.png", region=(self.PhotosInit[0],self.PhotosInit[1], int(39* DISPLAY[0]/100),int(39* DISPLAY[0]/100)))
    def FT(self):
        self.messagebox("Foto da Posição dos Gônios","Faça o ajuste para fazer a captura da foto da posição dos gônios do paciente")
        self.quad()
        pyautogui.screenshot(os.getcwd() + "/Resources/Images/temp/FT.png", region=(self.PhotosInit[0],self.PhotosInit[1], int(39* DISPLAY[0]/100),int(39* DISPLAY[0]/100)))
    def PG(self):
        pyautogui.screenshot(os.getcwd() + "/Resources/Images/temp/PG.png", region=(self.PhotosInit[0],self.PhotosInit[1], int(39* DISPLAY[0]/100),int(39* DISPLAY[0]/100)))
    def DH(self):
        self.messagebox("Dimensões das Hemi-Mandíbulas","Faça o ajuste para fazer a captura da foto das Hemi-Mandíbulas")
        self.quad()
        pyautogui.screenshot(os.getcwd() + "/Resources/Images/temp/DH.png", region=(self.PhotosInit[0],self.PhotosInit[1], int(39* DISPLAY[0]/100),int(39* DISPLAY[0]/100)))
    def DPC(self):
        self.messagebox("Distância Dentes P. Coronal","Faça o ajuste para fazer a captura da foto da Distância Dentes P. Coronal")
        self.quad()
        pyautogui.screenshot(os.getcwd() + "/Resources/Images/temp/DPC.png", region=(self.PhotosInit[0],self.PhotosInit[1], int(39* DISPLAY[0]/100),int(39* DISPLAY[0]/100)))
    def AF(self):
        self.messagebox("Foto da Altura Facial e Forma da Mandibula","Faça o ajuste para fazer a captura da foto da altura facial e forma da mandibula")
        self.quad()
        pyautogui.screenshot(os.getcwd() + "/Resources/Images/temp/AF.png", region=(self.PhotosInit[0],self.PhotosInit[1], int(39* DISPLAY[0]/100),int(39* DISPLAY[0]/100)))
    def FM(self):
        #self.messagebox("Forma da Mandíbula","Faça o ajuste para fazer a captura da foto da forma da mandíbula")
        #self.quad()
        pyautogui.screenshot(os.getcwd() + "/Resources/Images/temp/FM.png", region=(self.PhotosInit[0],self.PhotosInit[1], int(39* DISPLAY[0]/100),int(39* DISPLAY[0]/100)))
    def POEF(self):
        self.messagebox("POEF","Faça o ajuste para fazer a captura da foto do POEF")
        self.quad()
        pyautogui.screenshot(os.getcwd() + "/Resources/Images/temp/POEF.png", region=(self.PhotosInit[0],self.PhotosInit[1], int(39* DISPLAY[0]/100),int(39* DISPLAY[0]/100)))
    def INC(self):
        self.messagebox("Incisivos","Faça o ajuste para fazer a captura da foto dos incisivos")
        self.quadFull()
        coords= (self.PhotosInitFull[0],self.PhotosInitFull[1], self.PhotosFinalFull[0] - self.PhotosInitFull[0],self.PhotosFinalFull[1] - self.PhotosInitFull[1])
        pyautogui.screenshot(os.getcwd() + "/Resources/Images/temp/INC.png", region= coords)
    def TM(self):
        self.messagebox("Triangulo Mandibular","Faça o ajuste para fazer a captura da foto do triangulo mandibular")
        self.quad()
        coords= (self.PhotosInit[0],self.PhotosInit[1], int(39* DISPLAY[0]/100),int(39* DISPLAY[0]/100))
        pyautogui.screenshot(os.getcwd() + "/Resources/Images/temp/TM.png", region= coords)
    def PSGCF(self):
        #self.messagebox("Posições Sagitais - Gônios, Capitulares e F. Mentonianos","Faça o ajuste para fazer a captura da foto das posições sagitais")
        #self.quadFull()
        coords= (self.PhotosInit[0],self.PhotosInit[1], int(39* DISPLAY[0]/100),int(39* DISPLAY[0]/100))
        pyautogui.screenshot(os.getcwd() + "/Resources/Images/temp/PSGCF.png", region= coords)
    def RIGHTMETR(self):
        self.messagebox("Reconstrução da Superficie","Faça o ajuste para fazer a captura da foto direita com medidas")
        self.quadFull()
        coords= (self.PhotosInitFull[0],self.PhotosInitFull[1], self.PhotosFinalFull[0] - self.PhotosInitFull[0],self.PhotosFinalFull[1] - self.PhotosInitFull[1])
        pyautogui.screenshot(os.getcwd() + "/Resources/Images/temp/RIGHTMETR.png", region= coords)

    def LEFTMETR(self):
        self.messagebox("Reconstrução da Superficie","Faça o ajuste para fazer a captura da foto esquerda com medidas")
        self.quadFull()
        coords= (self.PhotosInitFull[0],self.PhotosInitFull[1], self.PhotosFinalFull[0] - self.PhotosInitFull[0],self.PhotosFinalFull[1] - self.PhotosInitFull[1])
        pyautogui.screenshot(os.getcwd() + "/Resources/Images/temp/LEFTMETR.png", region= coords)
    
    def RIGHTRAD(self):
        self.messagebox("Reconstrução da Superficie","Faça o ajuste para fazer a captura da foto direita tomografica")
        self.quadFull()
        coords= (self.PhotosInitFull[0],self.PhotosInitFull[1], self.PhotosFinalFull[0] - self.PhotosInitFull[0],self.PhotosFinalFull[1] - self.PhotosInitFull[1])
        pyautogui.screenshot(os.getcwd() + "/Resources/Images/temp/RIGHTRAD.png", region= coords)
    def LEFTRAD(self):
        self.messagebox("Reconstrução da Superficie","Faça o ajuste para fazer a captura da foto esquerda tomografica")
        self.quadFull()
        coords= (self.PhotosInitFull[0],self.PhotosInitFull[1], self.PhotosFinalFull[0] - self.PhotosInitFull[0],self.PhotosFinalFull[1] - self.PhotosInitFull[1])
        pyautogui.screenshot(os.getcwd() + "/Resources/Images/temp/LEFTRAD.png", region= coords)
    def PANRAD(self):
        self.messagebox("Reconstrução da Superficie","Faça o ajuste para fazer a captura da foto tomografia panoramica")
        self.quadFull()
        coords= (self.PhotosInitFull[0],self.PhotosInitFull[1], self.PhotosFinalFull[0] - self.PhotosInitFull[0],self.PhotosFinalFull[1] - self.PhotosInitFull[1])
        pyautogui.screenshot(os.getcwd() + "/Resources/Images/temp/PANRAD.png", region= coords)
    def SOBREPOSICAO(self):
        self.quadFull()
        coords= (self.PhotosInitFull[0],self.PhotosInitFull[1], self.PhotosFinalFull[0],self.PhotosFinalFull[1])
        pyautogui.screenshot(os.getcwd() + "/Resources/Images/temp/SOBREPOSICAO.png", region= coords)
    def ATMLEFT(self):
        self.messagebox("ATM Esquerda","Faça o ajuste para fazer a captura da foto da ATM Esquerda")
        self.quadFull()
        coords= (self.PhotosInitFull[0],self.PhotosInitFull[1], self.PhotosFinalFull[0] - self.PhotosInitFull[0],self.PhotosFinalFull[1] - self.PhotosInitFull[1])
        pyautogui.screenshot(os.getcwd() + "/Resources/Images/temp/ATMLEFT.png", region= coords)
    def ATMRIGHT(self):
        self.messagebox("ATM Direito","Faça o ajuste para fazer a captura da foto da ATM Direito")
        self.quadFull()
        coords= (self.PhotosInitFull[0],self.PhotosInitFull[1], self.PhotosFinalFull[0] - self.PhotosInitFull[0],self.PhotosFinalFull[1] - self.PhotosInitFull[1])
        pyautogui.screenshot(os.getcwd() + "/Resources/Images/temp/ATMRIGHT.png", region= coords)
    def quad(self):
        arq= open(os.getcwd() + "/Resources/Databases/protocoords.json","r")
        db= json.loads(arq.readlines()[0])
        arq.close()
        InitPosition= (db["quad"][0],db["quad"][1])
        FinalPosition= (int(InitPosition[0] + ((39* DISPLAY[0]/100))),int(InitPosition[1] + ((39* DISPLAY[0]/100))))
        self.PhotosInit= InitPosition
        self.PhotosFinal= FinalPosition
        red = win32api.RGB(255, 0, 0)
        cont = 1
        while True:
            cont += 1
            for x1 in range(int(InitPosition[0]),int(FinalPosition[0])):
                win32gui.SetPixel(dc,x1,InitPosition[1] -1,red)
                win32gui.SetPixel(dc,x1,InitPosition[1] -2,red)
                win32gui.SetPixel(dc,x1,InitPosition[1] -3,red)
            
            for x2 in range(int(InitPosition[0]),int(FinalPosition[0])):
                win32gui.SetPixel(dc,x2,FinalPosition[1] +1,red)
                win32gui.SetPixel(dc,x2,FinalPosition[1] +2,red)
                win32gui.SetPixel(dc,x2,FinalPosition[1] +3,red)
                
            for y1 in range(int(InitPosition[1]),int(FinalPosition[1])):
                win32gui.SetPixel(dc,InitPosition[0] -1,y1,red)
                win32gui.SetPixel(dc,InitPosition[0] -2,y1,red)
                win32gui.SetPixel(dc,InitPosition[0] -3,y1,red)
                
            for y2 in range(int(InitPosition[1]),int(FinalPosition[1])):
                win32gui.SetPixel(dc,FinalPosition[0] +1,y2,red)
                win32gui.SetPixel(dc,FinalPosition[0] +2,y2,red)
                win32gui.SetPixel(dc,FinalPosition[0] +3,y2,red)
                
            if(cont > 50):
                break
    def quadFull(self):
        InitPosition= (263,121)
        FinalPosition= (1885,966)
        self.PhotosInitFull= InitPosition
        self.PhotosFinalFull= FinalPosition
        self.messagebox("Tudo pronto?","A captura será feita do retangulo completo do Vista Dent")
        time.sleep(2)
    def optimizeImages(self):
        self.convertImage(os.getcwd() + "/Resources/Images/temp/FT.png")
        self.convertImage(os.getcwd() + "/Resources/Images/temp/DPC.png", fullscreen= True)
        self.convertImage(os.getcwd() + "/Resources/Images/temp/PG.png")
        self.convertImage(os.getcwd() + "/Resources/Images/temp/DH.png")
        self.convertImage(os.getcwd() + "/Resources/Images/temp/AF.png")
        self.convertImage(os.getcwd() + "/Resources/Images/temp/FM.png")
        self.convertImage(os.getcwd() + "/Resources/Images/temp/POEF.png")
        self.convertImage(os.getcwd() + "/Resources/Images/temp/INC.png",fullscreen= True, filter= False)
        self.convertImage(os.getcwd() + "/Resources/Images/temp/TM.png", fullscreen= True)
        self.convertImage(os.getcwd() + "/Resources/Images/temp/PSGCF.png", fullscreen= True)
        self.convertImage(os.getcwd() + "/Resources/Images/temp/ATMLEFT.png", fullscreen= True, filter= False)
        self.convertImage(os.getcwd() + "/Resources/Images/temp/ATMRIGHT.png", fullscreen= True, filter= False)
        try:
            self.convertImage(os.getcwd() + "/Resources/Images/temp/SOBREPOSICAO.png")
        except Exception:
            pass

    def convertImage(self, path, tam= (700,700), fullscreen= False, tamprop= None, filter= True):
        if(fullscreen == False):
            imgresize= Image.open(path)
            imgresized= imgresize.resize(tam, Image.ANTIALIAS)
            imgresized.save(path)
        if(tamprop != None):
            imgresize= Image.open(path)
            width, height= imgresize.size
            if(tamprop < 0):
                pcent= abs(tamprop)/100
                width= width - (width * pcent)
                height= height - (height * pcent)
                tamanho= (int(width),int(height))
            else:
                pcent= abs(tamprop)/100
                width= width + (width * pcent)
                height= height + (height * pcent)
                tamanho= (int(width),int(height))
            imgresized= imgresize.resize(tamanho, Image.ANTIALIAS)
            imgresized.save(path)
        if(fullscreen == False or filter == True):
            img = Image.open(path)
            img = img.convert("RGBA")
            datas = img.getdata() 
            newData = [] 
            for item in datas:
                if (item[0] >= 0 and item[0] <= 60) and (item[1] >= 0 and item[1] <= 60) and (item[2] >= 0 and item[2] <= 60):
                    newData.append((255, 255, 255, 0)) 
                else: 
                    newData.append(item) 
            img.putdata(newData)
            path= path.replace(".jpg",".png")
            img.save(path)