from Models.Cores.Compass.Functions.desvio import desvio

class HC(desvio):
	def __init__(self, master):
		self.fdict= master.csv
		self.master= master
		self.load("_13 Height Camper","1b 23 Height Camper", "13 Height Camper","23 Height Camper","HC1323")
		self.load("1e 14 Height Camper","1f 24 Height Camper", "14 Height Camper","24 Height Camper","HC1424")
		self.load("1i 16 Height Camper","1j 26 Height Camper", "16 Height Camper","26 Height Camper","HC1626")
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

	def response(self):
		average= round((self.master.fdict["HC1323"]["formula"] + self.master.fdict["HC1424"]["formula"] + self.master.fdict["HC1626"]["formula"])/3)
		if(average == 0):
			return "Planos oclusais simétricos no aspecto vertical."
		elif(average == 1):
			return "Planos oclusais ligeiramente assimétricos no aspecto vertical."
		elif(average == 2):
			return "Planos oclusais assimétricos no aspecto vertical."
		else:
			return ""