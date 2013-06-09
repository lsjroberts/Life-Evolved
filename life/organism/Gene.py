# -------- Gene.py --------
# Generic gene model
# --------

# General imports
from random import randint

# Panda3D imports

# Game imports

# -------- Gene --------
class Gene( object ):
    
    # Init
    # @param self
    # @return void
    def __init__( self, traits ):
        self.traits = traits

    # Create a potentially mutated copy of the gene
    # @param self
    # @return Gene
    def copy( self, mutate = False ):
        if mutate:
            copyTraits = []
            for trait in self.traits:
                trait.mutate( )
                copyTraits.append( trait )
        else:
            copyTraits = self.traits

        return Gene( copyTraits )