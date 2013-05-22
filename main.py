# ------------------------ Evolution ------------------------
# @author Gelatin Design, Laurence Roberts
# @datestart 17th May 2013
# 
# @version Pre-Alpha 0.0.0
# -----------------------------------------------------------


# ------------------------ Imports ------------------------

# Logging
import logging
import logging.config
logging.config.fileConfig( 'config/logging.conf' )
logger = logging.getLogger( 'root' )

# Panda3d imports
from panda3d.core import loadPrcFile

# Import app logic
from app.App import App
from app.Camera import CameraHandler


# ------------------------ Panda3D Config ------------------------

loadPrcFile("./config/config.prc")


# ------------------------ Main ------------------------

# Create app instance
app = App( )

# Create the camera
camera = CameraHandler( )

# Set background colour
base.setBackgroundColor( 0, 0, 0 )

# Set the app to run
app.run( )