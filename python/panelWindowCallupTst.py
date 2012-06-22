# import TestObj.py as *
import pymel  # touch pat.py in the cwd and try to import the empty file under Linux
import string 
import os,sys
try:
    from panelWindow import *
except:
    sys.path.append(os.getcwd())
    from panelWindow import *

openTestPanel()