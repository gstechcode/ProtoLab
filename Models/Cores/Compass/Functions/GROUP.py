class GROUP:
	def __init__(self, master):
		self.master= master
		self.sna= self.master.csv["2h SNA"][0]
		self.snb= self.master.csv["2i SNB"][0]
		self.mlnsl= self.master.csv["NSL x ML"][0]
		self.nlnsl= self.master.csv["NSL x NL"][0]
		self.__process__()
	def __process__(self):
		T1, T2, T3= {}, {}, {}
		T1["MLesp"]= 192 - (self.snb * 2)
		T1["T1"]= T1["MLesp"] - self.mlnsl
		T2["NLesp"]= (self.mlnsl/2) - 7
		T2["T2"]= T2["NLesp"] - self.nlnsl
		T3["T3"]= self.sna - self.snb

		T1= float("%.2f" % round(T1["T1"],2))
		T2= float("%.2f" % round(T2["T2"],2))
		T3= float("%.2f" % round(T3["T3"],2))
		#quadro1
		if(T1 > 6):
			if(T2 > 3):
				if(T3 <= 1.5):
					gp= "A3M DB"
					cat= 6
				elif(T3 > 1.5 and T3 <= 5.5):
					gp= "A1N OB"
					cat= 5
				elif(T3 > 5,5 and T3 <= 8.5):
					gp= "A1D OB"
					cat= 5
				elif(T3 > 8.5):
					gp= "A2D OB"
					cat= 2
			elif(T2 <= 3 and T2 >= 0):
				if(T3 <= 0):
					gp= "A3M N"
					cat= 6
				elif(T3 > 0 and T3 <= 4):
					gp= "A1N N"
					cat= 5
				elif(T3 > 4 and T3 <= 7):
					gp= "A1D N"
					cat= 5
				elif(T3 > 7):
					gp= "A2D N"
					cat= 2
			elif(T2 < 0):
				if(T3 <= -1.5):
					gp="A3M DB"
					cat= 6
				elif(T3 > -1.5 and T3 <= 3):
					gp= "A1N DB"
					cat= 5
				elif(T3 > 3 and T3 <= 6):
					gp= "A1D DB"
					cat= 5
				elif(T3 > 6):
					gp= "A2D DB"
					cat= 2
		#fimquadro1
		#quadro2
		elif(T1 <= 6 and T1 >= 0):
			if(T2 > 3):
				if(T3 <= 1):
					gp= "R3M OB"
					cat= 5
				elif(T3 > 1 and T3 <= 5):
					gp= "R1N OB"
					cat= 4
				elif(T3 > 5):
					gp= "R2D OB"
					cat= 3
			elif(T2 <= 3 and T2 >= 0):
				if(T3 <= 0):
					gp= "R3M N"
					cat= 5
				elif(T3 > 0 and T3 <= 4):
					gp= "R1N N"
					cat= 4
				elif(T3 > 4):
					gp= "R2D N"
					cat= 3
			elif(T2 < 0):
				if(T3 <= -1):
					gp= "R3M DB"
					cat= 5
				elif(T3 > -1 and T3 <= 3):
					gp= "R1N DB"
					cat= 4
				elif(T3 > 3):
					gp= "R2D DB"
					cat= 3
		#fimquadro2
		#quadro3
		elif(T1 < 0):
			if(T2 > 3):
				if(T3 >= 5.5):
					gp= "P2D OB"
					cat= 1
				elif(T3 >= 1 and T3 < 5.5):
					gp= "P1N OB"
					cat= 2
				elif(T3 >= -6 and T3 < 1):
					gp= "P1M OB"
					cat= 5
				elif(T3 < -6):
					gp= "P3M OB"
					cat= 6
			elif(T2 <= 3 and T2 >= 0):
				if(T3 >= 4):
					gp= "P2D N"
					cat= 1
				elif(T3 >= 0 and T3 < 4):
					gp= "P1N N"
					cat= 2
				elif(T3 >= -7 and T3 < 0):
					gp= "P1M N"
					cat= 5
				elif(T3 < -7):
					gp= "P3M N"
					cat= 6
			elif(T2 < 0):
				if(T3 >= 3):
					gp= "P2D DB"
					cat= 1
				elif(T3 >= -1 and T3 < 3):
					gp= "P1N DB"
					cat= 2
				elif(T3 >= -8 and T3 < -1):
					gp= "P1M DB"
					cat= 5
				elif(T3 < -8):
					gp= "P3M DB"
					cat= 6
		self.master.fdict["GrupoR"] = gp
		self.master.fdict["CatAux"]= cat





