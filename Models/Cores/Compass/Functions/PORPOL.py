class PORPOL:
    def __init__(self, master):
        self.fdict= master.csv
        self.master= master
        self.load("POR-POL","POR-POL")
    def load(self, fator, name):
        self.master.fdict[name]= {
            name: str(self.fdict[fator][0]) + str(self.fdict[fator][1]),
            "desvio": 0,
            "formula": 0,
            "color": "white"
		}