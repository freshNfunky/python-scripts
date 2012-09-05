from pymel.all import *


class PanelWindow( object ):

#------------------------------------------------------------------------    
    gSampleState = []
        
    _wName = ''
    windowTitle = 'iMayaUi Window'
    panelLabel = 'SamplePanel'
    panelWrapName = 'frm'
#------------------------------------------------------------------------    
    def __init__( self, name, title, namespace=__name__ ):
        
        # print "self instanceName: %s " % self.__class__.__name__
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
                           createCallback='python("import %s ; %s._createCallback()")' %  (namespace, self.instance),
                           initCallback='python("import %s ; %s._initCallback()"  )' % (namespace, self.instance),
                           addCallback='python("import %s ; %s._addCallback()"   )' %  (namespace, self.instance),
                           removeCallback='python("import %s ; %s._removeCallback()")' % (namespace, self.instance),
                           deleteCallback='python("import %s ; %s._deleteCallback()")' % (namespace, self.instance),
                           saveStateCallback='python("import %s ; %s._saveCallback()")' % (namespace, self.instance)
                           )
        print "RESULT: %s " % result
#------------------------------------------------------------------------
    def _setup(self):
        """Command to be call for new scene"""
        print 'SETUP CALLED'
        gMainPane = mel.eval( 'global string $gMainPane; $temp = $gMainPane;' )
        sceneUIReplacement( update=gMainPane )
        panelName = sceneUIReplacement( getNextScriptedPanel=(self.__name__, self._title) )
        
        # print "-->Panel Name: %s" % panelName
        
        if panelName == '':
            try:
                panelName = scriptedPanel( mbv=1, unParent=True, type=self.__name__, label=self._title )
                scriptedPanel( panelName, e=True, parent=self.panelParent)
                print "sceneUIreplacement has found something"
            except:
                pass
        else:
            try:
                pLabel = panel( self.__name__, query=True, label=True )
                panelName = scriptedPanel( self.__name__, edit=True,  label=pLabel )
                scriptedPanel( panelName, e=True, parent=self.panelParent)
                print "sceneUIreplacement has FAILED finding something - however"
            except:
                pass

#------------------------------------------------------------------------
    def _createCallback(self):
        """Create any editors unparented here and do any other initialization required."""
        print 'CREATE CALLBACK'
        self.gSampleState = {'fsg1':0, 'fsg2':1, 'fsg3':3, 'rbg':1, 'rbg1':2}

#------------------------------------------------------------------------
    def _initCallback(self):
        """Re-initialize the panel on file -new or file -open."""
        print 'INIT CALLBACK'
        # needs to be filled out when more advanced with save, new, open etc.

#------------------------------------------------------------------------
    def _addCallback(self):
        """Create UI and parent any editors."""
        print 'ADD CALLBACK'
        #
        #  Description:  Create UI and parent any editors.
        #
        if not self.gSampleState.__len__() : 
            self._createCallback()
            print "---->gSampleState was Empty"
        #------------------------------- testmodule
        columnLayout('topCol',adj=True)
        separator(h=10,style="none")
        frameLayout(mw=10,l="Sliders")
        columnLayout('sampleCol',adj=True)
        separator(h=10,style="none")
        floatSliderGrp('fsg1',v=self.gSampleState['fsg1'],
            l="Property A",f=True)
        floatSliderGrp('fsg2',v=self.gSampleState['fsg2'],
            l="Property B",f=True)
        floatSliderGrp('fsg3',v=self.gSampleState['fsg3'],
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
        #------------------------------- testmodule
#------------------------------------------------------------------------
    def _removeCallback(self):
        """Unparent any editors and save state if required."""
        if not scriptedPanel(self.__name__, ex=1):
            return                                  # no common call 
        print 'REMOVE CALLBACK: %s' % self.__name__
        
        control=str(scriptedPanel(self.__name__,
                                  q=1,control=1))
        setParent(control)
        #------------------------------- testmodule
        self.gSampleState['fsg1']=float(floatSliderGrp('fsg1',q=1,v=1))
        self.gSampleState['fsg2']=float(floatSliderGrp('fsg2',q=1,v=1))
        self.gSampleState['fsg3']=float(floatSliderGrp('fsg3',q=1,v=1))
        self.gSampleState['rbg']=float(radioButtonGrp('rbg',q=1,sl=1))
        self.gSampleState['rbg1']=float(radioButtonGrp('rbg2',q=1,sl=1))
        #------------------------------- testmodule
#------------------------------------------------------------------------
    def _deleteCallback(self):
        """Delete any editors and do any other cleanup required."""
        print 'DELETE CALLBACK'

#------------------------------------------------------------------------
    def _saveCallback(self):
        """Save Callback."""
        print 'SAVE CALLBACK'
        indent="\n\t\t\t"
        reCreateCommand = 'python("print \\"RECREATE COMMAND %s\\" % '+ self.instance + ' ")' 
        print "prepared recreate Command: %s" % reCreateCommand
        return reCreateCommand
        
#------------------------------------------------------------------------
    def show( self ):
        #scriptedPanel( self._title, edit=True, tearOff=True )
        print "SHOW PANEL"
        # print "self?: %s" % self.__name__
        if not window(self._wName, exists=True ):          
            print "fenster existiert nicht"
            try: 
                wPanel = scriptedPanel(  self.__name__, unParent=True, type=self.__name__, label=self._title )
            except:
                pLabel = panel( self.__name__, query=True, label=True )
                wPanel = scriptedPanel( self.__name__, edit=True,  label=pLabel )
            
            self._wName = window( self._title, t=self.windowTitle )
        
            wFrame = frameLayout( self.panelWrapName, l=self.panelLabel ,lv=True, bv=True ) ## get external definitions
            # print "Frame Name %s" % wFrame
            #panelParent = (wName+'|'+wFrame)
            self.panelParent = wFrame
            scriptedPanel( wPanel, e=True, parent=self.panelParent)
            self.panelUIpath = scriptedPanel( self.__name__, q=True, control=True )
            
        showWindow(self._wName)

#------------------------------------------------------------------------


def openTestPanel():
    # global testPanel
    global PanelObj
    PanelObj = PanelWindow( 'PanelObj','Panel Obj Window' ) 
    PanelObj.show()
    return PanelObj