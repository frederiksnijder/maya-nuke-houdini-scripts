import maya.cmds as cmds
from sys import exit

# start counting from this value
count = 1

# set multimatte prefix
prefix = "m"

# create list from current selection
sel = cmds.ls( selection=True )

# check if selection contains only nodes of the type VRayMtl 
for i in sel:
    if cmds.nodeType(i) != "VRayMtl":
        sys.exit("Not every node in your selection is of the type 'VRayMtl'")

for i in sel:
    # create list of connected shadingGroups
    s_grp = cmds.listConnections( i, type="shadingEngine")
 
    # create name for the Multi Matte
    multi_matte_name = prefix + str(count) + "_" + i
    
    # add attributes to shadingGroup
    cmds.vray("addAttributesFromGroup", s_grp[0], "vray_material_id", 1)
    # set Multimatte ID to count
    cmds.setAttr( s_grp[0] + ".vrayMaterialId", count)
    
    # create new Multimatte render element and rename to multimatte name
    renderElement = mel.eval('vrayAddRenderElement MultiMatteElement;')
    renderElement = cmds.rename(renderElement, multi_matte_name)
    
    # set Render Element filename suffix
    cmds.setAttr(renderElement + ".vray_name_multimatte", multi_matte_name, type="string")
    cmds.setAttr(multi_matte_name + ".vray_redid_multimatte", count)
    cmds.setAttr(multi_matte_name + ".vray_usematid_multimatte", count)
    
    # update the count variable
    count += 1