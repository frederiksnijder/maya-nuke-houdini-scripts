'''
Maya startup script.
'''

from os import environ
from subprocess import call
from sys import exit
import platform

# set drive/system by checking computer name and windows version
if (platform.node() == 'ws1') and (platform.release() == '10'):
	system = 'ws1'
elif (platform.node() == 'm-vfx-07') and (platform.release() == '7'):
	system = 'm-vfx-07'
else:
	exit('Platform not recognised')

# enable/disable Maya classic UI colors
standard_ui = True

# set machine depended drive
if system == 'ws1':
	drive = 'D'
elif system == 'm-vfx-07':
	drive = 'E'

###############################################################################################################
# set script variables
###############################################################################################################

# custom shaders
alshaders_dir = drive+':/cg/env/alShaders/alShaders-win-1.0.0rc11-ai4.2.2.0'
obqshaders_dir = drive+':/cg/env/obqShaders/Obq_Shaders__Build_2015-06-03'
jf_nested_dir = drive+':/cg/env/jf-nested-dielectric'
aaOcean_dir = drive+':/cg/env/aaOcean'

# fabric engine
fabric_dir = drive+':/cg/env/fabric_engine/FabricEngine-2.0.1-Windows-x86_64'

# set environment base dir
env_dir = drive+':/cg/env'

###############################################################################################################
# environment variables
###############################################################################################################


# arnold render
environ['ARNOLD_PLUGIN_PATH'] = (
	alshaders_dir+'/bin;' + 
	obqshaders_dir+'/bin/v304;' + 
	obqshaders_dir+'/maya/metadata;' +
	jf_nested_dir+'/binaries/v1.0.5/win64/arnold_4.1;' +
	aaOcean_dir+'/aaOceanRev345_latest_win/aaOcean/Arnold/Arnold-4.2.0.6-windows/Shader;' +
	aaOcean_dir+'/aaOceanRev345_latest_win/aaOcean/Arnold/Arnold-4.2.0.6-windows/MtoA;' +
	drive+':/cg/env/solidangle/oculusCamera;'
	)
environ['MTOA_TEMPLATES_PATH'] = (
	alshaders_dir+'/ae;' +
	obqshaders_dir+'/maya/ae;' +
	aaOcean_dir+'/aaOceanRev345_latest_win/aaOcean/Arnold/Arnold-4.2.0.6-windows/MtoA;' +
	drive+':/cg/env/solidangle/oculusCamera;'
	)
environ['MAYA_CUSTOM_TEMPLATE_PATH'] = (
	alshaders_dir+'/aexml;' + 
	obqshaders_dir+'/maya/ae;'
	)
# arnold render log
environ['MTOA_LOG_PATH'] = (
	drive+':/cg/temp/logs;'
	)
# arnold houdini mplay driver
environ['__HOUDINI_BINARY_FOLDER'] = (
	'C:/Program Files/Side Effects Software/Houdini 15.0.244.16/bin;'
	)

''' USE THESE LINES TO SET MTOA ENV ON DIFFERENT MACHINES/DRIVES
# load modules
mtoa_mod_path = drive+':/cg/env/solidangle/mtoa_mod_home;' if system == 'home' else drive+':/cg/env/solidangle/mtoa_mod_mv;'
environ['MAYA_MODULE_PATH'] = (
	fabric_dir+'/SpliceIntegrations/FabricSpliceMaya2015SP2;' + 
	mtoa_mod_path)
'''

# load modules
mtoa_mod_path = drive+':/cg/env/solidangle/2016.5;'
environ['MAYA_MODULE_PATH'] = (
	fabric_dir+'/SpliceIntegrations/FabricSpliceMaya2015SP2;' + 
	mtoa_mod_path
	)

# set render description
environ['MAYA_RENDER_DESC_PATH'] = (
	drive+':/cg/env/solidangle/2016.5;'
	)

# load maya plugins
environ['MAYA_PLUG_IN_PATH'] = (
	aaOcean_dir+'/aaOceanRev345_latest_win/aaOcean/Maya/Maya2015;' # aaOcean deformer not working in Maya 2016.5
	)

# maya preset path
environ['MAYA_PRESET_PATH'] = (
	env_dir+'/maya/presets;' +
	obqshaders_dir+'/maya;'
	)

# script path MEL
environ['MAYA_SCRIPT_PATH'] = (
	env_dir+'/maya/scripts;' +
	env_dir+'/maya/shelves;' +
	env_dir+'/maya/scripts/scriptManager;' +
	aaOcean_dir+'/aaOceanRev345_latest_win/aaOcean/Maya/Maya2015;'
	)

# script path Python
environ['PYTHONPATH'] = (
	env_dir+'/zync/zync-maya;' +
	env_dir+'/maya/scripts' # do NOT add semicolon
	)
# maya automatically appends all default folders and adds it's own semicolon

# custom shelves
environ['MAYA_SHELF_PATH'] = (
	env_dir+'/maya/shelves;'
	)

# custom icons
environ['XBMLANGPATH'] = (
	env_dir+'/maya/icons;' +
	env_dir+'/maya/icons/layouts;' +
	env_dir+'/maya/icons/modelling_icons;' +
	env_dir+'/maya/icons/other_icons;' +
	env_dir+'/zync/zync-maya;' +
	obqshaders_dir+'/maya/icons;'
	)


###############################################################################################################
# Run maya
###############################################################################################################

# path to maya executable
maya_exec = 'C:/Program Files/Autodesk/Maya2016.5/bin/maya.exe'

if standard_ui:
	call([maya_exec])
else:
	call([maya_exec, "-style", "windows"])
