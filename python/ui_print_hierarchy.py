# script created by pymel.tools.mel2py from mel file:
# \\powervault\users$\fschaller\eigene_dateien\docs\ui_print_hierarchy2.mel

from pymel.all import *
def findWindowLayout(windowUI):
	controls=lsUI(l=1)
	# Brute force: Get a list of all control layouts, and see which
	# is a child of the specified window.
	#
	# Create a wildcard pattern used by the "gmatch" command.
	#lsUI -l -controlLayouts
	pattern=windowUI + "*"
	# Default empty string to denote that no matching layout was found.
	#
	layout=""
	for ui in controls:
		if mel.gmatch(ui, pattern):
			tokens=[]
			# Compare the wildcard pattern against the name of this control.
			#
			# Found it!
			#
			numTokens=int(tokens=ui.split("|"))
			if numTokens>1:
				layout=tokens[0] + "|" + tokens[1]
				# This returns a path to the control, specifying the window as the parent.
				# It's advisable to always reference UI controls by their full path.
				#
				break
				
			
		
	return layout
	

def _printLayoutHierarchy(layout,parent,tab):
	bars="| | | | | | | | | | | | | | | | | | | | | | | | | | | "
	# Note: You _must_ specify the full path for a control in order to
	#       avoid ambiguous queries (and in this case, an infinite loop).
	#
	path=(parent + "|" + layout)
	# Print a pseudo-tree representation.
	#
	if tab>1:
		print bars[0:(tab - 1) * 2]
		
	if layout(path,
		q=1,exists=1):
		if tab>0:
			print "+ "
			
		print layout + "\n"
		# Query the children of this layout.
		#
		ca=layout(path,
			q=1,ca=1)
		# And recurse...
		#
		for c in ca:
			mel.printLayoutHierarchy(c, path, tab + 1)
			
		
	
	else:
		print "- "
		print layout + "\n"
		
	

windowUI="scriptEditorPanel1Window"
# Find the path of the layout control for Maya's main window.
#
path=str(findWindowLayout(windowUI))
# Split this into its path and layout name (short form).
#
layout=str(mel.match("[^|]*$", path))
parent=path.replace("|[^|]*$","")
print "layout is:" + layout + "\n"
print "parent is:" + parent + "\n"
# Build a hierarchical tree for this layout.
#
_printLayoutHierarchy(layout, parent, 0)
