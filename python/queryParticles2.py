# queryParticles.py
#-----------------------------------------------------------
# Builds files containing the X,Y,Z information of particles
# from all particle shape nodes inside a Maya scene file
#-----------------------------------------------------------
# Chance Payne and Kyle Nikolich
# April 2009

import os
import maya.cmds as mc

# Get the position of the particles
def getPositions(currentTime, tnode, path):
	
	# Select Particles
	selection = tnode + "*"
	mc.select(selection)
	particleNames = mc.ls(sl=True, type="transform")

	# Get particle positions
	for part in particleNames:
		
		# Find number of particles within particle shape
		num = mc.particle(part, q=True, ct=True)
		
		# Write X Y Z values of each particle to file
		for n in range(num):
		
			pPath = path + "/particles/particleNum" + str(n) + ".mel"
			
			#Check to see if file exits, if not, create it
			#print ("Does the path exist? %s" % pPath)
			#print os.path.exists(pPath)
			if os.path.exists(pPath):
				filePart = open(pPath, 'a')
			else:
				filePart = open(pPath, 'w')
				
			partP = part + ".pt[%s]" % n
			pos = mc.getParticleAttr(partP, at='position')
		
			
			filePart.write("%s " % pos[0])
			filePart.write("%s " % pos[1])
			filePart.write("%s \n" % pos[2])
			
# Create files with particle information, master procedure
# This def utilizes getPositions to write files	
def buildFile(endFrame, tnode, path):	

	# Initialize the frame number to 1
	## BUG - frame reinitializes to 0 in the loop below
	## OFFSET frame value in getPositions by 1
	frame = 1
	# Step through every frame, get positions of particles
	for frame in range(endFrame):
		currentTime = mc.currentTime(frame, edit=True)
		currentTime = int(currentTime)
		#print ("this is teh time yo %s" % currentTime)
		#print (" tnode %s" % tnode)
		getPositions(currentTime, tnode, path)


#Call buildFile to bake particle data to text files
#buildFile(240, "particle", "/stuhome/vsfx705/particleData")

