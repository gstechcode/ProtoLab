from Libs.autoload import *
from Libs.variables import *
from Libs.Tests.Test import Test
        
class Lab:
    def __init__(self):
        print(DISPLAY)
        gui= Test()
        EnginePC(gui)
        x= pcc3d("Teste.pdf")
            
Lab()