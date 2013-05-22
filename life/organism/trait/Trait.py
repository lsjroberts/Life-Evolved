# -------- Trait.py --------
# Generic genetic trait model.
# 
# A genetic trait can be affected by one or multiple genes:
# - Polygenic (multiple genes, one trait)
# - Pleitropic (one gene, multiple traits)
# - Mendelian (one gene, one trait)
# --------

# General imports
from random import randint

# Panda3D imports

# Game imports

# -------- Trait --------
class Trait( object ):
    mutationRate = 0
    
    # Init
    # @param self
    # @return void
    def __init__( self ):
        pass

    def mutations( self ):
        return [ ]

    # Attempt to mutate any of the available mutations
    # @return boolean If there was a mutation
    def mutate( self ):
        globalMutationRateModifier = 100
        mutations = self.mutations( )
        count = len( mutations )
        mutated = False

        for mutation in mutations:
            per = randint(0, 100 * count)
            if (per * globalMutationRateModifier) / 100 <= self.mutationRate:
                mutation( self )
                mutated = True

        return mutated