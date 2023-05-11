import os
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

class structure(object):
    def registerFont(self):
        pdfmetrics.registerFont(TTFont('Berlin', os.getcwd() + '/Resources/Fonts/berlin.ttf'))
    def drawText(self, x: int, y: int, text: str, size: int, color: list= [1,1,1]):
        self.document.setFont("Berlin", size)
        self.document.setFillColorRGB(color[0],color[1],color[2])
        self.document.drawString(x,y,text)
    def drawImage(self, path: str, x: int, y: int, mask="auto", invert= False, **kwargs):
        if(invert):
            self.document.scale(-1,-1)
        else:
            self.document.scale(1,-1)
        self.document.drawImage(path,x,-y,mask=mask, **kwargs)