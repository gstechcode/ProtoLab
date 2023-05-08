import platform, os
from tkinter import Tk


SO= platform.system()
root = Tk()
DISPLAY= (root.winfo_screenwidth(),root.winfo_screenheight())
root.destroy()
PROCESSORS= os.cpu_count()
ARCHITECTURE= platform.machine()