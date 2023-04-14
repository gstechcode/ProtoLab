from reportlab.pdfgen import canvas
from Libs.variables import *
from Libs.Reports.PDFs.components import backgrounds, structure, photos
import os, json
from Resources.Tools import GenOdontograma

class pcc3d(
    backgrounds.backgrounds,
    structure.structure,
    photos.photos):
    def __init__(self, docname):
        super().__init__()
        self.docname= docname
        self.__vars__()
        self.Cover()
        self.Page1()
        self.Page2()
        self.Page3()
        self.Page4()
        self.Page5()
        self.Page6()
        self.Page7()
        self.Page8()
        self.Page9()
        self.Page10()
        self.Page11()
        self.Page12()
        self.Page13()
        self.Page14()
        self.Page15()
        self.setBackgroundEnd()
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
        self.drawText(970, 820, "Grupo Rotacional: {GrupoR} :: Categoria Auxológica: {Cat}".format(GrupoR= self.db["GrupoR"], Cat= self.db["CatAux"]), 35)
        self.drawImage(os.getcwd() + "/Resources/Images/temp/profile.png", 1000,750, width=700, height= 700)
        self.document.showPage()
        
    def Page2(self):
        self.textSize= 32
        self.setBody()
        spacing= 60
        desvio= 0
        x1, y1, x2, y2= 40,530,1350,530
        justify= 95
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
        self.document.rect(40,215,400,90, fill=0, stroke= 1)
        self.drawText(60,250,"Distância em Milímetros dos dentes aos", 20)
        self.drawText(60,280,"Planos de Camper e P. Sagital Mediano", 20)
        self.drawImage(os.getcwd() + "/Resources/Images/temp/FT.png",620,850, mask= "auto")
        self.document.showPage()

    def Page3(self):
        self.setBody()
        self.drawText(60,120,"Posição dos Gônios",self.titleSize, self.ORANGE)
        self.drawText(20,550,"Gônio Direito",self.textSize + 5)
        self.drawText(20,625,"Profundidade do Gônio Direito " + self.db["GOLRCP"]["GoL Coronal Plane"],self.textSize)
        self.drawText(20,675,"Distância Gônio Direito ao P. Camper " + self.db["GoLRCamper"]["GoL Camper"],self.textSize)
        self.drawText(20,725,"Gônio Direito X P.S.M " + self.db["GOLRMSP"]["GoL MSP"],self.textSize)
        
        self.drawText(1640,550,"Gônio Esquerdo",self.textSize + 5)
        self.drawText(1310,625,"Profundidade do Gônio Esquerdo " + self.db["GOLRCP"]["GoR Coronal Plane"],self.textSize)
        self.drawText(1220,675,"Distância Gônio Esquerdo ao P. Camper " + self.db["GoLRCamper"]["GoR Camper"],self.textSize)
        self.drawText(1425,725,"Gônio Esquerdo X P.S.M " + self.db["GOLRMSP"]["GoR MSP"],self.textSize)
        
        self.document.drawCentredString(self.PAGESIZE[0]/2,910,self.db["response"]["GOLRCP"])
        self.document.drawCentredString(self.PAGESIZE[0]/2,960,self.db["response"]["GOLRCAMPER"])
        self.document.drawCentredString(self.PAGESIZE[0]/2,1010,self.db["response"]["GOLRMSP"])
        self.drawImage(os.getcwd() + "/Resources/Images/temp/PG.png",590,850, mask= "auto")
        self.document.showPage()
        
    def Page4(self):
        self.textSize= 30

        self.setBody()
        self.drawText(60,120,"Dimensões das", self.titleSize, self.ORANGE)
        self.drawText(60,190,"Hemi-Mandíbulas", self.titleSize, self.ORANGE)

        self.drawText(40,645,"Diagonal Mandibular Direita " + self.db["CondLRGN"]["CondR - Gn"], self.textSize)
        self.drawText(40,695,"Comprimento do Ramo Mandibular Direita " + self.db["CONDLRGOLR"]["CondR GoR"], self.textSize)
        self.drawText(40,745,"Comprimento do Corpo Mandibular Direita " + self.db["CORPUSLR"]["Corpus R"], self.textSize)
        
        self.drawText(1340,645,"Diagonal Mandibular Esquerda " + self.db["CondLRGN"]["CondL - Gn"], self.textSize)
        self.drawText(1180,695,"Comprimento do Ramo Mandibular Esquerda " + self.db["CONDLRGOLR"]["CondL GoL"], self.textSize)
        self.drawText(1180,745,"Comprimento do Corpo Mandibular Esquerda " + self.db["CORPUSLR"]["Corpus L"], self.textSize)

        self.document.drawCentredString(self.PAGESIZE[0]/2,910,self.db["response"]["CONDLRGN"])
        self.document.drawCentredString(self.PAGESIZE[0]/2,960,self.db["response"]["CONDLRGOLR"])
        self.document.drawCentredString(self.PAGESIZE[0]/2,1010,self.db["response"]["GOLRGN"])
        
        self.drawImage(os.getcwd() + "/Resources/Images/temp/DH.png",590,850, mask= "auto")
        
        self.document.showPage()
        
        
    def Page5(self):

        self.setBody()

        self.drawText(60,120,"Altura Facial",self.titleSize, self.ORANGE)
        
        self.drawText(40,745,"Altura Facial Ântero-superior AFAS " + self.db["AFASI"]["AFAS"],self.textSize)
        self.drawText(1300,745,"Altura Facial Ântero-inferior AFAI " + self.db["AFASI"]["AFAI"],self.textSize)
        
        self.document.drawCentredString(self.PAGESIZE[0]/2,960,self.db["response"]["ULH"])
        
        self.drawImage(os.getcwd() + "/Resources/Images/temp/AF.png",620,850, mask= "auto")
        
        self.document.showPage()
        
    def Page6(self):

        self.setBody()

        self.drawText(60,120,"Forma da Mandíbula", self.titleSize, self.ORANGE)

        self.drawText(60,497,"Ângulo Goníaco Direito " + self.db["AFASI"]["AFAS"], self.textSize)
        self.drawText(60,745,"Eixo Condilar Direito " + self.db["AFASI"]["AFAI"], self.textSize)

        self.drawText(1400,497,"Ângulo Goníaco Esquerdo " + self.db["AFASI"]["AFAS"], self.textSize)
        self.drawText(1430,745,"Eixo Condilar Esquerdo " + self.db["AFASI"]["AFAI"], self.textSize)
        
        self.drawImage(os.getcwd() + "/Resources/Images/temp/FM.png",620,880, mask= "auto")
        
        self.document.showPage()
    
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
    
    def Page8(self):

        self.setBody()
        
        self.drawText(1920/2,140,"Incisivos", self.titleSize, self.ORANGE)
        self.drawText(1920/2 + 100,330,"Incisivo Central Esquerdo x Linha Holdaway " + self.db["P, Holdaway"]["31"], self.textSize)
        self.drawText(1920/2 + 140,385,"Incisivo Central Direito x Linha Holdaway " + self.db["P, Holdaway"]["41"], self.textSize)
        self.drawText(1920/2 + 370,440,"Pogônio x Linha Holdaway " + self.db["Pog P, Holdaway"]["Pog P, Holdaway"], self.textSize)
        self.drawText(1920/2 + 510,495,"Distância H-Nariz 0,00mm", self.textSize)
        self.drawText(1920/2 + 570,550,"IMPA Esquerdo " + self.db["IMPA"]["31"], self.textSize)
        self.drawText(1920/2 + 610,605,"IMPA Direito " + self.db["IMPA"]["41"], self.textSize)
        self.drawText(1920/2 + 220,660,"Ângulo Interincisivos Centrais Direitos " + self.db["ANG21311141"]["ANG1141"], self.textSize)
        self.drawText(1920/2 + 160,715,"Ângulo Interincisivos Centrais Esquerdos " + self.db["ANG21311141"]["ANG2131"], self.textSize)

        #self.drawImage(os.getcwd() + "/Resources/Images/temp/INC.png",-562,1142, mask= "auto")

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
  
        self.drawText(self.PAGESIZE[0]/2,140,"Incisivos", self.titleSize, self.ORANGE)

        self.drawText(self.PAGESIZE[0]/2 + 220,330,f"Ângulo {teeth11} Linha NA " + self.db["NA"]["ANG11"], self.textSize)
		
        self.drawText(self.PAGESIZE[0]/2 + 220,385,f"Ângulo {teeth21} Linha NA " + self.db["NA"]["ANG21"], self.textSize)

        self.drawText(self.PAGESIZE[0]/2 + 220,440,f"Distância {teeth11} Linha NA " + self.db["NA"]["MM11"], self.textSize)

        self.drawText(self.PAGESIZE[0]/2 + 220,495,f"Distância {teeth21} Linha NA " + self.db["NA"]["MM21"], self.textSize)
        
        self.drawText(self.PAGESIZE[0]/2 + 220,550,f"Distância {teeth11} Linha A-Pog " + self.db["APOG1121"]["APOG11MM"], self.textSize)

        self.drawText(self.PAGESIZE[0]/2 + 220,605,f"Distância {teeth21} Linha A-Pog " + self.db["APOG1121"]["APOG21MM"], self.textSize)
		
        #self.drawImage(os.getcwd() + "/Resources/Images/temp/INC.png",-562,1142, mask= "auto")
        
        self.document.showPage()
        
    def Page10(self):

        self.setBody()

		#self.pdf.drawImage(os.environ["USERPROFILE"] + "\\Documents\\LabReport\\TM.png",-270,-1060, mask= "auto")

        self.drawText(80,140,"Triângulo Mandibular", self.titleSize, self.ORANGE)

        self.drawText(self.PAGESIZE[0]/2 + 250,330,f"Gônio Esquerdo X P.S.M " + self.db["GOLRMSP"]["GoL MSP"], self.textSize)

        self.drawText(self.PAGESIZE[0]/2 + 250,385,f"Profundidade do Gônio Esquerdo " + self.db["GOLRCP"]["GoL Coronal Plane"], self.textSize)

        self.drawText(self.PAGESIZE[0]/2 + 250,440,f"Gônio Direito X P.S.M " + self.db["GOLRMSP"]["GoR MSP"], self.textSize)

        self.drawText(self.PAGESIZE[0]/2 + 250,495,f"Profundidade do Gônio Direito " + self.db["GOLRCP"]["GoR Coronal Plane"], self.textSize)

        self.drawText(self.PAGESIZE[0]/2 + 250,550,f"Gnátio X P.S.M " + self.db["GNMSP"]["Gn MSP"], self.textSize)

        self.drawText(self.PAGESIZE[0]/2 + 60,680,self.db["response"]["GNMSP"], self.textSize)

        self.drawText(self.PAGESIZE[0]/2 + 60,725,self.db["response"]["GOLRCP"], self.textSize)

        self.drawText(self.PAGESIZE[0]/2 + 60,770,self.db["response"]["GOLRMSP"], self.textSize)

        self.document.showPage()
        
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
		
        self.drawImage(os.getcwd() + "/Resources/Images/temp/PSGCF.png",270,-1060, mask= "auto")
  
        self.document.showPage()
        
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
        
        self.drawText(self.PAGESIZE[0]/2 - 40,730,self.db["response"]["CP1626"], self.textSize)
        
        self.drawText(self.PAGESIZE[0]/2 - 40,785,self.db["response"]["CP3646"], self.textSize)
        
        self.document.showPage()   

    def Page13(self):
        
        self.setBody()
        
        self.drawText(self.PAGESIZE[0]/2 - 40,120,"Espaços Articulares ATM Esquerda", self.titleSize, self.ORANGE)
        
        self.document.showPage()
  
    def Page14(self):
        
        self.setBody()
        
        self.drawText(self.PAGESIZE[0]/2 - 40,120,"Espaços Articulares ATM Direita", self.titleSize, self.ORANGE)

        self.document.showPage()
    
    def Page15(self):
		
        self.setBody()

        GenOdontograma.GenOdontograma(self.db)
        
        self.drawText(1570, 100, "Infográfico", self.titleSize, self.ORANGE)
        
        self.drawText(1700, 250, "Criado por", self.textSize)
        
        self.drawText(1500, 290, "Dra. Mara Rufato Cardoso", self.textSize)
        
        self.drawImage(os.getcwd() + "/Resources/Images/temp/odontograma.png",70,1000, width= 1326,height= 949, mask="auto")
        
        self.document.showPage()

    def setBackgroundEnd(self):
        self.document.scale(1,-1)
        self.document.drawImage(os.getcwd() + r"\Resources\Images\Final.png",-1,-1,self.PAGESIZE[0],-self.PAGESIZE[1])
        self.document.scale(1,-1)
        self.document.linkURL("https://www.instagram.com/compasscomvoce/?hl=pt",[950,270,530,190])
        self.document.linkURL("https://pt-br.facebook.com/CompassComVoce/",[1400,270,970,180])
        self.document.showPage()
  
    def __vars__(self):
        self.denticaoSlot= 1
        self.runPhotos()
        self.optimizeImages()
        self.titleSize= 60
        self.textSize= 45
        banco= open(os.getcwd() + "/Resources/Databases/PCTable.tbl", "r")
        self.db= json.loads(banco.readlines()[0])
        banco.close()
        self.PAGESIZE= (1920,1080)
        self.registerFont()
        self.ORANGE= (255/255,102/255,0/255)
        self.document= canvas.Canvas(self.docname,self.PAGESIZE, bottomup=0)
        