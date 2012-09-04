from pymel.all import *


class PanelWindow( object ):
    
    gSampleState=[]
    
    def __init__( self, name, title, namespace=__name__ ):
        
        print "self instanceName: %s " % self.__class__.__name__
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
                           createCallback='python("%s._createCallback(\\"%s\\")")' %  (self.instance, self.__name__),
                           initCallback='python("%s._initCallback(\\"%s\\")"  )' % (self.instance, self.__name__),
                           addCallback='python("%s._addCallback(\\"%s\\")"   )' %  (self.instance, self.__name__),
                           removeCallback='python("%s._removeCallback(\\"%s\\")")' % (self.instance,self.__name__),
                           deleteCallback='python("%s._deleteCallback(\\"%s\\")")' % (self.instance, self.__name__),
                           saveStateCallback='python("%s._deleteCallback(\\"%s\\")")' % (self.instance, self.__name__)
                           )
        print "RESULT: %s " % result

    def _setup(self, panelName):
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


    def _createCallback(self, panelName):
        """Create any editors unparented here and do any other initialization required."""
        print 'CREATE CALLBACK'
        self.gSampleState.append({'fsg1':0})
        self.gSampleState.append({'fsg2':1})
        self.gSampleState.append({'fsg3':3})
        self.gSampleState.append({'rbg':1})
        self.gSampleState.append({'rbg1':2})


    def _initCallback(self, panelName):
        """Re-initialize the panel on file -new or file -open."""
        print 'INIT CALLBACK'


    def _addCallback(self, panelName):
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
        floatSliderGrp('fsg1',v=self.gSampleState['fsg1'],
            l="Property A",f=True)
        floatSliderGrp('fsg2',v=self.gSampleState['fsg2'],
            l="Property B",f=True)
        floatSliderGrp('fsg3',v=self.gSampleState['fsg3']],
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
            select=self.gSampleState['rbg'],
            la3=("Option 1", "Option 2", "Option 3"))
        radioButtonGrp('rbg2',nrb=3,
            l="Little Options",
            select=self.gSampleState['rbg'],
            la3=("Option 4", "Option 5", "Option 6"))
        separator(h=10,style="none")


    def _removeCallback(self, panelName):
        """Unparent any editors and save state if required."""
        print 'REMOVE CALLBACK'
        control=str(scriptedPanel(panelName,
                                  q=1,control=1))
        setParent(control)
        self.gSampleState[0]=float(floatSliderGrp('fsg1',q=1,v=1))
        self.gSampleState[1]=float(floatSliderGrp('fsg2',q=1,v=1))
        self.gSampleState[2]=float(floatSliderGrp('fsg3',q=1,v=1))
        self.gSampleState[3]=float(radioButtonGrp('rbg',q=1,sl=1))
        self.gSampleState[4]=float(radioButtonGrp('rbg2',q=1,sl=1))


    def _deleteCallback(self, panelName):
        """Delete any editors and do any other cleanup required."""
        print 'DELETE CALLBACK'


    def _saveCallback(self, panelName):
        """Save Callback."""
        print 'SAVE CALLBACK'
        indent="\n\t\t\t"
        reCreateCommand = 'print "RECREATE COMMAND %s" % '+ self.instance 
        return reCreateCommand
        

    def show( self ):
        #scriptedPanel( self._title, edit=True, tearOff=True )
        mel.tearOffPanel( self._title, self.__name__, 1 )


def openTestPanel():
    global testPanel 
    testPanel = PanelWindow( 'testPanel','testPanelObj' )
    testPanel.show()
    return testPanel