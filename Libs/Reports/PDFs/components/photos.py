import win32api
import win32gui
import pyautogui
from Libs.variables import *
import os, json
from functools import partial
from tkinter import *
from tkinter import messagebox
from PIL import Image
import time

dc = win32gui.GetDC(0)

class photos(object):
    def runPhotos(self):
        '''
        self.responseask= ""
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
        '''
        pass
    def messagebox(self, title: str, texto: str):
        i= Tk()
        i.title(title)
        i.geometry("850x400")
        i.iconbitmap(os.getcwd() + "/CompassX.ico")
        i.config(bg="orange", padx="30px", pady="30px")
        label= Label(i, text= texto, wraplength= 700, font="Arial 14", bg="orange", fg="white")
        label.pack(pady="20px")
        btn= Button(i, text="OK", font="Arial 14", bg="green", fg="white", relief="flat",command= i.destroy)
        btn.pack()
        i.mainloop()
    def askmessagebox(self, title: str, texto: str):
        i= Tk()
        i.title(title)
        i.iconbitmap(os.getcwd() + "/CompassX.ico")
        i.config(bg="orange", padx="30px", pady="30px")
        label= Label(i, text= texto, font="Arial 14", bg="orange", fg="white")
        label.pack(pady="20px")
        frame= Frame(i, bg="orange")
        frame.pack()
        btn= Button(frame, text="Sim", font="Arial 14", bg="green", fg="white", relief="flat",command= partial(self.responseaskmessagebox, True, i))
        btn.pack(side="left", padx="5px")
        btn2= Button(frame, text="Não", font="Arial 14", bg="red", fg="white", relief="flat",command= partial(self.responseaskmessagebox, False, i))
        btn2.pack(side="left", padx="5px")
        i.mainloop()
    def responseaskmessagebox(self, text, display):
        self.responseAsk= text
        display.destroy()
    def profile(self):
        ciclo= True
        while ciclo:
            self.messagebox("Foto de Face Tecido Mole","Faça o ajuste para fazer a captura da Face de Tecido Mole do paciente")
            self.quad()
            pyautogui.screenshot(os.getcwd() + "/Resources/Images/temp/profile.png", region=(self.PhotosInit[0],self.PhotosInit[1], int(39* DISPLAY[0]/100),int(39* DISPLAY[0]/100)))
            self.messagebox("Compass X - Captura efetuada!","Sua captura foi realizada com sucesso!")
            self.askmessagebox("CompassX - Captura está correta?","Deseja realizar outra captura?")
            if(not(self.responseAsk)):
                break
    def FT(self):
        ciclo= True
        while ciclo:
            self.messagebox("Foto da Fig 1 Alterada","Faça o ajuste para fazer a captura da foto da Fig 1 Alterada do paciente")
            self.quad()
            pyautogui.screenshot(os.getcwd() + "/Resources/Images/temp/FT.png", region=(self.PhotosInit[0],self.PhotosInit[1], int(39* DISPLAY[0]/100),int(39* DISPLAY[0]/100)))
            self.messagebox("Compass X - Captura efetuada!","Sua captura foi realizada com sucesso!")
            self.askmessagebox("CompassX - Captura está correta?","Deseja realizar outra captura?")
            if(not(self.responseAsk)):
                break
    def PG(self):
        ciclo= True
        while ciclo:
            self.messagebox("_PC3D22 Fig 2 Posição Gônios","Faça o ajuste para fazer a captura da foto da _PC3D22 Fig 2 Posição Gônios")
            self.quad()
            pyautogui.screenshot(os.getcwd() + "/Resources/Images/temp/PG.png", region=(self.PhotosInit[0],self.PhotosInit[1], int(39* DISPLAY[0]/100),int(39* DISPLAY[0]/100)))
            self.messagebox("Compass X - Captura efetuada!","Sua captura foi realizada com sucesso!")
            self.askmessagebox("CompassX - Captura está correta?","Deseja realizar outra captura?")
            if(not(self.responseAsk)):
                break
    def DH(self):
        ciclo= True
        while ciclo:
            self.messagebox("Dimensões das Hemi-Mandíbulas - _PC3D22 Fig 3 HEMI-MAND","Faça o ajuste para fazer a captura da foto _PC3D22 Fig 3 HEMI-MAND")
            self.quad()
            pyautogui.screenshot(os.getcwd() + "/Resources/Images/temp/DH.png", region=(self.PhotosInit[0],self.PhotosInit[1], int(39* DISPLAY[0]/100),int(39* DISPLAY[0]/100)))
            self.messagebox("Compass X - Captura efetuada!","Sua captura foi realizada com sucesso!")
            self.askmessagebox("CompassX - Captura está correta?","Deseja realizar outra captura?")
            if(not(self.responseAsk)):
                break
    def DPC(self):
        ciclo= True
        while ciclo:
            self.messagebox("_PC3D22 Fig 10 Mand e P Coronal","Faça o ajuste para fazer a captura da foto da _PC3D22 Fig 10 Mand e P Coronal")
            self.quad()
            pyautogui.screenshot(os.getcwd() + "/Resources/Images/temp/DPC.png", region=(self.PhotosInit[0],self.PhotosInit[1], int(39* DISPLAY[0]/100),int(39* DISPLAY[0]/100)))
            self.messagebox("Compass X - Captura efetuada!","Sua captura foi realizada com sucesso!")
            self.askmessagebox("CompassX - Captura está correta?","Deseja realizar outra captura?")
            if(not(self.responseAsk)):
                break
    def AF(self):
        ciclo= True
        while ciclo:
            self.messagebox("Foto da Altura Facial e Forma da Mandibula - _PC3D22 Fig 4 AFAI AFAS","Faça o ajuste para fazer a captura da foto _PC3D22 Fig 4 AFAI AFAS")
            self.quad()
            pyautogui.screenshot(os.getcwd() + "/Resources/Images/temp/AF.png", region=(self.PhotosInit[0],self.PhotosInit[1], int(39* DISPLAY[0]/100),int(39* DISPLAY[0]/100)))
            self.messagebox("Compass X - Captura efetuada!","Sua captura foi realizada com sucesso!")
            self.askmessagebox("CompassX - Captura está correta?","Deseja realizar outra captura?")
            if(not(self.responseAsk)):
                break
    def FM(self):
        ciclo= True
        while ciclo:
            self.messagebox("Forma da Mandíbula - _PC3D22 Fig 5 FORMA MAND","Faça o ajuste para fazer a captura da foto _PC3D22 Fig 5 FORMA MAND")
            self.quad()
            pyautogui.screenshot(os.getcwd() + "/Resources/Images/temp/FM.png", region=(self.PhotosInit[0],self.PhotosInit[1], int(39* DISPLAY[0]/100),int(39* DISPLAY[0]/100)))
            self.messagebox("Compass X - Captura efetuada!","Sua captura foi realizada com sucesso!")
            self.askmessagebox("CompassX - Captura está correta?","Deseja realizar outra captura?")
            if(not(self.responseAsk)):
                break
    def POEF(self):
        ciclo= True
        while ciclo:
            self.messagebox("POEF - _PC3D22 Fig 6 POEF","Faça o ajuste para fazer a captura da foto _PC3D22 Fig 6 POEF")
            self.quad()
            pyautogui.screenshot(os.getcwd() + "/Resources/Images/temp/POEF.png", region=(self.PhotosInit[0],self.PhotosInit[1], int(39* DISPLAY[0]/100),int(39* DISPLAY[0]/100)))
            self.messagebox("Compass X - Captura efetuada!","Sua captura foi realizada com sucesso!")
            self.askmessagebox("CompassX - Captura está correta?","Deseja realizar outra captura?")
            if(not(self.responseAsk)):
                break
    def INC(self):
        ciclo= True
        while ciclo:
            self.messagebox("Incisivos","Cortes Ortorradiais Panorâmica. Linha Azul cheia, \n ponto de contato 11 e 21 – tela cheia apenas \n com os 9 cortes. Ajuste para foto.")
            self.quadFull()
            coords= (self.PhotosInitFull[0],self.PhotosInitFull[1], self.PhotosFinalFull[0] - self.PhotosInitFull[0],self.PhotosFinalFull[1] - self.PhotosInitFull[1])
            pyautogui.screenshot(os.getcwd() + "/Resources/Images/temp/INC.png", region= coords)
            self.messagebox("Compass X - Captura efetuada!","Sua captura foi realizada com sucesso!")
            self.askmessagebox("CompassX - Captura está correta?","Deseja realizar outra captura?")
            if(not(self.responseAsk)):
                break
    def TM(self):
        ciclo= True
        while ciclo:
            self.messagebox("Triangulo Mandibular - _PC3D22 Fig 9 Triângulo Mand","Faça o ajuste para fazer a captura da foto _PC3D22 Fig 9 Triângulo Mand")
            self.quad()
            coords= (self.PhotosInit[0],self.PhotosInit[1], int(39* DISPLAY[0]/100),int(39* DISPLAY[0]/100))
            pyautogui.screenshot(os.getcwd() + "/Resources/Images/temp/TM.png", region= coords)
            self.messagebox("Compass X - Captura efetuada!","Sua captura foi realizada com sucesso!")
            self.askmessagebox("CompassX - Captura está correta?","Deseja realizar outra captura?")
            if(not(self.responseAsk)):
                break
    def PSGCF(self):
        #self.messagebox("Posições Sagitais - Gônios, Capitulares e F. Mentonianos","Faça o ajuste para fazer a captura da foto das posições sagitais")
        #self.quadFull()
        #coords= (self.PhotosInit[0],self.PhotosInit[1], int(39* DISPLAY[0]/100),int(39* DISPLAY[0]/100))
        #pyautogui.screenshot(os.getcwd() + "/Resources/Images/temp/PSGCF.png", region= coords)
        pass
    def RIGHTMETR(self):
        ciclo= True
        while ciclo:
            self.messagebox("Reconstrução da Superficie - Fotos Planos 1","Faça o ajuste para fazer a captura da foto direita com medidas. (Fotos Planos 1)")
            self.quadFull()
            coords= (self.PhotosInitFull[0],self.PhotosInitFull[1], self.PhotosFinalFull[0] - self.PhotosInitFull[0],self.PhotosFinalFull[1] - self.PhotosInitFull[1])
            pyautogui.screenshot(os.getcwd() + "/Resources/Images/temp/RIGHTMETR.png", region= coords)
            self.messagebox("Compass X - Captura efetuada!","Sua captura foi realizada com sucesso!")
            self.askmessagebox("CompassX - Captura está correta?","Deseja realizar outra captura?")
            if(not(self.responseAsk)):
                break
    def LEFTMETR(self):
        ciclo= True
        while ciclo:
            self.messagebox("Reconstrução da Superficie - Fotos Planos 1","Faça o ajuste para fazer a captura da foto esquerda com medidas - Fotos Planos 1")
            self.quadFull()
            coords= (self.PhotosInitFull[0],self.PhotosInitFull[1], self.PhotosFinalFull[0] - self.PhotosInitFull[0],self.PhotosFinalFull[1] - self.PhotosInitFull[1])
            pyautogui.screenshot(os.getcwd() + "/Resources/Images/temp/LEFTMETR.png", region= coords)
            self.messagebox("Compass X - Captura efetuada!","Sua captura foi realizada com sucesso!")
            self.askmessagebox("CompassX - Captura está correta?","Deseja realizar outra captura?")
            if(not(self.responseAsk)):
                break
    def RIGHTRAD(self):
        ciclo= True
        while ciclo:
            self.messagebox("Reconstrução da Superficie - Hemitelerradiografia Direita","Faça o ajuste para fazer a captura da foto Hemitelerradiografia Direita")
            self.quadFull()
            coords= (self.PhotosInitFull[0],self.PhotosInitFull[1], self.PhotosFinalFull[0] - self.PhotosInitFull[0],self.PhotosFinalFull[1] - self.PhotosInitFull[1])
            pyautogui.screenshot(os.getcwd() + "/Resources/Images/temp/RIGHTRAD.png", region= coords)
            self.messagebox("Compass X - Captura efetuada!","Sua captura foi realizada com sucesso!")
            self.askmessagebox("CompassX - Captura está correta?","Deseja realizar outra captura?")
            if(not(self.responseAsk)):
                break
    def LEFTRAD(self):
        ciclo= True
        while ciclo:
            self.messagebox("Reconstrução da Superficie - Hemitelerradiografia Esquerda","Faça o ajuste para fazer a captura da foto Hemitelerradiografia Esquerda")
            self.quadFull()
            coords= (self.PhotosInitFull[0],self.PhotosInitFull[1], self.PhotosFinalFull[0] - self.PhotosInitFull[0],self.PhotosFinalFull[1] - self.PhotosInitFull[1])
            pyautogui.screenshot(os.getcwd() + "/Resources/Images/temp/LEFTRAD.png", region= coords)
            self.messagebox("Compass X - Captura efetuada!","Sua captura foi realizada com sucesso!")
            self.askmessagebox("CompassX - Captura está correta?","Deseja realizar outra captura?")
            if(not(self.responseAsk)):
                break
    def PANRAD(self):
        ciclo= True
        while ciclo:
            self.messagebox("Reconstrução da Superficie","Faça o ajuste para fazer a captura da foto tomografia panoramica")
            self.quadFull()
            coords= (self.PhotosInitFull[0],self.PhotosInitFull[1], self.PhotosFinalFull[0] - self.PhotosInitFull[0],self.PhotosFinalFull[1] - self.PhotosInitFull[1])
            pyautogui.screenshot(os.getcwd() + "/Resources/Images/temp/PANRAD.png", region= coords)
            self.messagebox("Compass X - Captura efetuada!","Sua captura foi realizada com sucesso!")
            self.askmessagebox("CompassX - Captura está correta?","Deseja realizar outra captura?")
            if(not(self.responseAsk)):
                break
    def SOBREPOSICAO(self):
        self.quadFull()
        coords= (self.PhotosInitFull[0],self.PhotosInitFull[1], self.PhotosFinalFull[0],self.PhotosFinalFull[1])
        pyautogui.screenshot(os.getcwd() + "/Resources/Images/temp/SOBREPOSICAO.png", region= coords)
    def ATMLEFT(self):
        ciclo= True
        while ciclo:
            self.messagebox("ATM Esquerda","Faça o ajuste para fazer a captura da foto \n da ATM Esquerda. Espaços Articulares \n Panorâmica das ATM - ATM Esquerda – Linha Azul Cheia no centro da Cabeça da Mandíbula Esquerda – aparece \n somente os 9 cortes ortorradiais.")
            self.quadFull()
            coords= (self.PhotosInitFull[0],self.PhotosInitFull[1], self.PhotosFinalFull[0] - self.PhotosInitFull[0],self.PhotosFinalFull[1] - self.PhotosInitFull[1])
            pyautogui.screenshot(os.getcwd() + "/Resources/Images/temp/ATMLEFT.png", region= coords)
            self.messagebox("Compass X - Captura efetuada!","Sua captura foi realizada com sucesso!")
            self.askmessagebox("CompassX - Captura está correta?","Deseja realizar outra captura?")
            if(not(self.responseAsk)):
                break
    def ATMRIGHT(self):
        ciclo= True
        while ciclo:
            self.messagebox("ATM Direito","Faça o ajuste para fazer a captura da foto \n da ATM Direito. Espaços Articulares \n Panorâmica das ATM - ATM DIreita – Linha Azul Cheia no centro da Cabeça da Mandíbula Direita – aparece \n somente os 9 cortes ortorradiais")
            self.quadFull()
            coords= (self.PhotosInitFull[0],self.PhotosInitFull[1], self.PhotosFinalFull[0] - self.PhotosInitFull[0],self.PhotosFinalFull[1] - self.PhotosInitFull[1])
            pyautogui.screenshot(os.getcwd() + "/Resources/Images/temp/ATMRIGHT.png", region= coords)
            self.messagebox("Compass X - Captura efetuada!","Sua captura foi realizada com sucesso!")
            self.askmessagebox("CompassX - Captura está correta?","Deseja realizar outra captura?")
            if(not(self.responseAsk)):
                break
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