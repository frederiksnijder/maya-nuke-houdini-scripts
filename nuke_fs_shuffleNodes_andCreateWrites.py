import nuke
from os.path import exists
from os import makedirs


# function to find the base-path for the write nodes
def basePath():
    # first find the root directory path of the comp script
    basePath = (nuke.root()['name'].value())[0:(nuke.root()['name'].value()).rfind('/')+1]

    tempDir = 'shuffleTemp'
    # create tempDir if it doesn't exists
    if not exists(basePath + tempDir):
        makedirs(basePath + tempDir)

    return basePath + tempDir

# function to shuffle out all passes
def shufflePasses():
    node = nuke.selectedNode()
    channels = node.channels()
    layers = list( set([c.split('.')[0] for c in channels]) )
    layers.sort()

    for lay in layers:
        shuffleNode = nuke.nodes.Shuffle( name=lay, inputs=[node] )
        shuffleNode['in'].setValue( lay )
        shuffleNode['postage_stamp'].setValue( True )

shufflePasses()

# function to connect write nodes
def connectWrites():
    # set filname variables
    filePrefix = 'temp_'
    fileSuffix = '_####'
    fileExt = '.exr'
    # put selection in var
    node = nuke.selectedNodes()
    # loop over selection
    for i in node:
        # get name of node
        i_name = i['name'].getValue()
        # create new write node
        writeNode = nuke.nodes.Write( name=i_name, inputs=[i] )
        # set value for file path
        writeNode['file'].setValue ( basePath() + '/' + filePrefix + i_name + fileSuffix + fileExt)
        # display postage stamp
        writeNode['postage_stamp'].setValue( True )

connectWrites()
