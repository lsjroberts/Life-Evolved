# -------- Sizeable.py --------
# An abstract sizeable trait
# --------

# General imports

# Panda3D imports

# Game imports

# -------- Sizeable --------
class Sizeable( Trait ):
    
    # Init
    # @param self
    # @return void
    def __init__( self, size = [1.0, 1.0, 1.0] ):
        self.size = size

    def mutations( self ):
        def changeX( self ):
            direction = randint(0,1)
            if direction == 0: direction = -1
            change = 10.0 - ( random() * 10 )
            return self.size[0] + direction * ( self.size[0] * change )

        def changeY( self ):
            direction = randint(0,1)
            if direction == 0: direction = -1
            change = 10.0 - ( random() * 10 )
            return self.size[0] + direction * ( self.size[0] * change )

        def changeZ( self ):
            direction = randint(0,1)
            if direction == 0: direction = -1
            change = 10.0 - ( random() * 10 )
            return self.size[0] + direction * ( self.size[0] * change )

        return [changeX, changeY, changeZ]