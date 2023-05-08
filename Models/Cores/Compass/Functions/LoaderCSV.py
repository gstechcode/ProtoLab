import csv
from functools import partial

#Carrega o CSV, e formata para o protocolo Compass
class LoaderCSV:
	def __init__(self, path):
		self.vars= [
			"2h SNA",
			"31 P, Holdaway",
			"11 / NA",
			"21/ NA",
			"11/ NA mm",
			"21/ NA mm",
			"11/ A-Pog",
			"21/ A-Pog",
			"11/ A-Pog mm",
			"21/ A-Pog mm",
			"41 P, Holdaway",
			"Ângulo 21/31",
			"Ângulo 11/41",
			"Pog P, Holdaway",
			"IMPA Esq",
			"IMPA Dir",
			"CondL GoL",
			"1b 23 Height Camper",
			"CondR GoR",
			"POEF 11",
			"POEF 21",
			"POEF31",
			"POEF 41",
			"2q JR Camper",
			"2p JL Camper",
			"3DA CAPITULARE R PL, CORONAL",
			"1t 46 Coronal Plane",
			"2bB2 Left Lower Facial Height",
			"2b Lower Facial Height",
			"1h 24 X MSP",
			"2i SNB",
			"JR MSP",
			"2bB1 Right Lower Facial Height",
			"1tc 13 VL Inclination",
			"3 Midline Evaluation",
			"2oa GoR Camper",
			"2u,, MeFR Coronal Plane",
			"1o 36 X MSP",
			"2 Skeletal Evaluation",
			"1q 16 Coronal Plane",
			"1ta 16 VL Inclination",
			"1tf  36 VL Inclination",
			"Espaço ATM Sup Esq",
			"Espaço ATM Sup Dir",
			"Espaço ATM Post Esq",
			"Espaço ATM Post Dir",
			"Espaço ATM Ant Esq",
			"Espaço ATM Ant Dir",
			"2e NBa-PtRGn",
			"2f SpPol - GoLMe",
			"1d 23 X MSP",
			"1l  26 X MSP",
			"1f 24 Height Camper",
			"2l CondL - Gn",
			"2t MeFL X MSP",
			"2r MeFL X Camper",
			"JL MSP",
			"2m CondR - Gn",
			"3d Capitulare R MSP",
			"2z Condylar Axis Left",
			"2g SpPoR - GoRMe",
			"1th 33 VL Inclination",
			"2, A - Np",
			"GoL MSP",
			"2oc GoR Coronal Pl",
			"_13 Height Camper",
			"2c Cranial Base Angle",
			"1g 14 X MSP",
			"2ob GoL Coronal Pl",
			"2d NBa-PtLGn",
			"1p 46 X MSP",
			"Upper Dental Midline",
			"1r 26  Coronal Plane",
			"1td 23 VL Inclination",
			"_ Dental Evaluation",
			"Lower Dental Midline",
			"1i 16 Height Camper",
			"2s MeFR X Camper",
			"3DC CAPITULARE L PL, FRANKFURT",
			"2j CondL - A",
			"1c 13 X MSP",
			"2a Upper Facial Height",
			"1te 46 VL Inclination",
			"Gn MSP",
			"2k CondR - A",
			"3f Corpus Length Right",
			"2u MeFR X MSP",
			"GoR MSP",
			"1m 33 X MSP",
			"1tg 43 VL Inclination",
			"2u,  MeFL Coronal Plane",
			"3c Capitulare L MSP",
			"2n GoL Camper",
			"1e 14 Height Camper",
			"1n 43 X MSP",
			"NSL x NL",
			"3DB CAPITULARE L PL, CORONAL",
			"2z Condylar Axis Right",
			"NSL x ML",
			"1tb 26 VL Inclination",
			"1k 16 X MSP",
			"1j 26 Height Camper",
			"3e Corpus Length Left",
			"1s 36 Coronal Plane",
			"2, Pog - Np",
			"3DD CAPITULARE R PL, FRANKFURT",
			"POR-POL",
			"GOR-GOL",
			"Ângulo Goníaco Left",
			"Ângulo Goníaco Right",
			"T-TM ESQ",
			"T-TM DIR"
		]
		self.file= []
		self.proto= {}
		with open(path, newline='') as f:
			reader = csv.reader(f, delimiter=";")
			for row in reader:
				self.file.append(row)
	def forDict(self):
		self.proto["ID"]= self.file[1][1]
		self.proto["Name"]= self.file[1][3]
		gender= self.file[2][3]
		if(gender == "F" or gender == "f"):
			self.proto["Gender"]= "Feminino"
		elif(gender == "M" or gender == "m"):
			self.proto["Gender"]= "Masculino"
		else:
			self.proto["Gender"]= "-"
		self.proto["DataScan"]= self.file[2][1].split(" ")[0]
		print(self.proto["DataScan"])
		for csv in self.vars:
			for variables in self.file:
				if(csv in variables):
					self.proto[csv]= variables[1]
		for i in self.proto:
			if("°" in self.proto[i]):
				self.proto[i]= self.proto[i].replace(" ","")
				self.proto[i]= self.proto[i].split("°")
				self.proto[i][0]= self.proto[i][0].replace(",",".")
				self.proto[i][0]= float(self.proto[i][0])
				self.proto[i][1]= "°"
			elif("mm" in self.proto[i]):
				self.proto[i]= self.proto[i].replace(" ","")
				self.proto[i]= self.proto[i].split("mm")
				self.proto[i][0]= self.proto[i][0].replace(",",".")
				self.proto[i][0]= float(self.proto[i][0])
				self.proto[i][1]= "mm"
		return self.proto