from pymel import *
from scriptedPanel import PanelWindow

class CustomPanel( PanelWindow ):

    def __init__( self, name, title ):
        PanelWindow.__init__( self, name, title, __name__ )


#object should match panel name
myCustomPanel = CustomPanel( name='myCustomPanel', title='My Custom Panel' )

def openMyCustomPanel():
    myCustomPanel.show()