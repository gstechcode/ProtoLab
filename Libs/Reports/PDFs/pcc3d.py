from reportlab.pdfgen import canvas
from Libs.variables import *
from Libs.Reports.PDFs.components import backgrounds, structure, photos
import os, json
from PIL import Image
from Resources.Tools import GenOdontograma
from datetime import datetime
from Libs.Reports.PDFs.odontograma import PDFOdontograma

class pcc3d(
    backgrounds.backgrounds,
    structure.structure,
    photos.photos):
    def __init__(self):
        super().__init__()
        self.__vars__()
        self.Cover()
        self.Page1()
        self.Page2()
        self.Page12()
        self.Page3()
        self.Page4()
        self.Page5()
        self.Page6()
        self.Page7()
        self.Page8()
        self.Page9()
        self.INCView()
        self.Page10()
        self.Page11()
        self.Page13()
        self.Page13View()
        self.Page14()
        self.Page14View()
        self.Page15()
        self.Page16()
        self.Page17()
        self.Page18()
        self.Page19()
        self.Page20()
        if(self.db["denticao"] == "Decídua"):
            self.Page21()
        self.Page22()
        self.setBackgroundEnd()
        
        odonto= PDFOdontograma()
        
        self.document.save()
    def Cover(self):
        self.setCover()
        self.document.showPage()
    def Page1(self):
        self.setBody()
        self.drawText(60,100, "Dados do paciente:", self.titleSize, self.ORANGE)
        self.drawText(60,260, "Nome: ", self.textSize, self.ORANGE)
        self.drawText(200,260, self.db["NOME"], self.textSize)
        self.drawText(60,320, "Idade: ", self.textSize, self.ORANGE)
        self.drawText(200,320, str(self.db["IDADE"]), self.textSize)
        self.drawText(60,380, "Genero: ", self.textSize, self.ORANGE)
        self.drawText(220,380, self.db["Genero"], self.textSize)
        self.drawText(670, 900, "Grupo Rotacional: {GrupoR} - Categoria Auxológica: {Cat}".format(GrupoR= self.db["GrupoR"], Cat= self.db["CatAux"]), 50)
        self.drawImage(os.getcwd() + "/Resources/Images/temp/profile.png", 900,820, width=800, height= 800)
        self.document.showPage()
        
        self.View("Foto de Tecido Mole do Paciente - Visualização","profile", scale= 1.3)
        
    def Page2(self):
        self.textSize= 32
        self.setBody()
        spacing= 60
        desvio= 0
        x1, y1, x2, y2= 40,530,1350,530
        justify= 95
        
        self.drawImage(os.getcwd() + "/Resources/Images/temp/FT.png",620,900, mask= "auto")
        
        self.document.scale(1,-1)
        
        #13 Height Camper
        if(self.denticaoSlot):
            self.drawText(x1,y1, f"Altura 53 X Plano de Camper " + self.db["HC1323"]["13 Height Camper"],self.textSize)
        else:
            self.drawText(x1,y1, "Altura 13 X Plano de Camper " + self.db["HC1323"]["13 Height Camper"],self.textSize)
		
		#23 Height Camper
        if(self.denticaoSlot):
            self.drawText(x2,y2, "Altura 63 X Plano de Camper " + self.db["HC1323"]["23 Height Camper"],self.textSize)
        else:
            self.drawText(x2,y2, "Altura 23 X Plano de Camper " + self.db["HC1323"]["23 Height Camper"],self.textSize)

        #14 Height Camper
        if(self.denticaoSlot):
            self.drawText(x1 + desvio,y1 + spacing, "Altura 54 X Plano de Camper " + self.db["HC1424"]["14 Height Camper"],self.textSize)
        else:
            self.drawText(x1 + desvio,y1 + spacing, "Altura 14 X Plano de Camper " + self.db["HC1424"]["14 Height Camper"],self.textSize)	

		#24 Height Camper
        if(self.denticaoSlot):
            self.drawText(x2 - desvio,y2 + spacing, "Altura 64 X Plano de Camper " + self.db["HC1424"]["24 Height Camper"],self.textSize)
        else:
            self.drawText(x2 - desvio,y2 + spacing, "Altura 24 X Plano de Camper " + self.db["HC1424"]["24 Height Camper"],self.textSize)

		#16 Height Camper
        if(self.denticaoSlot):
            self.drawText(x1 + desvio*2,y1 + spacing*2, "Altura 55 X Plano de Camper " + self.db["HC1626"]["16 Height Camper"],self.textSize)
        else:
            self.drawText(x1 + desvio*2,y1 + spacing*2, "Altura 16 X Plano de Camper " + self.db["HC1626"]["16 Height Camper"],self.textSize)	

		#26 Height Camper
        if(self.denticaoSlot):
            self.drawText(x2 - desvio*2,y2 + spacing*2, "Altura 65 X Plano de Camper " + self.db["HC1626"]["26 Height Camper"],self.textSize)
        else:
            self.drawText(x2 - desvio*2,y2 + spacing*2, "Altura 26 X Plano de Camper " + self.db["HC1626"]["26 Height Camper"],self.textSize)	
	
		#13 XMSP
        if(self.denticaoSlot):
            self.drawText(x1 + desvio*3,y1 + spacing*3, "Distância 53 X P.S.M. " + self.db["MSP1323"]["13 X MSP"],self.textSize)
        else:
            self.drawText(x1 + desvio*3,y1 + spacing*3, "Distância 13 X P.S.M. " + self.db["MSP1323"]["13 X MSP"],self.textSize)
		#23 XMSP
        if(self.denticaoSlot):
            self.drawText(x2 - desvio*3 + justify,y2 + spacing*3, "Distância 63 X P.S.M. " + self.db["MSP1323"]["23 X MSP"],self.textSize)
        else:
            self.drawText(x2 - desvio*3 + justify,y2 + spacing*3, "Distância 23 X P.S.M. " + self.db["MSP1323"]["23 X MSP"],self.textSize)

		#14 XMSP
        if(self.denticaoSlot):
            self.drawText(x1 + desvio*4,y1 + spacing*4, "Distância 54 X P.S.M. " + self.db["MSP1424"]["14 X MSP"],self.textSize)
        else:
            self.drawText(x1 + desvio*4,y1 + spacing*4, "Distância 14 X P.S.M. " + self.db["MSP1424"]["14 X MSP"],self.textSize)	
		
		#24 XMSP
        if(self.denticaoSlot):
            self.drawText(x2 - desvio*4 + justify,y2 + spacing*4, "Distância 64 X P.S.M. " + self.db["MSP1424"]["24 X MSP"],self.textSize)
        else:
            self.drawText(x2 - desvio*4 + justify,y2 + spacing*4, "Distância 24 X P.S.M. " + self.db["MSP1424"]["24 X MSP"],self.textSize)

		#16 XMSP
        if(self.denticaoSlot):
            self.drawText(x1 + desvio*5,y1 + spacing*5, "Distância 55 X P.S.M. " + self.db["MSP1626"]["16 X MSP"],self.textSize)
        else:
            self.drawText(x1 + desvio*5,y1 + spacing*5, "Distância 16 X P.S.M. " + self.db["MSP1626"]["16 X MSP"],self.textSize)

		#26 XMSP
        if(self.denticaoSlot):
            self.drawText(x2 - desvio*5 + justify,y2 + spacing*5, "Distância 65 X P.S.M. " + self.db["MSP1626"]["26 X MSP"],self.textSize)
        else:
            self.drawText(x2 - desvio*5 + justify,y2 + spacing*5, "Distância 26 X P.S.M. " + self.db["MSP1626"]["26 X MSP"],self.textSize)

        self.document.drawCentredString(self.PAGESIZE[0]/2,y1 + spacing*7,self.db["response"]["HC"])
        self.document.drawCentredString(self.PAGESIZE[0]/2,y1 + spacing*8,self.db["response"]["XMSP131416"])
        self.document.setStrokeColorRGB(255/255, 102/255, 0/255)
        self.document.rect(40,50,750,140, fill=0, stroke= 1)
        self.drawText(80,110,"Distância em Milímetros dos dentes aos", 40)
        self.drawText(80,160,"Planos de Camper e P. Sagital Mediano", 40)
        self.document.showPage()
        
        self.View("Distância Planos de Camper e P. Sagital Mediano - Visualização","FT", scale= 1.3)

    def Page3(self):
        self.setBody()
        self.drawText(60,120,"Posição dos Gônios",self.titleSize, self.ORANGE)
        self.drawText(20,550,"Gônio Direito",self.textSize + 5)
        
        self.drawImage(os.getcwd() + "/Resources/Images/temp/PG.png",590,850, mask= "auto")
        
        self.document.scale(1,-1)
        
        self.drawText(20,625,"Dist. do Gônio Dir. ao P. Coronal " + self.db["GOLRCP"]["GoL Coronal Plane"],self.textSize)
        self.drawText(20,675,"Dist. do Gônio Dir. ao P. Camper " + self.db["GoLRCamper"]["GoL Camper"],self.textSize)
        self.drawText(20,725,"Gônio Direito X P.S.M " + self.db["GOLRMSP"]["GoL MSP"],self.textSize)
        
        self.drawText(1640,550,"Gônio Esquerdo",self.textSize + 5)
        self.drawText(1310,625,"Dist. do Gônio Esq. ao P. Coronal " + self.db["GOLRCP"]["GoR Coronal Plane"],self.textSize)
        self.drawText(1315,675,"Dist. do Gônio Esq. ao P. Camper " + self.db["GoLRCamper"]["GoR Camper"],self.textSize)
        self.drawText(1425,725,"Gônio Esquerdo X P.S.M " + self.db["GOLRMSP"]["GoR MSP"],self.textSize)
        
        self.document.drawCentredString(self.PAGESIZE[0]/2,910,self.db["response"]["GOLRCP"])
        self.document.drawCentredString(self.PAGESIZE[0]/2,960,self.db["response"]["GOLRCAMPER"])
        self.document.drawCentredString(self.PAGESIZE[0]/2,1010,self.db["response"]["GOLRMSP"])
        self.document.showPage()
        
        self.View("Posição dos Gônios - Visualização","PG", scale= 1.3)
        
    def View(self, title, img, scale= 1.8):
        self.setBody()
        self.drawText(60,60,title,int(self.titleSize/2), self.ORANGE)
        
        self.resizeImage(img, img + "view", scale)
        
        self.drawImage(os.getcwd() + f"/Resources/Images/temp/{img}view.png",510,990, mask= "auto")
        
        self.document.showPage()
    def Page4(self):
        self.textSize= 30

        self.setBody()
        self.drawText(60,120,"Dimensões das", self.titleSize, self.ORANGE)
        self.drawText(60,190,"Hemimandíbulas", self.titleSize, self.ORANGE)
        
        self.drawImage(os.getcwd() + "/Resources/Images/temp/DH.png",590,850, mask= "auto")
        
        self.document.scale(1,-1)

        self.drawText(40,645,"Diagonal Mandibular Direita " + self.db["CondLRGN"]["CondR - Gn"], self.textSize)
        self.drawText(40,695,"Compr. do Ramo Mand. Dir. " + self.db["CONDLRGOLR"]["CondR GoR"], self.textSize)
        self.drawText(40,745,"Compr. do Corpo Mand. Dir. " + self.db["CORPUSLR"]["Corpus R"], self.textSize)
        
        self.drawText(1340,645,"Diagonal Mandibular Esquerda " + self.db["CondLRGN"]["CondL - Gn"], self.textSize)
        self.drawText(1370,695,"Compr. do Ramo Mand. Esq. " + self.db["CONDLRGOLR"]["CondL GoL"], self.textSize)
        self.drawText(1370,745,"Compr. do Corpo Mand. Esq. " + self.db["CORPUSLR"]["Corpus L"], self.textSize)

        self.document.drawCentredString(self.PAGESIZE[0]/2,910,self.db["response"]["CONDLRGN"])
        self.document.drawCentredString(self.PAGESIZE[0]/2,960,self.db["response"]["CONDLRGOLR"])
        self.document.drawCentredString(self.PAGESIZE[0]/2,1010,self.db["response"]["GOLRGN"])
        
        self.document.showPage()
        
        self.View("Dimensões das Hemimandíbulas - Visualização", "DH", scale= 1.3)
        
        
    def Page5(self):

        self.setBody()

        self.drawText(60,120,"Altura Facial",self.titleSize, self.ORANGE)
        
        self.drawImage(os.getcwd() + "/Resources/Images/temp/AF.png",610,850, mask= "auto")
        
        self.document.scale(1,-1)
        
        self.drawText(40,745,"Altura Facial Anterosuperior AFAS " + self.db["AFASI"]["AFAS"],self.textSize)
        self.drawText(1300,745,"Altura Facial Anteroinferior AFAI " + self.db["AFASI"]["AFAI"],self.textSize)
        
        self.document.drawCentredString(self.PAGESIZE[0]/2,960,self.db["response"]["ULH"])
        
        self.document.showPage()
        
        self.View("Altura Facial - Visualização", "AF", scale= 1.3)
        
    def Page6(self):

        self.setBody()

        self.drawText(60,120,"Forma da Mandíbula", self.titleSize, self.ORANGE)

        self.drawText(60,497,"Ângulo Goníaco Direito " + self.db["AGLR"]["AGR"], self.textSize)
        self.drawText(60,745,"Eixo Condilar Direito " + self.db["CARL"]["Condylar Axis Right"], self.textSize)

        self.drawText(1400,497,"Ângulo Goníaco Esquerdo " + self.db["AGLR"]["AGL"], self.textSize)
        self.drawText(1430,745,"Eixo Condilar Esquerdo " + self.db["CARL"]["Condylar Axis Left"], self.textSize)
        
        self.drawImage(os.getcwd() + "/Resources/Images/temp/FM.png",620,880, mask= "auto")
        
        self.document.showPage()
        
        self.View("Forma da Mandíbula - Visualização", "FM", scale= 1.3)
    
    def Page7(self):
        
        self.setBody()
		
        self.drawText(60,120,"POEF", self.titleSize, self.ORANGE)
        self.drawText(60,190,"Plano Oclusal Estético Funcional", 50, self.ORANGE)

        self.drawText(80,700,"POEF 11 " + self.db["POEF"]["POEF 11"], self.textSize)
        self.drawText(80,765,"POEF 21 " + self.db["POEF"]["POEF 21"], self.textSize)
        self.drawText(80,830,"POEF 31 " + self.db["POEF"]["POEF 31"], self.textSize)
        self.drawText(80,895,"POEF 41 " + self.db["POEF"]["POEF 41"], self.textSize)

        self.drawImage(os.getcwd() + "/Resources/Images/temp/POEF.png",820,1000, mask= "auto")
        
        self.document.showPage()
        
        self.View("POEF - Visualização", "POEF", scale= 1.3)
    
    def Page8(self):

        self.setBody()
        
        self.drawText(1920/2 + 250,140,"Incisivos", self.titleSize, self.ORANGE)
        self.drawText(1920/2 + 250,330,"Incisivo Central Esquerdo x Linha Holdaway " + self.db["P, Holdaway"]["31"], self.textSize)
        self.drawText(1920/2 + 280,385,"Incisivo Central Direito x Linha Holdaway " + self.db["P, Holdaway"]["41"], self.textSize)
        self.drawText(1920/2 + 440,440,"Pogônio x Linha Holdaway " + self.db["Pog P, Holdaway"]["Pog P, Holdaway"], self.textSize)
        self.drawText(1920/2 + 610,495,"IMPA Esquerdo " + self.db["IMPA"]["31"], self.textSize)
        self.drawText(1920/2 + 650,550,"IMPA Direito " + self.db["IMPA"]["41"], self.textSize)
        self.drawText(1920/2 + 335,605,"Ângulo Interincisivos Centrais Direitos " + str("%.2f"%(180 - float(self.db["ANGGONLR"]["ANGGONRIGHT"].replace("°","")))) + "°", self.textSize)
        self.drawText(1920/2 + 305,660,"Ângulo Interincisivos Centrais Esquerdos " + str("%.2f"%float(self.db["ANGGONLR"]["ANGGONLEFT"].replace("°",""))) + "°", self.textSize)

        self.drawImage(os.getcwd() + "/Resources/Images/temp/INC.png",40,800, width= 1135, height= 591, mask= "auto")

        self.document.showPage()
        
    def Page9(self):
        decidua= self.db["denticao"] == "Decídua"
        if(decidua):
            teeth11= "61"
            teeth21= "51"
        else:
            teeth11= "11"
            teeth21= "21"
            
        self.setBody()
  
        self.drawText(self.PAGESIZE[0]/2 + 250,140,"Incisivos", self.titleSize, self.ORANGE)

        self.drawText(self.PAGESIZE[0]/2 + 270,330,f"Ângulo {teeth11} Linha NA " + self.db["NA"]["ANG11"], self.textSize)
		
        self.drawText(self.PAGESIZE[0]/2 + 270,385,f"Ângulo {teeth21} Linha NA " + self.db["NA"]["ANG21"], self.textSize)

        self.drawText(self.PAGESIZE[0]/2 + 270,440,f"Distância {teeth11} Linha NA " + self.db["NA"]["MM11"], self.textSize)

        self.drawText(self.PAGESIZE[0]/2 + 270,495,f"Distância {teeth21} Linha NA " + self.db["NA"]["MM21"], self.textSize)
        
        self.drawText(self.PAGESIZE[0]/2 + 270,550,f"Distância {teeth11} Linha A-Pog " + self.db["APOG1121"]["APOG11MM"], self.textSize)

        self.drawText(self.PAGESIZE[0]/2 + 270,605,f"Distância {teeth21} Linha A-Pog " + self.db["APOG1121"]["APOG21MM"], self.textSize)
		
        self.drawImage(os.getcwd() + "/Resources/Images/temp/INC.png",40,800, width= 1135, height= 591, mask= "auto")
        
        
        #self.drawImage(os.getcwd() + "/Resources/Images/temp/INC.png",0,0, width= 1920, height= -1080, mask= "auto")
        
        self.document.showPage()
        
    def INCView(self):
        
        self.setBody()
        self.drawImage(os.getcwd() + "/Resources/Images/temp/INC.png",0,0, width= 1920, height= -1080, mask= "auto")
        self.document.showPage()
        
    def Page10(self):

        self.setBody()

        self.drawText(80,140,"Triângulo Mandibular", self.titleSize, self.ORANGE)

        self.drawText(self.PAGESIZE[0]/2 + 250,330,f"Gônio Esquerdo X P.S.M " + self.db["GOLRMSP"]["GoL MSP"], self.textSize)

        self.drawText(self.PAGESIZE[0]/2 + 250,385,f"Profundidade do Gônio Esquerdo " + self.db["GOLRCP"]["GoL Coronal Plane"], self.textSize)

        self.drawText(self.PAGESIZE[0]/2 + 250,440,f"Gônio Direito X P.S.M " + self.db["GOLRMSP"]["GoR MSP"], self.textSize)

        self.drawText(self.PAGESIZE[0]/2 + 250,495,f"Profundidade do Gônio Direito " + self.db["GOLRCP"]["GoR Coronal Plane"], self.textSize)

        self.drawText(self.PAGESIZE[0]/2 + 250,550,f"Gnátio X P.S.M " + self.db["GNMSP"]["Gn MSP"], self.textSize)

        self.drawText(self.PAGESIZE[0]/2 + 60,680,self.db["response"]["GNMSP"], self.textSize)

        self.drawText(self.PAGESIZE[0]/2 + 60,725,self.db["response"]["GOLRCP"], self.textSize)

        self.drawText(self.PAGESIZE[0]/2 + 60,770,self.db["response"]["GOLRMSP"], self.textSize)

        self.resizeImageManual("TM", "TMdim", scale= 1.1)
        
        self.drawImage(os.getcwd() + "/Resources/Images/temp/TMdim.png",100,950, mask= "auto")
        
        self.document.showPage()
        
        self.View("Triângulo Mandibular - Visualização", "TM", scale= 1.3)
        
    def Page11(self):
		
        self.setBody()

        self.drawText(80,140,"Posições Sagitais - Gônios, Capitulares e F. Mentonianos", self.titleSize, self.ORANGE)

        self.drawText(self.PAGESIZE[0]/2 + 120,330,f"Profundidade do Gônio Esquerdo " + self.db["GOLRCP"]["GoL Coronal Plane"], self.textSize)

        self.drawText(self.PAGESIZE[0]/2 + 120,385,f"Profundidade do Gônio Direito " + self.db["GOLRCP"]["GoR Coronal Plane"], self.textSize)
		
        self.drawText(self.PAGESIZE[0]/2 + 120,440,f"Forame Mentoniano Direito X P. Coronal " + self.db["MEFLRCP"]["MeFR Coronal Plane"], self.textSize)

        self.drawText(self.PAGESIZE[0]/2 + 120,495,f"Forame Mentoniano Esquerdo X P. Coronal " + self.db["MEFLRCP"]["MeFL Coronal Plane"], self.textSize)
        
        self.drawText(self.PAGESIZE[0]/2 + 120,550,f"Distância Capitulare Direito ao P. Coronal " + self.db["CAPITULARELRPCP"]["Capitulare R P. CP"], self.textSize)

        self.drawText(self.PAGESIZE[0]/2 + 120,605,f"Distância Capitulare Esquerdo ao P. Coronal " + self.db["CAPITULARELRPCP"]["Capitulare L P. CP"], self.textSize)

		#comment
        self.drawText(self.PAGESIZE[0]/2 + 60,720,self.db["response"]["CAPITULARELRMSP"], self.textSize)

        self.drawText(self.PAGESIZE[0]/2 + 60,765,self.db["response"]["MEFLRCP"], self.textSize)

        self.drawText(self.PAGESIZE[0]/2 + 60,810,self.db["response"]["GOLRMSP"], self.textSize)
		
        self.resizeImageManual("PSGCF", "PSGCFdim", scale= 1.1)
        
        self.drawImage(os.getcwd() + "/Resources/Images/temp/PSGCFdim.png",100,950, mask= "auto")
  
        self.document.showPage()
        
        self.View("Posições Sagitais - Gônios, Capitulares e F. Mentonianos - Visualização","PSGCF", scale= 1.3)
        
    def Page12(self):
		
        self.setBody()

        if(self.denticaoSlot == True):
            teeth16= "55"
            teeth26= "65"
            teeth36= "75"
            teeth46= "85"
        else:
            teeth16= "16"
            teeth26= "26"
            teeth36= "36"
            teeth46= "46"

        self.drawText(self.PAGESIZE[0]/2 - 40,140,"Distância Dentes P. Coronal", self.titleSize, self.ORANGE)

        self.drawText(self.PAGESIZE[0]/2 + 40,300,f"Distância {teeth16} X P. Coronal " + self.db["CP1626"]["16 Coronal Plane"], self.textSize)

        self.drawText(self.PAGESIZE[0]/2 + 40,355,f"Distância {teeth26} X P. Coronal " + self.db["CP1626"]["26 Coronal Plane"], self.textSize)

        self.drawText(self.PAGESIZE[0]/2 + 40,515,f"Distância {teeth36} X P. Coronal " + self.db["CP3646"]["36 Coronal Plane"], self.textSize)
        
        self.drawText(self.PAGESIZE[0]/2 + 40,570,f"Distância {teeth46} X P. Coronal " + self.db["CP3646"]["46 Coronal Plane"], self.textSize)
        
        self.drawText(self.PAGESIZE[0]/2,730,self.db["response"]["CP1626"], self.textSize)
        
        self.drawText(self.PAGESIZE[0]/2,785,self.db["response"]["CP3646"], self.textSize)
        
        
        self.drawImage(os.getcwd() + "/Resources/Images/temp/DPC.png",100,950, mask= "auto")
        
        self.document.showPage()
        
        
        self.View("Distância Dentes P. Coronal - Visualização", "DPC", scale= 1.3)

    def Page13(self):
        
        self.setBody()
        
        self.drawText(int(self.PAGESIZE[0]/4 - 200),int(self.PAGESIZE[1]/2),"Espaços Articulares ATM Esquerda", 100,self.ORANGE)
        
        self.drawText(int(self.PAGESIZE[0]/4 - 100),int(self.PAGESIZE[1]/2 + 120),"Avaliar valores no Infográfico", 90)
        
        self.document.showPage()
        
    def Page13View(self):
        
        self.setBody()
        self.drawImage(os.getcwd() + "/Resources/Images/temp/ATMLEFT.png",0,0, width= 1920, height= -1080, mask= "auto")
        self.document.showPage()
        
        
  
    def Page14(self):
        
        self.setBody()
        
        self.drawText(int(self.PAGESIZE[0]/4 - 200),int(self.PAGESIZE[1]/2),"Espaços Articulares ATM Direita", 100,self.ORANGE)
        
        self.drawText(int(self.PAGESIZE[0]/4 - 100),int(self.PAGESIZE[1]/2 + 120),"Avaliar valores no Infográfico", 90)
        
        self.document.showPage()
        
    def Page14View(self):
        
        self.setBody()
        self.drawImage(os.getcwd() + "/Resources/Images/temp/ATMRIGHT.png",0,0, width= 1920, height= -1080, mask= "auto")
        self.document.showPage()
        
    def Page15(self):
        
        self.setBody()
        
        self.drawText(int(self.PAGESIZE[0]/4 - 100),int(self.PAGESIZE[1]/2),"Reconstrução de Superfície", 100,self.ORANGE)
        
        self.document.showPage()
        
    def Page16(self):
        
        self.setBody()
        
        self.drawImage(os.getcwd() + "/Resources/Images/temp/RIGHTMETR.png",0,0, width= 1920, height= -1080, mask= "auto")
         
        self.document.scale(1,-1)
        
        self.drawText(1360,250,"Posição Maxila", self.titleSize, self.ORANGE)
         
        self.drawText(1360,350,f"A-Nperp {self.db['A - Np']['A - Np']}", self.textSize + 5)
        self.drawText(1360,415,f"SNA {self.db['SNA']['SNA']}", self.textSize + 5)
        
        self.drawText(1360,515,"Posição Mandibula", self.titleSize, self.ORANGE) 
        
        self.drawText(1360,615,f"Pog – Nperp {self.db['Pog - Np']['Pog - Np']}", self.textSize + 5)
        self.drawText(1360,680,f"SNB {self.db['SNB']['SNB']}", self.textSize + 5)
        self.drawText(1360,745,f"T-TM Direita {self.db['TTMLR']['T-TM DIR']}", self.textSize + 5)
        
        self.document.showPage()
        
    def Page17(self):
        
        self.setBody()
        self.drawImage(os.getcwd() + "/Resources/Images/temp/LEFTMETR.png",0,0, width= 1920, height= -1080, mask= "auto")
        
        self.document.scale(1,-1)
        
        self.drawText(20,250,"Posição Maxila", self.titleSize, self.ORANGE)
         
        self.drawText(20,350,f"A-Nperp {self.db['A - Np']['A - Np']}", self.textSize + 5)
        self.drawText(20,415,f"SNA {self.db['SNA']['SNA']}", self.textSize + 5)
        
        self.drawText(20,515,"Posição Mandibula", self.titleSize, self.ORANGE) 
        
        self.drawText(20,615,f"Pog – Nperp {self.db['Pog - Np']['Pog - Np']}", self.textSize + 5)
        self.drawText(20,680,f"SNB {self.db['SNB']['SNB']}", self.textSize + 5)
        self.drawText(20,745,f"T-TM Esquerda {self.db['TTMLR']['T-TM ESQ']}", self.textSize + 5)
        
        self.document.showPage()
        
    def Page18(self):
        
        self.setBody()
        self.drawImage(os.getcwd() + "/Resources/Images/temp/PANRAD.png",0,0, width= 1920, height= -1080, mask= "auto")
        
        self.document.scale(1,-1)
        
        self.drawText((self.PAGESIZE[0] / 4) + 100,80,"Reconstrução Panorâmica", self.titleSize, self.ORANGE)
        
        self.document.showPage()
        
    def Page19(self):
        
        self.setBody()
        self.drawImage(os.getcwd() + "/Resources/Images/temp/RIGHTRAD.png",0,0, width= 1920, height= -1080, mask= "auto")
        
        self.document.scale(1,-1)
        
        self.drawText(60,80,"Reconstrução", self.titleSize, self.ORANGE)
        self.drawText(60,150,"Hemitelerradiografia Direita", self.titleSize, self.ORANGE)
        
        self.document.showPage()
        
    def Page20(self):
        
        self.setBody()
        self.drawImage(os.getcwd() + "/Resources/Images/temp/LEFTRAD.png",-1920,0, width= 1920, height= -1080, mask= "auto", invert= True)
        
        self.document.scale(-1,-1)
        
        self.drawText(60,80,"Reconstrução", self.titleSize, self.ORANGE)
        self.drawText(60,150,"Hemitelerradiografia Esquerda", self.titleSize, self.ORANGE)
        
        self.document.showPage()
    
    def Page21(self):
        
        self.setBody()
        
        self.drawImage(os.getcwd() + "/Resources/Images/temp/RIGHTMETR.png",0,0, width= 1920, height= -1080, mask= "auto")
         
        self.document.scale(1,-1)
        
        self.drawText(1360,280,"Cefalometria Tollaro", self.titleSize, self.ORANGE)
         
        self.drawText(1360,380,f"SNA {self.db['SNA']['SNA']}", self.textSize + 5)
        self.drawText(1360,430,f"SNB {self.db['SNB']['SNB']}", self.textSize + 5)
        self.drawText(1360,480,f"Ângulo da Base do Crânio {self.db['CBA']['Cranial Base Angle']}", self.textSize + 5)
        self.drawText(1360,530,f"NSL x ML {self.db['NSL x ML']['NSL x ML']}", self.textSize + 5)
        self.drawText(1360,580,f"NSL x ML {self.db['NSL x NL']['NSL x NL']}", self.textSize + 5)
        
        self.document.showPage()
    
    def Page22(self):
		
        self.setBody()

        GenOdontograma.GenOdontograma(self.db)
        
        self.drawText(810, 100, "Infográfico", 40, self.ORANGE)
        
        self.drawText(1595, 830, "Infográfico criado pela", self.textSize)
        
        self.drawText(1480, 870, "Dra. Mara Rufato Cardoso(2017)", self.textSize)
        
        self.drawImage(os.getcwd() + "/Resources/Images/temp/odontograma.png",230,1000, width= 1326,height= 949, mask="auto")
        
        self.document.showPage()

    def setBackgroundEnd(self):
        self.document.scale(1,-1)
        self.document.drawImage(os.getcwd() + r"\Resources\Images\Final.png",-1,-1,self.PAGESIZE[0],-self.PAGESIZE[1])
        self.document.scale(1,-1)
        self.document.linkURL("https://www.instagram.com/compasscomvoce/?hl=pt",[950,270,530,190])
        self.document.linkURL("https://pt-br.facebook.com/CompassComVoce/",[1400,270,970,180])
        self.document.showPage()
  
    def __vars__(self):
        self.runPhotos()
        self.titleSize= 60
        self.textSize= 45
        banco= open(os.getcwd() + "/Resources/Databases/PCTable.tbl", "r")
        self.db= json.loads(banco.readlines()[0])
        banco.close()
        if(self.db["denticao"] == "Decídua" or self.db["denticao"] == "Mista"):
            self.denticaoSlot= False
        else:
            self.denticaoSlot= True
        self.PAGESIZE= (1920,1080)
        self.registerFont()
        self.ORANGE= (255/255,102/255,0/255)
        self.optimizeImages()
        try:
            os.mkdir(os.environ["USERPROFILE"] + "/Documents/CompassX")
        except FileExistsError:
            pass
        try:
            os.mkdir(os.environ["USERPROFILE"] + "/Documents/CompassX/" + self.db["NOME"])
        except FileExistsError:
            pass
        try:
            os.mkdir(os.environ["USERPROFILE"] + "/Documents/CompassX/" + self.db["NOME"] + "/Protocolos")
        except FileExistsError:
            pass
        try:
            os.mkdir(os.environ["USERPROFILE"] + "/Documents/CompassX/" + self.db["NOME"] + "/Odontogramas")
        except FileExistsError:
            pass
        dt= datetime.now()
        ano, mes, dia, hora, minutos, segundos= dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second
        complementoid= f"{ano}{mes}{dia}{hora}{minutos}{segundos}"
        self.document= canvas.Canvas(os.environ["USERPROFILE"] + "/Documents/CompassX/" + self.db["NOME"] + "/Protocolos" + "/" + self.db["NOME"].replace(" ","_")+ complementoid + ".pdf",self.PAGESIZE, bottomup=0)
        path= f"""explorer.exe "{os.environ['USERPROFILE']}\Documents\CompassX\{self.db['NOME']}"""
        os.system(path)
        