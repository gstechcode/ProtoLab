from Models.Cores.Compass.Functions.desvio import desvio

class GOLRGN(desvio):
	def __init__(self, master):
		self.fdict= master.csv
		self.master= self.master
		self.load("3e Corpus Length Left","3f Corpus Length Right","GoL Gn","GoR Gn","GOLRGN")
	def load(self, fator1, fator2, name1, name2, relacao):
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
		response= 0
		desv= super().__init__(fator1,fator2, self.master)
		desv= abs(float("%.2f" % desv))
		if(desv <= 1):
			response= 0
		else:
			if(desv > 2):
				response= 2
			else:
				response= 1

		if(response >= 2):
			color= "red"
		elif(response < 2 and response >= 1):
			color= "yellow"
		elif(response < 1):
			color= "green"
		else:
			color= ""

		self.master.fdict[relacao]= {
			name1: str(self.fdict[fator1][0]) + self.fdict[fator1][1],
			name2: str(self.fdict[fator2][0]) + self.fdict[fator2][1],
			"desvio": desv,
			"formula": response,
			"color": color
		}

	def response(self):
		if(self.master.fdict["GOLRGN"]["formula"] == 0):
			return "Corpos mandibulares simétricos."
		elif(self.master.fdict["GOLRGN"]["formula"] == 1):
			return "Corpos mandibulares ligeiramente assimétricos."
		elif(self.master.fdict["GOLRGN"]["formula"] == 2):
			return "Corpos mandibulares assimétricos."
		else:
			return ""


