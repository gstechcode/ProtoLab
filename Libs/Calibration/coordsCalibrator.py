from Libs.Calibration.components.treeview import *
from Libs.Calibration.components.GraphInterface import *
import json, os

class coordsCalibrator:
    def __init__(self) -> None:
        self.basicConfiguration()
        self.display= GraphInterface(title="CompassX - Calibrador de Coordenada",geometry="500x500", bg="orange").run()
        self.treeview= treeview(self.display, ["Coordenada","Valor"], self.content, updateCoord= self.updateCoord)
        self.lastConfiguration()
        self.updateFileDB()
        self.display.mainloop()
     
    def updateCoord(self, itemSelected: str, newCoord: tuple) -> None:
        self.editFileDB(itemSelected,newCoord)
        self.updateFileDB()
        
    def editFileDB(self, indice, valor) -> None:
        FileDB= open(self.PATHDB,"r")
        FileDBtoJSON= json.loads(FileDB.readlines()[0])
        FileDB.close()
        FileDBtoJSON[indice]= valor
        FileDB= open(self.PATHDB,"w")
        FileDB.write(json.dumps(FileDBtoJSON))
        FileDB.close()
        
    def updateFileDB(self) -> None:
        self.treeviewInstance.delete(*self.treeviewInstance.get_children())
        fileDB= open(self.PATHDB,"r")
        FileDBtoJSON= json.loads(fileDB.readlines()[0])
        fileDB.close()
        for i in FileDBtoJSON:
            self.treeviewInstance.insert("",END,values= [i,FileDBtoJSON[i]])
        self.treeviewInstance.update()
            
    def lastConfiguration(self) -> None:
        self.treeviewInstance= self.treeview.getTreeview()
        
    def basicConfiguration(self) -> None:
        self.PATHDB= os.getcwd() + "/Resources/Databases/CompassX.coords"
        modelCoords= {"QUAD": (0,0),"QUADFULL": (0,0)}
        self.content= []
        
        if(not(self.DBExist())):
            fileDB= open(self.PATHDB,"w")
            fileDB.write(json.dumps(modelCoords))
            fileDB.close()
            self.content= [["QUAD",(0,0),["QUADFULL",(0,0)]]]
        else:
            fileDB= open(self.PATHDB,"r")
            FileDBtoJSON= json.loads(fileDB.readlines()[0])
            fileDB.close()
            for i in FileDBtoJSON:
                self.content.append([i,FileDBtoJSON[i]])
        
    def DBExist(self) -> bool:
        if(os.path.exists(self.PATHDB)):
            return True
        else:
            return False