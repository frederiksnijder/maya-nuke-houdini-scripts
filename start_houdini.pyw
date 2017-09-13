'''
Execute Houdini with a custom environment

;& > expands to the default path
;@ > Typically expands to the directories on the HOUDINI_PATH
/path/to/folder;& > search custom path first; then search the default paths

'''

from os import environ
from os import pathsep
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

# set machine depended drive
if system == 'ws1':
	drive = 'D'
elif system == 'm-vfx-07':
	drive = 'E'

###############################################################################################################
# set script variables
###############################################################################################################

# set environment base dir
env_dir = drive+':/cg/env'

###############################################################################################################
# environment variables
###############################################################################################################


# htoa variables
environ['PATH'] += (
	env_dir+'/solidangle/htoa-1.11.1_r1692_houdini-15.0.416/scripts/bin;')

environ['HOUDINI_PATH'] = (
	env_dir+'/solidangle/htoa-1.11.1_r1692_houdini-15.0.416;&')


# custom OTL folder
environ['HOUDINI_OTLSCAN_PATH'] = (
 	'@/otls;' +
	env_dir+'/houdini/otls;')


# custom script path
environ['HOUDINI_SCRIPT_PATH'] = (
	'@/scripts;' + 
	env_dir+'/houdini/scripts;')


# custom desktop folder
environ['HOUDINI_DESK_PATH'] = (
	# '@/desktop;' +
	env_dir+'/houdini/desktops;')


# custom UI scale > 85 is smaller UI, 105 is bigger UI
environ['HOUDINI_UISCALE'] = (
 	'100')


# redshift vars
environ['HOUDINI_DSO_ERROR'] = (
 	'2')

environ['PATH'] += (
	'C:/ProgramData/Redshift/bin;')

environ['HOUDINI_PATH'] = (
	'C:/ProgramData/Redshift/Plugins/Houdini/15.5.565;&')

# custom Houdini temp dir
environ['HOUDINI_TEMP_DIR'] = (
	drive+':/_temp/houdini_temp_dir;')


###############################################################################################################
# Other usefull variables
###############################################################################################################

'''
HOUDINI_MULTITHREADED_COOKING
HOUDINI_VEX_PATH
HOUDINI_TOOLBAR_PATH
HOUDINI_TEXTURE_PATH
HOUDINI_MACRO_PATH
HOUDINI_GEOMETRY_PATH
HOUDINI_CUSTOM_PATH
'''

###############################################################################################################
# Run Houdini
###############################################################################################################

# path to houdini executable
houdini_exec = 'C:\\Program Files\\Side Effects Software\\Houdini 15.5.746\\bin\\houdinifx.exe'

call([houdini_exec])


