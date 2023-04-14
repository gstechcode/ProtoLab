class SNA:
	def __init__(self, master):
		self.fdict= master.csv
		self.master= master
		self.load("2h SNA","SNA")
	def load(self, fator1, name1):
		if(self.master.csv[fator1] == ""):
			self.master.fdict[name]= {
			name: "",
			"desvio": 404,
			"formula": 404,
			"color": "white"
			}
			return 0
		relacao= name1
		if(self.fdict[fator1][0] >= 79 and self.fdict[fator1][0] <= 85):
			desv= 0
		else:
			if(self.fdict[fator1][0] < 79):
				desv= 1
			else:
				desv= 2
		res= desv

		if(res >= 3):
			color= "red"
		elif(res < 3 and res >= 1):
			color= "yellow"
		elif(res < 1):
			color= "green"

		self.master.fdict[relacao]= {
			name1: str(self.fdict[fator1][0]) + self.fdict[fator1][1],
			"desvio": desv,
			"formula": res,
			"color": color
		}
	def response(self):
		if(self.master.fdict["SNA"]["formula"] == 0):
			return "Ortognatismo Maxilar."
		elif(self.master.fdict["SNA"]["formula"] == 1):
			return "Retrognatismo Maxilar."
		elif(self.master.fdict["SNA"]["formula"] == 2):
			return "Prognatismo Maxilar."
