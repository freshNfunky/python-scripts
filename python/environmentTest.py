# import TestObj.py as *
import pymel  # touch pat.py in the cwd and try to import the empty file under Linux
import string 
import os,sys
try:
    from TestObj import *
except:
    sys.path.append(os.getcwd())
    from TestObj import *


################## os.getcwd()##############
"""def get_path():
    PAT=str(pymel).split()[3][1:-9] # PATH extracted..
    sig=None
    try:
     sig=os.remove(PAT + 'pat.pyc')# get_rid...
    except OSError:
     PAT=PAT +'/'
     sig=os.remove(PAT + 'pat.pyc')# Fix for mutiple calls..  
    return PAT
"""
        
def runTest():
    global runObj
    runObj = TestObj('Name1', 'Name2')
    
runTest()
print os.environ['PYTHONPATH']
LOCATE=str(pymel).split()
print LOCATE # 
print os.getcwd()+ '/' #
print sys.path
print sys.argv[0]