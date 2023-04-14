import json
import os
from Libs.variables import *
from Models.Cores.Compass.Functions.AGLR import AGLR
from Models.Cores.Compass.Functions.LoaderCSV import LoaderCSV as Loader
from Models.Cores.Compass.Functions.HC import HC
from Models.Cores.Compass.Functions.CP import CP
from Models.Cores.Compass.Functions.XMSP import XMSP
from Models.Cores.Compass.Functions.VL import VL
from Models.Cores.Compass.Functions.ANP import ANP
from Models.Cores.Compass.Functions.POGNP import POGNP
from Models.Cores.Compass.Functions.UPPERLOWERHEIGHT import UPPERLOWERHEIGHT
from Models.Cores.Compass.Functions.PHOLDAWAY import PHOLDAWAY
from Models.Cores.Compass.Functions.POGPHOLDAWAY import POGPHOLDAWAY
from Models.Cores.Compass.Functions.RIGHTLFH import RIGHTLFH
from Models.Cores.Compass.Functions.LEFTLFH import LEFTLFH
from Models.Cores.Compass.Functions.CBA import CBA
from Models.Cores.Compass.Functions.NBAPTLGN import NBAPTLGN
from Models.Cores.Compass.Functions.NBAPTRGN import NBAPTRGN
from Models.Cores.Compass.Functions.SPPOLGOLME import SPPOLGOLME
from Models.Cores.Compass.Functions.SNA import SNA
from Models.Cores.Compass.Functions.SNB import SNB
from Models.Cores.Compass.Functions.CONDLRA import CONDLRA
from Models.Cores.Compass.Functions.CONDLRGN import CONDLRGN
from Models.Cores.Compass.Functions.GOLRCAMPER import GOLRCAMPER
from Models.Cores.Compass.Functions.GOLRCP import GOLRCP
from Models.Cores.Compass.Functions.JLRCAMPER import JLRCAMPER
from Models.Cores.Compass.Functions.MEFLRCAMPER import MEFLRCAMPER
from Models.Cores.Compass.Functions.MEFLRMSP import MEFLRMSP
from Models.Cores.Compass.Functions.MEFLRCP import MEFLRCP
from Models.Cores.Compass.Functions.APOG1121 import APOG1121
from Models.Cores.Compass.Functions.NA import NA
from Models.Cores.Compass.Functions.IMPA import IMPA
from Models.Cores.Compass.Functions.CARL import CARL
from Models.Cores.Compass.Functions.AFASI import AFASI
from Models.Cores.Compass.Functions.CORPUSLR import CORPUSLR
from Models.Cores.Compass.Functions.ESPACOATM import ESPACOATM
from Models.Cores.Compass.Functions.CAPITULARELRMSP import CAPITULARELRMSP
from Models.Cores.Compass.Functions.CAPITULARELRPCP import CAPITULARELRPCP
from Models.Cores.Compass.Functions.CAPITULARELRPFRANK import CAPITULARELRPFRANK
from Models.Cores.Compass.Functions.GOLRGN import GOLRGN
from Models.Cores.Compass.Functions.CONDLRGOLR import CONDLRGOLR
from Models.Cores.Compass.Functions.ANGULO21311141 import ANGULO21311141
from Models.Cores.Compass.Functions.GNMSP import GNMSP
from Models.Cores.Compass.Functions.POEF import POEF
from Models.Cores.Compass.Functions.GOLRMSP import GOLRMSP
from Models.Cores.Compass.Functions.JLRMSP import JLRMSP
from Models.Cores.Compass.Functions.LDM import LDM
from Models.Cores.Compass.Functions.NSLXML import NSLXML
from Models.Cores.Compass.Functions.NSLXNL import NSLXNL
from Models.Cores.Compass.Functions.UDM import UDM
from Models.Cores.Compass.Functions.GROUP import GROUP
from Models.Cores.Compass.Functions.COMMENTS import COMMENTS
from Models.Cores.Compass.Functions.GORGOL import GORGOL
from Models.Cores.Compass.Functions.PORPOL import PORPOL
from Libs.autoload import *

class EnginePC:
	def __init__(self, GUI):
		self.GUI= GUI
		self.path= GUI.path
		self.fdict= {}
		self.anp= -1 if int(GUI.forms["A - Np"]) == 0 else 1
		self.pognp= -1 if int(GUI.forms["Pog - Np"]) == 0 else 1
		self.gnmsp= -1 if int(GUI.forms["Gn MSP"]) == 0 else 1
		self.ldm= -1 if int(GUI.forms["LDM"]) == 0 else 1
		self.udm= -1 if int(GUI.forms["UDM"]) == 0 else 1
		self.denticao= GUI.denticao
		self.idade= GUI.idade
		self.__process__()
	def __process__(self):
		csv= Loader(self.GUI.path)
		self.csv= csv.forDict()
		self.fdict["NOME"]= self.csv["Name"]
		self.fdict["IDADE"]= self.idade
		self.fdict["Genero"]= self.csv["Gender"]
		self.fdict["DataExame"]= self.csv["DataScan"]

		hc= HC(self)
		cp= CP(self)
		xmsp= XMSP(self)
		vl= VL(self)
		anp= ANP(self)
		pognp= POGNP(self)
		ulh= UPPERLOWERHEIGHT(self)
		rightlfh= RIGHTLFH(self)
		leftlfh= LEFTLFH(self)
		cba= CBA(self)
		nbaptlgn= NBAPTLGN(self)
		nbaptrgn= NBAPTRGN(self)
		sppolgolme= SPPOLGOLME(self)
		sna= SNA(self)
		snb= SNB(self)
		condlra= CONDLRA(self)
		condlrgn= CONDLRGN(self)
		golrcamper= GOLRCAMPER(self)
		golrcp= GOLRCP(self)
		try:
			pholdway= PHOLDAWAY(self)
		except Exception:
			pass
		try:
			pogpholdway= POGPHOLDAWAY(self)
		except Exception:
			pass
		jlrcamper= JLRCAMPER(self)
		meflrcamper= MEFLRCAMPER(self)
		meflrmsp= MEFLRMSP(self)
		try:
			impa= IMPA(self)
		except Exception:
			pass
		try:
			na= NA(self)
		except Exception:
			pass
		meflrcp= MEFLRCP(self)
		carl= CARL(self)
		try:
			angulo21311141= ANGULO21311141(self)
		except Exception:
			pass
		corpuslr= CORPUSLR(self)
		capitularelrmsp= CAPITULARELRMSP(self)
		capitularelrpcp= CAPITULARELRPCP(self)
		capitularelrpfrank= CAPITULARELRPFRANK(self)
		golrgn= GOLRGN(self)
		try:
			espacoatm= ESPACOATM(self)
		except Exception:
			pass
		afasi= AFASI(self)
		condlrgolr= CONDLRGOLR(self)
		gnmsp= GNMSP(self)
		golrmsp= GOLRMSP(self)
		try:
			apog1121= APOG1121(self)
		except Exception:
			pass
		jlrmsp= JLRMSP(self)
		ldm= LDM(self)
		nslxml= NSLXML(self)
		nslxml= NSLXNL(self)
		udm= UDM(self)
		try:
			poef= POEF(self)
		except Exception:
			pass
		try:
			gorgol= GORGOL(self)
		except Exception:
			pass
		try:
			porpol= PORPOL(self)
		except Exception:
			pass
		try:
			aglr= AGLR(self)
		except Exception:
			pass
		group= GROUP(self)
		self.fdict["denticao"] = self.denticao
		self.fdict["response"] = {
			"HC": hc.response(),
			"CP1626": cp.response1626(),
			"CP3646": cp.response3646(),
			"XMSP131416": xmsp.response131416(),
			"XMSP3343": xmsp.response3343(),
			"XMSP3646": xmsp.response3646(),
			"VL": vl.response(),
			"ANP": anp.response(),
			"POGNP": pognp.response(),
			"ULH": ulh.response(),
			"RIGHTLFH": rightlfh.response(),
			"LEFTLFH": leftlfh.response(),
			"CBA": "",
			"NBAPTLGN": nbaptlgn.response(),
			"NBAPTRGN": nbaptrgn.response(),
			"SPPOLGOLME": sppolgolme.response(),
			"SNA": sna.response(),
			"SNB": snb.response(),
			"CONDLRA": condlra.response(),
			"CONDLRGN": condlrgn.response(),
			"GOLRCAMPER": golrcamper.response(),
			"GOLRCP": golrcp.response(),
			"JLRCAMPER": jlrcamper.response(),
			"MEFLRCAMPER": meflrcamper.response(),
			"MEFLRMSP": meflrmsp.response(),
			"MEFLRCP": meflrcp.response(),
			"CARL": carl.response(),
			"CAPITULARELRMSP": capitularelrmsp.response(),
			"CAPITULARELRPCP": capitularelrpcp.response(),
			"CAPITULARELRPFRANK": capitularelrpfrank.response(),
			"GOLRGN": golrgn.response(),
			"CONDLRGOLR": condlrgolr.response(),
			"GNMSP": gnmsp.response(),
			"GOLRMSP": golrmsp.response(),
			"JLRMSP": jlrmsp.response(),
			"LDM": ldm.response(),
			"NSLXML": "",
			"NSLXNL": "",
			"UDM": udm.response(),
			"ESPACOATM": espacoatm.responses()
		}
		comments= COMMENTS(self)
		self.__exports__()
	def __exports__(self):
		_export= open(os.getcwd() + "/Resources/Databases/PCtable.tbl","w")
		_export.write(json.dumps(self.fdict))
		_export.close()
