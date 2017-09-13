import maya.cmds as cmds

sel = cmds.ls( selection=True )
x = cmds.getAttr(sel[0]+'.outSizeX')
y = cmds.getAttr(sel[0]+'.outSizeY')
print "x: " + str(x) + " y: " + str(y),