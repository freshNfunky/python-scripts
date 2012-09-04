from pymel.all import *


class PanelWindow( object ):
    
    gSampleState=[]
    
    def __init__( self, name, title, namespace=__name__ ):
        
        print "self instanceName: %s " % self
        self.__name__ = name
        self._title = title

        self.instance = str(namespace) + '.' + self.__name__
        
        if not scriptedPanelType( self.__name__, query=True, exists=True ):
            scriptedPanelType( self.__name__, unique=True )
        print self.instance 
        jobCmd = 'python(\\\"%s._setup()\\\")' % self.instance
        job = "scriptJob -replacePrevious -parent \"%s\" -event \"SceneOpened\" \"%s\";" % ( self.__name__, jobCmd )
        mel.eval(job)

        result = scriptedPanelType( self.__name__, edit=True,
                           unique=True,
                           createCallback='python("import %s ; print \\"callback: %s._createCallback()\\" ; %s._createCallback()")' % (namespace, self.instance, self.instance),
                           initCallback='python("import %s ; %s._initCallback()"  )' % (namespace, self),
                           addCallback='python("import %s ; print \\"callback: %s._createCallback()\\" ; %s._addCallback()"   )' % (namespace, self.instance, self.instance),
                           removeCallback='python("import %s ; %s._removeCallback()")' % (namespace, self.instance),
                           deleteCallback='python("import %s ; %s._deleteCallback()")' % (namespace, self.instance),
                           saveStateCallback='python("import %s ; %s._deleteCallback()")' % (namespace, self.instance)
                           )
        print "RESULT: %s " % result

    def _setup(self):
        """Command to be call for new scene"""
        print 'SETUP CALLED'
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
        print 'CREATE CALLBACK'


    def _initCallback(self):
        """Re-initialize the panel on file -new or file -open."""
        print 'INIT CALLBACK'


    def _addCallback(self):
        """Create UI and parent any editors."""
        print 'ADD CALLBACK'
        #
        #  Description:  Create UI and parent any editors.
        #
        columnLayout('topCol',adj=True)
        separator(h=10,style="none")
        frameLayout(mw=10,l="Sliders")
        columnLayout('sampleCol',adj=True)
        separator(h=10,style="none")
        floatSliderGrp('fsg1',v=gSampleState[0],
            l="Property A",f=True)
        floatSliderGrp('fsg2',v=gSampleState[1],
            l="Property B",f=True)
        floatSliderGrp('fsg3',v=gSampleState[2],
            l="Property C",f=True)
        separator(h=10,style="none")
        setParent('..')
        setParent('..')
        separator(h=10,style="none")
        frameLayout(mw=10,l="Radio Buttons")
        columnLayout('sampleCol2')
        separator(h=10,style="none")
        radioButtonGrp('rbg',nrb=3,
            l="Big Options",
            select=gSampleState[3],
            la3=("Option 1", "Option 2", "Option 3"))
        radioButtonGrp('rbg2',nrb=3,
            l="Little Options",
            select=gSampleState[4],
            la3=("Option 4", "Option 5", "Option 6"))
        separator(h=10,style="none")


    def _removeCallback(self):
        """Unparent any editors and save state if required."""
        print 'REMOVE CALLBACK'
        control=str(scriptedPanel(panelName,
                                  q=1,control=1))
        setParent(control)
        gSampleState[0]=float(floatSliderGrp('fsg1',q=1,v=1))
        gSampleState[1]=float(floatSliderGrp('fsg2',q=1,v=1))
        gSampleState[2]=float(floatSliderGrp('fsg3',q=1,v=1))
        gSampleState[3]=float(radioButtonGrp('rbg',q=1,sl=1))
        gSampleState[4]=float(radioButtonGrp('rbg2',q=1,sl=1))


    def _deleteCallback(self):
        """Delete any editors and do any other cleanup required."""
        print 'DELETE CALLBACK'


    def _saveCallback(self):
        """Save Callback."""
        print 'SAVE CALLBACK'
        indent="\n\t\t\t"
        reCreateCommand = str(indent) + "$gSampleState[0]=" + str(melGlobals['gSampleState'][0]) + ";" + str(indent) + "$gSampleState[1]=" + str(melGlobals['gSampleState'][1]) + ";" + str(indent) + "$gSampleState[2]=" + str(melGlobals['gSampleState'][2]) + ";" + str(indent) + "$gSampleState[3]=" + str(melGlobals['gSampleState'][3]) + ";" + str(indent) + "$gSampleState[4]=" + str(melGlobals['gSampleState'][4]) + ";" + str(indent) + "setSamplePanelState $panelName;\n"
        return reCreateCommand
        

    def show( self ):
        #scriptedPanel( self._title, edit=True, tearOff=True )
        mel.tearOffPanel( self._title, self.__name__, 1 )


def openTestPanel():
    global testPanel 
    testPanel = PanelWindow( 'testPanel','testPanelObj' )
    testPanel.show()
    return testPanel