import win32api
import win32gui
import pyautogui
from Libs.variables import *
from PIL import Image
import os

#Pega o contexto gráfico para o Desktop
dc = win32gui.GetDC(0)


class photos(object):
    def runPhotos(self):
        '''self.profile()
        self.FT()
        self.PG()
        self.DH()
        self.AF()
        self.FM()
        self.POEF()
        self.INC()
        self.TM()
        self.PSGCF()
        self.SOBREPOSICAO()'''
        pass
    def profile(self):
        self.quad()
        pyautogui.screenshot(os.getcwd() + "/Resources/Images/temp/profile.png", region=(self.PhotosInit[0],self.PhotosInit[1], int(39* DISPLAY[0]/100),int(39* DISPLAY[0]/100)))
    def FT(self):
        self.quad()
        pyautogui.screenshot(os.getcwd() + "/Resources/Images/temp/FT.png", region=(self.PhotosInit[0],self.PhotosInit[1], int(39* DISPLAY[0]/100),int(39* DISPLAY[0]/100)))
    def PG(self):
        self.quad()
        pyautogui.screenshot(os.getcwd() + "/Resources/Images/temp/PG.png", region=(self.PhotosInit[0],self.PhotosInit[1], int(39* DISPLAY[0]/100),int(39* DISPLAY[0]/100)))
    def DH(self):
        self.quad()
        pyautogui.screenshot(os.getcwd() + "/Resources/Images/temp/DH.png", region=(self.PhotosInit[0],self.PhotosInit[1], int(39* DISPLAY[0]/100),int(39* DISPLAY[0]/100)))
    def AF(self):
        self.quad()
        pyautogui.screenshot(os.getcwd() + "/Resources/Images/temp/AF.png", region=(self.PhotosInit[0],self.PhotosInit[1], int(39* DISPLAY[0]/100),int(39* DISPLAY[0]/100)))
    def FM(self):
        self.quad()
        pyautogui.screenshot(os.getcwd() + "/Resources/Images/temp/FM.png", region=(self.PhotosInit[0],self.PhotosInit[1], int(39* DISPLAY[0]/100),int(39* DISPLAY[0]/100)))
    def POEF(self):
        self.quad()
        pyautogui.screenshot(os.getcwd() + "/Resources/Images/temp/POEF.png", region=(self.PhotosInit[0],self.PhotosInit[1], int(39* DISPLAY[0]/100),int(39* DISPLAY[0]/100)))
    def INC(self):
        self.quad()
        pyautogui.screenshot(os.getcwd() + "/Resources/Images/temp/INC.png", region=(self.PhotosInit[0],self.PhotosInit[1], int(39* DISPLAY[0]/100),int(39* DISPLAY[0]/100)))
    def TM(self):
        self.quad()
        pyautogui.screenshot(os.getcwd() + "/Resources/Images/temp/TM.png", region=(self.PhotosInit[0],self.PhotosInit[1], int(39* DISPLAY[0]/100),int(39* DISPLAY[0]/100)))
    def PSGCF(self):
        self.quad()
        pyautogui.screenshot(os.getcwd() + "/Resources/Images/temp/PSGCF.png", region=(self.PhotosInit[0],self.PhotosInit[1], int(39* DISPLAY[0]/100),int(39* DISPLAY[0]/100)))
    def SOBREPOSICAO(self):
        self.quad()
        pyautogui.screenshot(os.getcwd() + "/Resources/Images/temp/SOBREPOSICAO.png", region=(self.PhotosInit[0],self.PhotosInit[1], int(39* DISPLAY[0]/100),int(39* DISPLAY[0]/100)))
    def quad(self):
        InitPosition= (342,240)
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
                
            if(cont > 100):
                break
    def optimizeImages(self):
        self.convertImage(os.getcwd() + "/Resources/Images/temp/FT.png")
        self.convertImage(os.getcwd() + "/Resources/Images/temp/PG.png")
        self.convertImage(os.getcwd() + "/Resources/Images/temp/DH.png")
        self.convertImage(os.getcwd() + "/Resources/Images/temp/AF.png")
        self.convertImage(os.getcwd() + "/Resources/Images/temp/FM.png")
        self.convertImage(os.getcwd() + "/Resources/Images/temp/POEF.png")
        self.convertImage(os.getcwd() + "/Resources/Images/temp/INC.png", tam= (2016,1136))
        self.convertImage(os.getcwd() + "/Resources/Images/temp/TM.png", tam= (1542,868))
        self.convertImage(os.getcwd() + "/Resources/Images/temp/PSGCF.png", tam= (1542,868))
        try:
            self.convertImage(os.getcwd() + "/Resources/Images/temp/SOBREPOSICAO.png", tam= (int(2652/2.2),int(2315/2.2)))
        except Exception:
            pass

    def convertImage(self, path, tam= (700,700)):
        imgresize= Image.open(path)
        imgresized= imgresize.resize(tam, Image.ANTIALIAS)
        imgresized.save(path)
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