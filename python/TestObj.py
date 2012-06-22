from pymel import *

class TestObj( object ):
    
    def __init__( self, name, title, namespace=__name__ ):
        self.__name__ = name
        self._title = title
        print "namespace: %s " % namespace
        print "self.__name__: %s " % self.__name__
        print "name: %s " % name
        print "title: %s" % title
        
"""def runTest():
    global runObj
    runObj = TestObj('Name1', 'Name2')
    
runTest()"""