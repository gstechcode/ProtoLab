class TTMLR:
    def __init__(self, master):
        self.fdict= master.csv
        self.master= master
        self.load("T-TM ESQ","T-TM ESQ","T-TM DIR","T-TM DIR","TTMLR")
    def load(self, fator1, name1, fator2, name2, relacao):
        if(float(self.fdict[fator1][0]) < 28):
            colorL= "yellow"
        elif(float(self.fdict[fator1][0]) > 32):
            colorL= "green"
        elif(float(self.fdict[fator1][0]) >= 28 and float(self.fdict[fator1][0]) <= 32):
            colorL= "red"
            
        if(float(self.fdict[fator2][0]) < 28):
            colorR= "yellow"
        elif(float(self.fdict[fator2][0]) > 32):
            colorR= "green"
        elif(float(self.fdict[fator2][0]) >= 28 and float(self.fdict[fator2][0]) <= 32):
            colorR= "red"
            
        self.master.fdict[relacao]= {
            name1: str(self.fdict[fator1][0]) + str(self.fdict[fator1][1]),
            name2: str(self.fdict[fator2][0]) + str(self.fdict[fator2][1]),
            "desvio": 0,
            "formula": 0,
            "colorR": colorR,
            "colorL": colorL,
		}