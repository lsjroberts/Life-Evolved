# -------- JointAxes.py --------
# Trait < Appendage < Limb
# --------

# General imports

# Panda3D imports

# Game imports
from life.organism.trait.appendage.Appendage import Appendage

# -------- JointAxes --------
class JointAxes( Trait ):
    mutationRate = 0.01
    
    # Init
    # @param self
    # @return void
    def __init__( self, axes ):
        self.axes = axes

    def mutations( self ):
        def changeX( self ):
            self.axes.x = not self.axes.x

        def changeY( self ):
            self.axes.y = not self.axes.y

        def changeZ( self ):
            self.axes.z = not self.axes.z

        return [changeX, changeY, changeZ]