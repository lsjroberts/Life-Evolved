# -------- Organ.py --------
# Generic organ component.
# 
# An organ performs a function.
# --------

# General imports

# Panda3D imports

# Game imports
from life.organism.component.Component import Component

# -------- Organ --------
class Organ( Component ):
    enabled = True
    
    # Init
    # @param self
    # @return void
    def __init__( self ):
        pass

    def enable( self ):
        self.enabled = True

    def disable( self ):
        self.enabled = False

    def isEnabled( self ):
        return self.enabled;

    def enact( self ):
        if ( self.isEnabled ):
            return self.action( )
        else:
            return False