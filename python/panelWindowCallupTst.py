# import TestObj.py as *
import pymel  # touch pat.py in the cwd and try to import the empty file under Linux
import string 
import os,sys


if not os.getcwd() in sys.path:
    sys.path.append(os.getcwd())

import panelWindow    
# from panelWindow import *
reload(panelWindow)
Obj = panelWindow.openTestPanel()
# print Obj