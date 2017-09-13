import maya.cmds as cmds

# create a list of all shadingEngines
sel = cmds.ls(type='shadingEngine')

# default Maya shading engines
defSG = ['initialShadingGroup','initialParticleSE']

# if any or all of the shading engines are part of the selection list
if any(i in sel for i in defSG) or all(i in sel for i in defSG):
    # get the index positions of the default shading engines and delete them from the selection list 
    del sel[sel.index('initialShadingGroup')]
    del sel[sel.index('initialParticleSE')]
    
sg_suffix = '_SG'

# loop over the shading engines
for SG in sel:
    # list all connections to the .surfaceShader attribute
    connectedNode = cmds.listConnections(SG + '.surfaceShader')
    
    # in case there are no connections
    if connectedNode == None:
        # check if all the shading engines connections are None
        attribute = [SG+'.surfaceShader', SG+'.volumeShader', SG+'.displacementShader']
        # keep track if the SG should be deleted
        deleteFlag = False
        # for each attribute check if there are any connections
        for attr in attribute:        
            # if something is connected and the deleteFlag is not already set
            if (cmds.listConnections(attr) != None) and (deleteFlag == False):
                deleteFlag = False
            # if something is connected the the flag to false
            elif (cmds.listConnections(attr) != None):
                deleteFlag = False
            else:
                deleteFlag = True
        # delete node
        if deleteFlag == True:
            cmds.delete(SG)

    # if the .surfaceShader attribute has a connection rename the shading engine
    else:
        cmds.rename(SG, connectedNode[0] + sg_suffix)