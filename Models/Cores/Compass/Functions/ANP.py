class ANP:
	def __init__(self, master):
		self.fdict= master.csv
		self.master= master
		self.load("2, A - Np","A - Np")
	def load(self, fator, name):
		if(self.master.csv[fator] == ""):
			self.master.fdict[name]= {
			name: "",
			"desvio": 404,
			"formula": 404,
			"color": "white"
			}
			return 0
		self.fdict[fator][0] = self.fdict[fator][0] * self.master.anp
		anp= self.fdict[fator][0]
		if(self.master.denticao == "Decídua" or self.master.denticao == "Mista"):
			if(anp > -1 and anp < 1):
				desv= 0
			else:
				if(anp < -1):
					desv= 1
				else:
					desv= 2
		else:
			if(anp > 0 and anp < 2):
				desv= 0
			else:
				if(anp < 0):
					desv= 1
				else:
					desv= 2

		if(self.master.denticao == "Permanente"):
			if(anp >= 0 and anp < 2):
				res= 0
			else:
				if(anp >= -2 and anp <= 4):
					res= 2
				else:
					res= 3
		else:
			if(anp >= -1 and anp <= 1):
				res= 0
			else:
				if(anp >= -3 and anp <= 3):
					res= 2
				else:
					res= 3

		if(res >= 3):
			color= "red"
		elif(res < 3 and res >= 1):
			color= "yellow"
		else:
			color= "green"

		self.master.fdict[name]= {
			name: str(self.fdict[fator][0]) + str(self.fdict[fator][1]),
			"desvio": desv,
			"formula": desv,
			"color": color
		}
	def response(self):
		average= round(self.master.fdict["A - Np"]["formula"])
		if(self.fdict["2, A - Np"][0] == ""):
			return ""
		else:
			if(self.master.fdict["A - Np"]["formula"] == 0):
				return "Ortognatismo maxilar."
			elif(self.master.fdict["A - Np"]["formula"] == 1):
				return "Retrognatismo maxilar."
			elif(self.master.fdict["A - Np"]["formula"] == 2):
				return "Prognatismo maxilar."
