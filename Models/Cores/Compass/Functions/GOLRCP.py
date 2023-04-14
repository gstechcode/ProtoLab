from Models.Cores.Compass.Functions.desvio import desvio

class GOLRCP(desvio):
	def __init__(self, master):
		self.fdict= master.csv
		self.master= master
		self.load("2ob GoL Coronal Pl","2oc GoR Coronal Pl","GoL Coronal Plane","GoR Coronal Plane","GOLRCP")
	def load(self, fator1, fator2, name1, name2, relacao):
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
			res= 0
		else:
			if(self.fdict[fator2][0] < self.fdict[fator1][0]):
				if(desv > 2):
					res= 3
				else:
					res= 1
			else:
				if(desv > 2):
					res= 4
				else:
					res= 2

		if(res >= 3):
			color= "red"
		elif(res < 3 and res >= 1):
			color= "yellow"
		elif(res < 1):
			color= "green"
		else:
			color= ""

		self.master.fdict[relacao]= {
			name1: str(self.fdict[fator1][0]) + self.fdict[fator1][1],
			name2: str(self.fdict[fator2][0]) + self.fdict[fator2][1],
			"desvio": desv,
			"formula": res,
			"color": color
		}
	def response(self):
		if(self.master.fdict["GOLRCP"]["formula"] == 0):
			return "Ramos mandibulares equidistantes ao Plano Coronal"
		elif(self.master.fdict["GOLRCP"]["formula"] == 1):
			return "Ramo mandibular esquerdo ligeiramente mais anterior"
		elif(self.master.fdict["GOLRCP"]["formula"] == 2):
			return "Ramo mandibular direito ligeiramente mais anterior"
		elif(self.master.fdict["GOLRCP"]["formula"] == 3):
			return "Ramo mandibular esquerdo mais anterior"
		elif(self.master.fdict["GOLRCP"]["formula"] == 4):
			return "Ramo mandibular direito mais anterior"
		else:
			return ""