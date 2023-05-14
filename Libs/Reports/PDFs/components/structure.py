import os
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from PIL import Image

class structure(object):
    def registerFont(self):
        pdfmetrics.registerFont(TTFont('Berlin', os.getcwd() + '/Resources/Fonts/berlin.ttf'))
    def drawText(self, x: int, y: int, text: str, size: int, color: list= [1,1,1]):
        self.document.setFont("Berlin", size)
        self.document.setFillColorRGB(color[0],color[1],color[2])
        self.document.drawString(x,y,text)
    def drawImage(self, path: str, x: int, y: int, mask="auto", invert= False, **kwargs):
        self.document.scale(1,-1)
        if(invert):
            self.document.scale(-1,-1)
        self.document.drawImage(path,x,-y,mask=mask, **kwargs)
    def resizeImage(self, img, newimg, scale= 2):
        img = Image.open(os.getcwd() + f"/Resources/Images/temp/{img}.png")
        width = int(img.width * scale)
        height = int(img.height * scale)
        img_resized = img.resize((width, height))
        img_resized.save(os.getcwd() + f"/Resources/Images/temp/{newimg}.png")
        
    def resizeImageManual(self, img, newimg, scale= 2):
        img = Image.open(os.getcwd() + f"/Resources/Images/temp/{img}.png")
        width = int(img.width * scale)
        height = int(img.height * scale)
        img_resized = img.resize((width, height))
        img_resized.save(os.getcwd() + f"/Resources/Images/temp/{newimg}.png")