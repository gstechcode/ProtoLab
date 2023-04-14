class AGLR:
    def __init__(self, master):
        print("Executei")
        self.fdict= master.csv
        self.master= master
        self.load("Ângulo Goníaco Right","AGR","Ângulo Goníaco Left","AGL","AGLR")
    def load(self, fator1, name1, fator2, name2, relacao):
        self.master.fdict[relacao]= {
            name1: str(self.fdict[fator1][0]) + str(self.fdict[fator1][1]),
            name2: str(self.fdict[fator2][0]) + str(self.fdict[fator2][1]),
            "desvio": 0,
            "formula": 0,
            "color": "white"
		}
        