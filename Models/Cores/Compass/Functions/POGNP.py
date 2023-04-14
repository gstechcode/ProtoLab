class POGNP:
	def __init__(self, master):
		self.fdict= master.csv
		self.master= master
		self.load("2, Pog - Np","Pog - Np")
	def load(self, fator, name):
		if(self.master.csv[fator] == ""):
			self.master.fdict[name]= {
			name: "",
			"desvio": 404,
			"formula": 404,
			"color": "white"
			}
			return 0
		self.fdict[fator][0] = self.fdict[fator][0] * self.master.pognp
		anp= self.fdict[fator][0]
		if(self.master.denticao == "Decídua" or self.master.denticao == "Mista"):
			if(anp > -8 and anp < -6):
				desv= 0
			else:
				if(anp < -8):
					desv= 1
				else:
					desv= 2
		else:
			if(anp > -2 and anp < 4):
				desv= 0
			else:
				if(anp < -2):
					desv= 1
				else:
					desv= 2

		if(self.master.denticao == "Permanente"):
			if(anp >= -2 and anp <= 4):
				res= 0
			else:
				if(anp >= -4 and anp <= 6):
					res= 2
				else:
					res= 3
		else:
			if(anp >= -8 and anp <= -6):
				res= 0
			else:
				if(anp >= -10 and anp <= -4):
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
		average= round(self.master.fdict["Pog - Np"]["formula"])
		if(self.fdict["2, Pog - Np"][0] == ""):
			return ""
		else:
			if(self.master.fdict["Pog - Np"]["formula"] == 0):
				return "Ortognatismo mandibular."
			elif(self.master.fdict["Pog - Np"]["formula"] == 1):
				return "Retrognatismo mandibular."
			elif(self.master.fdict["Pog - Np"]["formula"] == 2):
				return "Prognatismo mandibular."
