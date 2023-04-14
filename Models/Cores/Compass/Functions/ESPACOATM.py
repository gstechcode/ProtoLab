class ESPACOATM:
	def __init__(self, master):
		self.fdict= master.csv
		self.master= master
		self.load("Espaço ATM Sup Esq","Espaço ATM Sup Dir","Espaço ATM Post Esq","Espaço ATM Post Dir","Espaço ATM Ant Esq","Espaço ATM Ant Dir","EASUPESQ","EASUPDIR","EAPOSTESQ","EAPOSTDIR","EAANTESQ","EAANTDIR","ESPACOATM")
	def load(self, fator1, fator2, fator3, fator4, fator5, fator6, name1, name2, name3, name4, name5, name6, relacao):

		try:
			self.master.fdict[relacao]= {
				name1: str(self.fdict[fator1][0]) + self.fdict[fator1][1],
				name2: str(self.fdict[fator2][0]) + self.fdict[fator2][1],
				name3: str(self.fdict[fator3][0]) + self.fdict[fator3][1],
				name4: str(self.fdict[fator4][0]) + self.fdict[fator4][1],
				name5: str(self.fdict[fator5][0]) + self.fdict[fator5][1],
				name6: str(self.fdict[fator6][0]) + self.fdict[fator6][1],
				"desvio": 0,
				"formula": 0,
				"color": "white"
			}
		except Exception:
			self.master.fdict[relacao]= {
				name1: "",
				name2: "",
				name3: "",
				name4: "",
				name5: "",
				name6: "",
				"desvio": 0,
				"formula": 0,
				"color": "white"
			}

	def responses(self):
		responses= {}
		try:
			if(self.fdict["Espaço ATM Sup Esq"][0] > 4):
				responses["EASUPESQ"] = "Espaço articular superior aumentado na ATM  Esquerda"
			elif(self.fdict["Espaço ATM Sup Esq"][0] < 2.5):
				responses["EASUPESQ"] = "Espaço articular superior diminuído na ATM  Esquerda"
			elif(self.fdict["Espaço ATM Sup Esq"][0] <= 4 and self.fdict["Espaço ATM Sup Esq"][0] >= 2.5):
				responses["EASUPESQ"] = "Espaço articular superior adequado na ATM  Esquerda"
		except Exception:
			responses["EASUPESQ"] = ""

		try:
			if(self.fdict["Espaço ATM Sup Dir"][0] > 4):
				responses["EASUPDIR"] = "Espaço articular superior aumentado na ATM  Direita"
			elif(self.fdict["Espaço ATM Sup Dir"][0] < 2.5):
				responses["EASUPDIR"] = "Espaço articular superior diminuído na ATM  Direita"
			elif(self.fdict["Espaço ATM Sup Dir"][0] <= 4 and self.fdict["Espaço ATM Sup Dir"][0] >= 2.5):
				responses["EASUPDIR"] = "Espaço articular superior adequado na ATM  Direita"
		except Exception:
			responses["EASUPDIR"] = ""

		try:
			if(self.fdict["Espaço ATM Post Esq"][0] > 2.5):
				responses["EAPOSTESQ"] = "Espaço articular posterior aumentado na ATM Esquerda"
			elif(self.fdict["Espaço ATM Post Esq"][0] < 1.5):
				responses["EAPOSTESQ"] = "Espaço articular posterior diminuído na ATM  Esquerda"
			elif(self.fdict["Espaço ATM Post Esq"][0] <= 2.5 and self.fdict["Espaço ATM Post Esq"][0] >= 1.5):
				responses["EAPOSTESQ"] = "Espaço articular posterior adequado na ATM  Esquerda"
		except Exception:
			responses["EAPOSTESQ"] = ""


		try:
			if(self.fdict["Espaço ATM Post Dir"][0] > 2.5):
				responses["EAPOSTDIR"] = "Espaço articular posterior aumentado na ATM Direita"
			elif(self.fdict["Espaço ATM Post Dir"][0] < 1.5):
				responses["EAPOSTDIR"] = "Espaço articular posterior diminuído na ATM  Direita"
			elif(self.fdict["Espaço ATM Post Dir"][0] <= 2.5 and self.fdict["Espaço ATM Post Dir"][0] >= 1.5):
				responses["EAPOSTDIR"] = "Espaço articular posterior adequado na ATM  Direita"
		except Exception:
			responses["EAPOSTDIR"] = ""

		try:
			if(self.fdict["Espaço ATM Ant Esq"][0] > 2.5):
				responses["EAANTESQ"] = "Espaço articular anterior aumentado na ATM Esquerda"
			elif(self.fdict["Espaço ATM Ant Esq"][0] < 1.5):
				responses["EAANTESQ"] = "Espaço articular anterior diminuído na ATM  Esquerda"
			elif(self.fdict["Espaço ATM Ant Esq"][0] <= 2.5 and self.fdict["Espaço ATM Ant Esq"][0] >= 1.5):
				responses["EAANTESQ"] = "Espaço articular anterior adequado na ATM  Esquerda"
		except Exception:
			responses["EAANTESQ"] = ""

		try:
			if(self.fdict["Espaço ATM Ant Dir"][0] > 2.5):
				responses["EAANTDIR"] = "Espaço articular anterior aumentado na ATM Direita"
			elif(self.fdict["Espaço ATM Ant Dir"][0] < 1.5):
				responses["EAANTDIR"] = "Espaço articular anterior diminuído na ATM  Direita"
			elif(self.fdict["Espaço ATM Ant Dir"][0] <= 2.5 and self.fdict["Espaço ATM Ant Dir"][0] >= 1.5):
				responses["EAANTDIR"] = "Espaço articular anterior adequado na ATM  Direita"
		except Exception:
			responses["EAANTDIRs"] = ""

		return responses