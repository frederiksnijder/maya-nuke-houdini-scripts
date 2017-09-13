import maya.cmds as mc


# first hand select all aiSkyDomeLights
mc.pickWalk( d="down" )
sel = mc.ls(sl=True, fl=True)
file_nodes = []


# print the number of selected aiSkyDomeLights
print str(len(sel)) + ' node(s) selected'


# check if selected nodes are aiSkydomeLights
def testNodeType(selection, node):
	testFailed = []
	for i in selection:
		if mc.nodeType( i ) != node:
			testFailed.append( i )
	if len(testFailed) > 0:
		print testFailed, 
		print "__SCRIPT FAILED__"
		return "failed"

testNodeType_return = testNodeType(sel, "aiSkyDomeLight")



# loop over selection and check which nodes are connected to the color attribute
# put those nodes in the list file_nodes
def connected2color(selection):
	nodesConnectedList = []
	for i in selection:
		connected_nodes = mc.listConnections( i+'.color' )
		nodesConnectedList.append(connected_nodes)
	return nodesConnectedList


# if the selection is of the correct type
# check which nodes are connected to the selection
if testNodeType_return != "failed":
	file_nodes = connected2color(sel)

def modifyPath(insert1, insert2):
	for i in file_nodes:
		# get old path from file node
		old_path = mc.getAttr(i[0]+".fileTextureName")
	
		# get starting index for last slash and edit path
		index_last_slash = len(old_path) - old_path[::-1].index("/")
		new_path = old_path[:index_last_slash] + insert1 + old_path[index_last_slash:]
	
		# get starting index for last dot and edit path
		index_last_dot = new_path.index(".")
		new_path = new_path[:index_last_dot] + insert2 + new_path[index_last_dot:]

		# print new path and assign to filetextureName
		print new_path
		cmds.setAttr(i[0] + ".fileTextureName", new_path, type="string")

modifyPath('lowres/', '_lowres')