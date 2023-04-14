from Models.Cores.Compass.Functions.desvio import desvio

class XMSP(desvio):
	def __init__(self,master):
		self.fdict= master.csv
		self.master= master
		self.load("1c 13 X MSP","1d 23 X MSP","13 X MSP","23 X MSP","MSP1323")
		self.load("1g 14 X MSP","1h 24 X MSP","14 X MSP","24 X MSP","MSP1424")
		self.load("1k 16 X MSP","1l  26 X MSP","16 X MSP","26 X MSP","MSP1626")
		self.load("1m 33 X MSP","1n 43 X MSP","33 X MSP","43 X MSP","MSP3343")
		self.load("1o 36 X MSP","1p 46 X MSP","36 X MSP","46 X MSP","MSP3646")
	def load(self,fator1,fator2, name1, name2, relacao):
		response= 0
		if(self.master.csv[fator1] == "" and self.master.csv[fator2] == ""):
			self.master.fdict[relacao]= {
			name1: "",
			name2: "",
			"desvio": 404,
			"formula": 404,
			"color": "white"
			}
			return 0
		elif(self.master.csv[fator1] == ""):
			self.master.fdict[relacao]= {
			name1: "",
			name2: str(self.fdict[fator2][0]) + self.fdict[fator2][1],
			"desvio": 404,
			"formula": 404,
			"color": "white"
			}
			return 0
		elif(self.master.csv[fator2] == ""):
			self.master.fdict[relacao]= {
			name1: str(self.fdict[fator1][0]) + self.fdict[fator1][1],
			name2: "",
			"desvio": 404,
			"formula": 404,
			"color": "white"
			}
			return 0
		desv= super().__init__(fator1,fator2, self.master)
		desv= abs(float("%.2f" % desv))
		if(desv <= 1):
			response= 0
		elif(desv > 3):
			response= 2
		else:
			response= 1
		if(desv >= 3):
			color= "red"
		elif(desv < 3 and desv >= 1):
			color= "yellow"
		elif(desv < 1):
			color= "green"
		#associa a relacao para criar um dict com o as informações
		self.master.fdict[relacao]= {
			name1: str(self.fdict[fator1][0]) + self.fdict[fator1][1],
			name2: str(self.fdict[fator2][0]) + self.fdict[fator2][1],
			"desvio": desv,
			"formula": response,
			"color": color
		}
	def response131416(self):
		average= round((self.master.fdict["MSP1323"]["formula"] + self.master.fdict["MSP1424"]["formula"] + self.master.fdict["MSP1626"]["formula"])/3)
		if(average == 0):
			return "Planos oclusais simétricos no aspecto transversal."
		elif(average == 1):
			return "Planos oclusais ligeiramente assimétricos no aspecto transversal."
		elif(average == 2):
			return "Planos oclusais assimétricos no aspecto transversal."
		else:
			return ""
	def response3343(self):
		average= self.master.fdict["MSP3343"]["formula"]
		if(average == 0):
			return "Hemi-arcos mandibulares simétricos ao MSP (Plano Sagital Mediano)."
		elif(average == 1):
			return "Hemi-arcos mandibulares ligeiramente assimétricos ao MSP (Plano Sagital Mediano)."
		elif(average == 2):
			return "Hemi-arcos mandibulares assimétricos ao MSP (Plano Sagital Mediano)."
		else:
			return ""
	def response3646(self):
		average= self.master.fdict["MSP3646"]["formula"]
		if(average == 0):
			return "Hemi-arcos mandibulares simétricos ao MSP (Plano Sagital Mediano)."
		elif(average == 1):
			return "Hemi-arcos mandibulares ligeiramente assimétricos ao MSP (Plano Sagital Mediano)."
		elif(average == 2):
			return "Hemi-arcos mandibulares assimétricos ao MSP (Plano Sagital Mediano)."
		else:
			return ""