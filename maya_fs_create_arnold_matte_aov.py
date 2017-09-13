from sys import exit
import maya.cmds as cmds
import mtoa.aovs as ma

# put all selected shaders in a list
sel = cmds.ls(sl=True)

# check if selection is not empty and if every node is a aiStandard shader
if len(sel) > 0:
	for i in sel:
		if cmds.nodeType(i) != "aiStandard":
			exit("Not every node in the selection is an aiStandard")
		else:
			print cmds.nodeType(i)
else:
	print "Your selection is empty"

surfaceShaderName = "_mSHDR_matte_aiUtil"

# check if aiUtility node with name _mSHDR_matte_aiUtil exists
aiUtilCheck = cmds.objExists(surfaceShaderName)
# if not create aiUtility node and set shading to flat
if aiUtilCheck == 0:
	aiUtil = cmds.createNode("aiUtility", name=surfaceShaderName)
	cmds.setAttr(aiUtil + ".shadeMode", 2)
	cmds.setAttr(aiUtil + ".color", 1,0,0, type="double3")


# create AOV and connect the aiUtility to the shading group
for i in sel:
	# create the AOV name
	aov_name = "m_" + i;

	# create the AOV node
	ctc = ma.AOVInterface()
	ctc.addAOV(aov_name)

	# set the AOVs Data Type to RGB
	cmds.setAttr("aiAOV_" + aov_name + ".type", 5)

	# get name of the shadingGroup
	shadingGroup_name = cmds.listConnections(i, type="shadingEngine")
	print shadingGroup_name

	# get AOV element number of AOV attribute child
	customAOVarray = cmds.listAttr((shadingGroup_name[0] + ".aiCustomAOVs"), multi=True,)
	# find index ID of in customAOVarray
	customAOVarrayIndex = customAOVarray.index("ai_aov_" + aov_name)
	customAOVarrayIndex = str(customAOVarrayIndex /3)
	print customAOVarrayIndex

	# connect the aiUtility to the AOV attribute of the shading engine]
	attr1 = surfaceShaderName + ".outColor"
	attr2 = shadingGroup_name[0] + ".aiCustomAOVs[" + customAOVarrayIndex + "].aovInput"
	cmds.connectAttr(attr1, attr2 , force=True)
