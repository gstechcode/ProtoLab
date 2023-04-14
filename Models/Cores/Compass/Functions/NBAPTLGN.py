class NBAPTLGN:
	def __init__(self, master):
		self.fdict= master.csv
		self.master= master
		self.load("2d NBa-PtLGn","NBa-PtLGn")
	def load(self, fator1, name):
		if(self.master.csv[fator1] == ""):
			self.master.fdict[name]= {
			name: "",
			"desvio": 404,
			"formula": 404,
			"color": "white"
			}
			return 0
		if(self.fdict[fator1][0] >= 87 and self.fdict[fator1][0] <= 91):
			desvio= 0
		else:
			if(self.fdict[fator1][0] >= 85 and self.fdict[fator1][0] < 87):
				desvio= 1
			else:
				if(self.fdict[fator1][0] > 91 and self.fdict[fator1][0] <= 93):
					desvio= 2
				else:
					if(self.fdict[fator1][0] < 85):
						desvio= 3
					else:
						desvio= 4
		if(desvio >= 3):
			color= "red"
		elif(desvio < 3 and desvio >= 1):
			color= "yellow"
		elif(desvio < 1):
			color= "green"
		else:
			color= ""

		self.master.fdict[name]= {
			 name: str(self.fdict[fator1][0]) + self.fdict[fator1][1],
			"desvio": desvio,
			"formula": desvio,
			"color": color
		}
	def response(self):
		if(self.master.fdict["NBa-PtLGn"]["formula"] == 0):
			return "Eixos faciais semelhantes."
		elif(self.master.fdict["NBa-PtLGn"]["formula"] == 1):
			return "Padrão facial ligeiramente vertical."
		elif(self.master.fdict["NBa-PtLGn"]["formula"] == 2):
			return "Padrão facial ligeiramente horizontal."
		elif(self.master.fdict["NBa-PtLGn"]["formula"] == 3):
			return "Padrão facial vertical."
		elif(self.master.fdict["NBa-PtLGn"]["formula"] == 4):
			return "Padrão facial horizontal."
		else:
			return ""
