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
Obj.createSliderObj() 
Obj.createRadioBtnObj()
print Obj.createSliderObj() 
print Obj.createTextfieldObj("this is a Test:\n aslkdj laksdj\n alksdj aslkdj \n aslkdjlkj asdkl sdakl sadlksdkjl\n sadlkjasd\n\n ljksda lkjsd jlksd kjlsda\n lkjsdajk lsda jklsdajqürewqew oiwqe i qwiuopqw qw iuopqw uioqwe uioqwe uiop")
print Obj.createVariableObj("test01")
print Obj.createVariableObj("Variable01")
print Obj.createVariableObj("SpereShape")
# print Obj