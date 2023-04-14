import os

class backgrounds(object):
    def setCover(self):
        self.document.scale(1,-1)
        self.document.drawImage(os.getcwd() + "/Resources/Images/Capa.png", 0,0, width= self.PAGESIZE[0],height= -self.PAGESIZE[1],mask=None)
    def setBody(self):
        self.document.scale(1,-1)
        self.document.drawImage(os.getcwd() + "/Resources/Images/Fundo.png", 0,0, width= self.PAGESIZE[0],height= -self.PAGESIZE[1],mask=None)
        self.document.scale(1,-1)
    def setEnd(self):
        self.document.drawImage(os.getcwd() + "/Resources/Images/Final.png", 0,0, width= self.PAGESIZE[0],height= self.PAGESIZE[1],mask=None)   