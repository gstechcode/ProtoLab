from Libs.autoload import *
from Libs.variables import *
from Libs.Tests.Test import Test
from Views import PCView
import sys, os, json
from tkinter import messagebox
        
        
class Lab:
    def __init__(self):
        gui= PCView.Execute()
        try:
            EnginePC(gui)
        except AttributeError:
            sys.exit()   
        x= pcc3d()
        
Lab()