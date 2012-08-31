# import TestObj.py as *
import pymel  # touch pat.py in the cwd and try to import the empty file under Linux
import string 
import os,sys

if not os.getcwd() in sys.path:
    sys.path.append(os.getcwd())
import panelWindow as pw

reload (pw)
pw.openTestPanel()