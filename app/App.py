# -------- App.py --------
# Handles all general application logic
# ------------------------

# General imports
import json

# Panda3d imports
from direct.showbase.ShowBase import ShowBase

# App imports


# -------- App --------
class App( ShowBase ):

    # Init
    # 
    # @param object Self
    # @return void
    def __init__( self ):
        ShowBase.__init__( self )

        self.loadGame( 'examples/standard.json' )

    def loadGame( self, filename ):
        f = open( 'data/' + filename, 'r' )
        data = json.load( f )

        print data