from Models.Cores.Compass.Functions.desvio import desvio

class SPPOLGOLME(desvio):
	def __init__(self, master):
		self.fdict= master.csv
		self.master= master
		self.load("2f SpPol - GoLMe","2g SpPoR - GoRMe","SpPol-GoLMe","SpPol-GoRMe","SpPoLGoLRMe")
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
		desv= super().__init__(fator1,fator2,self.master)
		if(desv <= 1):
			res= 0
		else:
			if(desv > 2.5):
				res= 2
			else:
				res= 1

		if(desv >= 3):
			color= "red"
		elif(desv < 3 and desv >= 1):
			color= "yellow"
		elif(desv < 1):
			color= "green"
		else:
			color= ""

		self.master.fdict[relacao]= {
			name1: str(self.fdict[fator1][0]) + self.fdict[fator1][1],
			name2: str(self.fdict[fator2][0]) + self.fdict[fator2][1],
			"desvio": "%.2f" % round(desv,2),
			"formula": res,
			"color": color
		}
	def response(self):
		if(self.master.fdict["SpPoLGoLRMe"]["formula"] == 0):
			return "Ângulos da simetria facial simétricos."
		elif(self.master.fdict["SpPoLGoLRMe"]["formula"] == 1):
			return "Ângulos da simetria facial ligeiramente assimétricos."
		elif(self.master.fdict["SpPoLGoLRMe"]["formula"] == 2):
			return "Ângulos da simetria facial assimétricos."
		else:
			return ""
