from pymel.all import *

class PanelWindow( object ):
    
    def __init__( self, name, title, namespace=__name__ ):
        self.__name__ = name
        self._title = title

        self.instance = str(namespace) + '.' + self.__name__

        if not scriptedPanelType( self.__name__, query=True, exists=True ):
            scriptedPanelType( self.__name__, unique=True )

        jobCmd = 'python(\\\"%s._setup()\\\")' % self.instance
        job = "scriptJob -replacePrevious -parent \"%s\" -event \"SceneOpened\" \"%s\";" % ( self.__name__, jobCmd )
        mel.eval(job)

        scriptedPanelType( self.__name__, edit=True,
                           unique=True,
                           createCallback='python("%s._createCallback()")' % self.instance,
                           initCallback='python("%s._initCallback()"  )' % self.instance,
                           addCallback='python("%s._addCallback()"   )' % self.instance,
                           removeCallback='python("%s._removeCallback()")' % self.instance,
                           deleteCallback='python("%s._deleteCallback()")' % self.instance,
                           saveStateCallback='python("%s._deleteCallback()")' % self.instance
                           )


    def _setup(self):
        """Command to be call for new scene"""

        panelName = sceneUIReplacement( getNextScriptedPanel=(self.__name__, self._title) )

        if panelName == '':
            try:
                panelName = scriptedPanel( mbv=1, unParent=True, type=self.__name__, label=self._title )
            except:
                pass
        else:
            try:
                label = panel( self.__name__, query=True, label=True )
                scriptedPanel( self.__name__, edit=True,  label=self._title )
            except:
                pass


    def _createCallback(self):
        """Create any editors unparented here and do any other initialization required."""
        #print 'CREATE CALLBACK'


    def _initCallback(self):
        """Re-initialize the panel on file -new or file -open."""
        #print 'INIT CALLBACK'


    def _addCallback(self):
        """Create UI and parent any editors."""
        #print 'ADD CALLBACK'


    def _removeCallback(self):
        """Unparent any editors and save state if required."""
        #print 'REMOVE CALLBACK'


    def _deleteCallback(self):
        """Delete any editors and do any other cleanup required."""
        #print 'DELETE CALLBACK'


    def _saveCallback(self):
        """Save Callback."""
        #print 'SAVE CALLBACK'
        reCreateCommand = ''
        return reCreateCommand


    def show( self ):
        #scriptedPanel( self._title, edit=True, tearOff=True )
        mel.tearOffPanel( self._title, self.__name__, 1 )


def openTestPanel():
    global testPanel
    testPanel = PanelWindow( 'testPanel' )
    testPanel.show()