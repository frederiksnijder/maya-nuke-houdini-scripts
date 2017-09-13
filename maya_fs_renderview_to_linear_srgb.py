"""
Set Render View Image Color Profile to Linear sRGB

"""

import maya.cmds as cmds

# check if window exists
try:
	if mc.window(imageColorProfile, ex=True):
		mc.deleteUI(imageColorProfile, window=True)
except NameError:
	pass

# creates UI window
imageColorProfile = cmds.window(title='Render View Image Color Profile', s=False, wh=(300,50))

# creates window attributes
cmds.columnLayout(adj=True)
cmds.text(l='Set the "Render View" "Image Color Profile" to linear')
cmds.button(l='Set to linear', w=300, h=50, c='set_to_linear()' )
# draws the window
cmds.showWindow(imageColorProfile)

# defines the function mc.button has to call
def set_to_linear():
	cmds.setAttr('defaultViewColorManager.imageColorProfile', 2)
	if cmds.getAttr('defaultViewColorManager.imageColorProfile') == 2:
		print("Render View' 'Image Color Profile' set to 'Linear sRGB'"),
# use a comma after the functioncall to print the output to the commandline
