from Libs.autoload import *
from Libs.variables import *
from Libs.Tests.Test import Test
from Libs.Calibration.Calibration import Calibration
from Views import PCView
        
class Lab:
    def __init__(self):
        gui= PCView.Execute()
        calibracao= Calibration()
        EnginePC(gui)
        x= pcc3d()
        
Lab()