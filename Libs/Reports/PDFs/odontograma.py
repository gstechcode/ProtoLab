from reportlab.pdfgen import canvas
from Libs.Reports.PDFs.components import backgrounds, structure
from datetime import datetime
import os, json


class PDFOdontograma(backgrounds.backgrounds, structure.structure):
    def __init__(self):
        self.registerFont()
        self.titleSize= 60
        self.textSize= 30
        self.ORANGE= (255/255,102/255,0/255)
        self.PAGESIZE= (1920,1080)
        banco= open(os.getcwd() + "/Resources/Databases/PCTable.tbl", "r")
        self.db= json.loads(banco.readlines()[0])
        banco.close()
        dt= datetime.now()
        ano, mes, dia, hora, minutos, segundos= dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second
        complementoid= f"{ano}{mes}{dia}{hora}{minutos}{segundos}"
        self.document= canvas.Canvas(os.environ["USERPROFILE"] + "/Documents/CompassX/" + self.db["NOME"] + "/Odontogramas" + "/" + self.db["NOME"].replace(" ","_")+ complementoid + ".pdf",self.PAGESIZE, bottomup=0)
        self.setCover()
        self.PageOdontograma()
        self.document.save()
        
    def PageOdontograma(self):
        
        self.setOdontogramaFundo()
        
        self.drawText(810, 100, "Infográfico", 40, self.ORANGE)
        
        self.drawText(1595, 810, "Infográfico criado pela", self.textSize)
        
        self.drawText(1480, 850, "Dra. Mara Rufato Cardoso(2017)", self.textSize)
        
        self.drawImage(os.getcwd() + "/Resources/Images/temp/odontograma.png",230,1000, width= 1326,height= 949, mask="auto")
        
        self.document.showPage()
        
    def setCover(self):
        self.setOdontogramaCover()
        self.document.showPage()